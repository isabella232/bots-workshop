# HubSpot Bot Workshop

🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖

We have a chatbot product at HubSpot that allows our users to build chatbots to interact with their users. Inside that product there is the option to write a code snippet to control the bot. During this workshop we are going to build some code snippets to make some sick bots.

## Our Agenda For Today

1. Create and configure a basic chatbot
2. Demo example code snippet chatbot
3. Create and run code snippets on your own bots
4. Go through how HubSpot chatbots execute code snippets

<!-- ## Creating a New Portal (Did this in the beginning of the talk)

1. Go to https://www.hubspot.com/products/get-started
2. Click on "Get Started Free" for Marketing Hub
3. Create an account and input any webpage url you want that isn't taken
    - You can hook up a personal website if you have one or just make up one that you want (you can always change this in the future)
4. Just select "1" for how many employees work at your company, and "Other" for job role
5. Select "Yes" or "No" depending on if you are using a website that you have previously created
6. If you are using a website that you have previously created, you will have to add the embed code into your website. Else, you can skip this step.
    - This might turn out to be a pain, so feel free to go back a couple of steps and just create a made-up url for the purpose of this tutorial, and you can go back and hook up your own later -->

## Creating a New Chat Bot

1. Create an account by responding to the email invitation
2. Go to "Conversations -> Chatflows" in the top nav of the portal after signing in
3. Click "More -> Clone" on the Chatflow named "Blank Bot"
4. Enter a unique name for your Bot Chatflow
5. Find your new chatflow in the table
6. Click "More -> Move to top Priority"
7. Click "Edit"
8. Configure targeting
    - set the targeting url to something unique
    ![Alt text](unique-url.png?raw=true "Unique Url in targeting")
9. Toggle the switch in the top right corner of the page
10. Preview bot in sandbox
    - go to https://app.hubspot.com/conversations-visitor-sandbox/8398068?showConfig=true&portalId=8398068
    - configure subroute to match your unique targeting url

    ![Alt text](subroute.png?raw=true "Sub route in sandbox")


you should see something like this:

![Alt text](base-bot.png?raw=true "base bot")



## Next Steps

Let's build a bot! There are a bunch of different things bots can do, but most make an api request and echo some data. Here are a few examples:

1. [Cat fact bot](cat-fact-bot.js)
2. [Stock Bot](stock-bot.js)
3. [Trivia bot](https://github.com/MotionAI/nodejs-samples/blob/master/triviabot.js)
    - NOTE: This is an example from MotionAI's implementation (MotionAI is a software company that develops and "trains" chatbots that HubSpot acquired a year ago), so try to incorporate this example into your own
4. [Beer bot](beer-bot.py)
    - Created by Steve Rowell at HubSpot. This bot uses python which is not available to all at this time, but shows that you can collect information through quick replies in the lambda through creating a session and having states stored in a contact property. At HubSpot, we have beer on tap in a bunch of different locations, and using pubspot API, he created a way to output what's on tap. Super cool!

Potential public APIs you can use can be found here: https://github.com/toddmotto/public-apis

### How It Works
Behind the scenes we take your javascript function and upload it to AWS Lambada where it waits to be executed by the bot. AWS Lambda is a serverless code execution environment. It's really great at running a single snippet of code without the requirement of setting up the server environment to run the code.


### Resources on lambda:
1. [AWS Lambda: How it Works](https://aws.amazon.com/lambda/)
2. [Benchling CRISPR Case Study](https://aws.amazon.com/solutions/case-studies/benchling/)
3. [Creating AWS Lambda Function Through AWS Console ](https://medium.freecodecamp.org/going-serverless-how-to-run-your-first-aws-lambda-function-in-the-cloud-d866a9b51536)

🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖
