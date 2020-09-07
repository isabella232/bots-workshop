# HubSpot Bot Workshop

HubSpot bots allows its users to build chat bots to interact with their users. A part of bots is the option to write a code snippet to control the bot. During this workshop we are going to build some code snippets to make some sick bots.


<!-- ## Creating a New Portal (Did this in the beginning of the talk)

1. Go to https://www.hubspot.com/products/get-started
2. Click on "Get Started Free" for Marketing Hub
3. Create an account and input any webpage url you want that isn't taken
    - You can hook up a personal website if you have one or just make up one that you want (you can always change this in the future)
4. Just select "1" for how many employees work at your company, and "Other" for job role
5. Select "Yes" or "No" depending on if you are using a website that you have previously created
6. If you are using a website that you have previously created, you will have to add the embed code into your website. Else, you can skip this step.
    - This might turn out to be a pain, so feel free to go back a couple of steps and just create a made-up url for the purpose of this tutorial, and you can go back and hook up your own later -->

## Part 1: Getting Setup

1. Create an account by responding to the email invitation
2. Go to "Conversations -> Chatflows" in the top nav of the portal after signing in
3. Click "More -> Clone" on the Chatflow named "Blank Bot"
4. Enter a unique name for your Bot Chatflow
5. Find your new Chatflow in the table
6. Click "More -> Move to top Priority"
7. Click "Edit"
8. Configure targeting
    - set the targeting url to something unique

    <img src="img/unique-url.png?raw=true" width="500" />
9. Toggle the switch in the top right corner of the page
10. Preview bot in sandbox
    - go to https://app.hubspot.com/conversations-visitor-sandbox/8398068?showConfig=true&portalId=8398068
    - configure subroute to match your unique targeting url

    <img src="img/subroute.png?raw=true" width="400" />


you should see something like this:

<img src="img/base-bot.png?raw=true" width="300" />

## Part 2: Learning to build bots

All bots consist of three things:
1. A welcome message
2. A prompt to start the conversation
3. Follow up actions

### Welcome message
A welcome message is a way to tell your user the purpose of the bot. It will display in a pop up while the widget is closed so it should be something to encourage your visitors to interact with your bot.

<img src="img/welcome-message.png?raw=true" width="200" />
<img src="img/welcome-message-widget.png?raw=true" width="300" />

### Actions and Prompts
Bots require a prompt to start the conversation so it knows a user has started an interaction. Otherwise it could send an unlimited number of messages without any user interaction. The follow up actions can collect information from quick replies or user input, send images or text, and branch to other parts of the boarder conversation tree. When an action is configured to take in user input, the bot will use natural language processing to try and pick out the relevant information from the user response. For example if I configure my bot to save information to the contact address field, it will specifically look for an address.

![Alt text](img/actions.png?raw=true "actions")

### Connections
Connections are what tie together the bot actions into a conversation tree. Each action can be configured with a connection which will divert the bots conversation chain given certain parameters or responses. For example, if a visitor has already interacted with my bot or website and I've already collected their information I can divert my bot to skip the actions that collect that information. These connections can be found under the if/then branch tab of the bot action configuration panel.

![Alt text](img/connections.png?raw=true "connections")

## Part 2: Build a bot

Let's build a bot! There are a bunch of different things bots can do, but most make an api request and echo some data.

To help give some inspiration here is a list of public APIs https://github.com/toddmotto/public-apis

### Examples
1. [Cat fact bot](examples/cat-fact-bot.js)
2. [Stock Bot](examples/stock-bot.js)
3. [Trivia bot](https://github.com/MotionAI/nodejs-samples/blob/master/triviabot.js)
    - NOTE: This is an example from MotionAI's implementation (MotionAI is a software company that develops and "trains" chat bots that HubSpot acquired a year ago), so try to incorporate this example into your own
4. [Beer bot](examples/beer-bot.py)
    - Created by Steve Rowell at HubSpot. This bot uses python which is not available to all at this time, but shows that you can collect information through quick replies in the lambda through creating a session and having states stored in a contact property. At HubSpot, we have beer on tap in a bunch of different locations, and using pubspot API, he created a way to output what's on tap. Super cool!

New to javascript? Here's a [quick cheat sheet](https://javascript.pythoncheatsheet.org/) that goes over the syntax.

### Challenge

Can you make a bot with several code snippets and branching using `nextModuleNickname`?

## Part 3: How do bots system run code snippets?

Behind the scenes we take your javascript function and upload it to AWS Lambada where it waits to be executed by the bot. AWS Lambda is a serverless code execution environment. It's really great at running a single snippet of code without the requirement of setting up the server environment to run the code.

![Alt text](img/lambda.png?raw=true "lambda high level system diagram")

### Resources on lambda:
1. [AWS Lambda: How it Works](https://aws.amazon.com/lambda/)
2. [Benchling CRISPR Case Study](https://aws.amazon.com/solutions/case-studies/benchling/)
3. [Creating AWS Lambda Function Through AWS Console ](https://medium.freecodecamp.org/going-serverless-how-to-run-your-first-aws-lambda-function-in-the-cloud-d866a9b51536)

🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖
