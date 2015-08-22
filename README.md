# SlackMinecraftRelay

Usage: run python on rtmbot.py in the SlackBot folder and python Spockbot.py in separate windows.  

![Screenshot](https://i.imgur.com/HMzoJdw.png)

Requires: pyslack-real python-slackclient python-rtmbot and SpockBotMC

You can install these by running:

```pip install pyslack-real python-slackclient python-rtmbot```

NOTE: Spockbot will need to be installed by itself, as it does not have any package (yet).

See http://github.com/spockbotmc/spockbot for installation instructions. 

Notes: There's a lot of files that need your personal settings in there. Until I get a YML config file, just look at each file and fill in your appropriate settings. Off the top of my head, you'll need your minecraft password, minecraft email, slack API token, slack channel ID (obtainable through Slack API website), and the civcraft namelayer group name in which the bot will chat in. 

MAKE SURE YOU INVITE YOUR BOT INTO THE CHANNEL IN WHICH IT WILL BE MONITORING OR ELSE IT WON'T SEE ANY NEW MESSAGES
