# SlackMinecraftRelay

Usage: run python on rtmbot.py in the SlackBot folder and python Spockbot.py in separate windows.  

![Screenshot](https://i.imgur.com/HMzoJdw.png)


Installation
-----------

Requires: pyslack-real slackclient python-rtmbot and SpockBot

Pyslack and slack client can be installed via pip:

```pip install pyslack-real slackclient ```

After that, install the rtmbot needed for getting real-time messages from slack:

1. Download the python-rtmbot code

        git clone git@github.com:slackhq/python-rtmbot.git
        cd python-rtmbot

2. Install dependencies ([virtualenv](http://virtualenv.readthedocs.org/en/latest/) is recommended.)

        pip install -r requirements.txt

Finally, install Spockbot. Good luck! If you don't have them installed already, you'll need python3-setuptools and python3-dev to compile cryptography. See http://github.com/spockbotmc/spockbot for the full installation instructions. 

Notes
-----------

There's a lot of files that need your personal settings in there. Until I get a YML config file, just look at each file and fill in your appropriate settings. Off the top of my head, you'll need your minecraft password, minecraft email, slack API token, slack channel ID (obtainable through Slack API website), and the civcraft namelayer group name in which the bot will chat in. 

MAKE SURE YOU INVITE YOUR BOT INTO THE CHANNEL IN WHICH IT WILL BE MONITORING OR ELSE IT WON'T SEE ANY NEW MESSAGES
