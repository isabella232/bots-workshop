import requests
import json
import os
import time
import base64
import pickle as pickle

API_KEY = os.environ["API_KEY"]

BEER_STATE_NAME = "beer_bot_state"
BEER_STATE_DATA = "beer_state_data"

STATES = ["SEND_BUILDINGS", "COLLECT_BUILDINGS", "SEND_KITCHEN", "COLLECT_KITCHEN"]


def main(event):
    botMessage = {'responseExpected': "true", 'disableUserInput': "true"}

    vid = event['session']['vid']

    beerSession = BeerSession.factory(vid)

    userMessage = event['userMessage']['message']

    if userMessage == "Nuke my session!":
        beerSession.clearSession()
        beerSession = BeerSession.factory(vid)

    STATE = beerSession.getState()

    if STATE == "SEND_BUILDINGS":
        botMessage['botMessage'] = "Awesome, where do you want some beer?"
        quickReplies = []

        for key in beerSession.getBeerData().keys():
            quickReplies.append({"value": key, "label": key})

        botMessage['quickReplies'] = quickReplies
        beerSession.setState("COLLECT_BUILDINGS")

    elif STATE == "COLLECT_BUILDINGS":
        building = event['userMessage']['message']
        beerSession.writeSessionValue("building", building)

        botMessage['botMessage'] = "Awesome! What area in {}?".format(building)

        quickReplies = []
        for key in beerSession.getBeerData()[building].keys():
            quickReplies.append({"value": key, "label": key})

        botMessage['quickReplies'] = quickReplies
        beerSession.setState("COLLECT_KITCHEN")

    elif STATE == "COLLECT_KITCHEN":
        area = event['userMessage']['message']
        tempMessage = "Awesome looking at the {} now! ::next-100:: Lets see I have... ".format(area)
        botMessage['botMessage'] = "Awesome looking at the {} now! ::next-1000:: Lets see I have... ".format(area)

        quickReplies = []
        for key in beerSession.getBeerData()[beerSession.getSessionValue("building")][area]:
            tempMessage = tempMessage + " ::next-2000:: " + key

        botMessage['quickReplies'] = quickReplies
        botMessage['botMessage'] = tempMessage
        botMessage['responseExpected'] = "false"

        beerSession.clearSession()
        return botMessage

    beerSession.writeSession()
    return botMessage

class BeerSession:
    def __init__(self, vid, state, beerData, sessionData):
        self.vid = vid
        self.state = state
        self.beerData = beerData
        self.sessionData = sessionData

    def factory(vid):
        dataMaybe = BeerSession.__fetchContactProperty__(vid, BEER_STATE_DATA);
        if dataMaybe is None or dataMaybe is '':
            aBeerSession = BeerSession(vid, "SEND_BUILDINGS", BeerSession.__buildBeerData__(), {})
            aBeerSession.writeSession()
            return aBeerSession
        else:
            externalSessionData = BeerSession.__decodeData__(dataMaybe)
            return BeerSession(vid, externalSessionData['state'], externalSessionData['beerData'],
                               externalSessionData['sessionData'])

    def writeSession(self):
        data = {"state": self.state, "beerData": self.beerData, "sessionData": self.sessionData}
        encodedData = base64.standard_b64encode(bytes(pickle.dumps(data)))

        url = "https://api.hubapi.com/contacts/v1/contact/vid/" + str(self.vid) + "/profile?hapikey=" + API_KEY
        json = {"properties": [{"property": BEER_STATE_DATA, "value": encodedData.decode("utf-8")}]}
        requests.post(url, json=json)

    def clearSession(self):
        url = "https://api.hubapi.com/contacts/v1/contact/vid/" + str(self.vid) + "/profile?hapikey=" + API_KEY
        json = {"properties": [{"property": BEER_STATE_DATA, "value": ""}]}
        requests.post(url, json=json)

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def getBeerData(self):
        return self.beerData

    def writeSessionValue(self, key, value):
        self.sessionData[key] = value

    def getSessionValue(self, key):
        if key in self.sessionData:
            return self.sessionData[key]
        return None

    def __decodeData__(data):
        return pickle.loads(base64.standard_b64decode(data))

    def __getAContact__(vid):
        url = "https://api.hubapi.com/contacts/v1/contact/vid/" + str(vid) + "/profile?hapikey=" + API_KEY
        return requests.get(url).json()

    def __fetchContactProperty__(vid, property):
        contact = BeerSession.__getAContact__(vid)
        if property in contact['properties']:
            return contact['properties'][property]['value']
        return None

    def __getBeer__(times):
        url = "http://pubspot.herokuapp.com/taps"
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        if times < 5:
            time.sleep(1)
            return BeerSession.__getBeer__(times + 1)

    def __getBeers__():
        return BeerSession.__getBeer__(1)

    def __buildBeerData__():
        beers = BeerSession.__getBeers__()
        buildings = {}
        for i in beers:
            aBuilding = json.dumps(i['location']['building']).strip('"')
            aRoom = json.dumps(i['location']['room']).strip('"')
            aBeer = json.dumps(i['beer']['name']).strip('"')
            if aBuilding not in buildings:
                buildings[aBuilding] = {}
            if aRoom not in buildings[aBuilding]:
                buildings[aBuilding][aRoom] = [aBeer]
            else:
                buildings[aBuilding][aRoom].append(aBeer)
        return buildings

    factory = staticmethod(factory)
    __decodeData__ = staticmethod(__decodeData__)
    __fetchContactProperty__ = staticmethod(__fetchContactProperty__)
    __getBeer__ = staticmethod(__getBeer__)
    __getBeers__ = staticmethod(__getBeers__)
    __buildBeerData__ = staticmethod(__buildBeerData__)
    __getAContact__ = staticmethod(__getAContact__)
