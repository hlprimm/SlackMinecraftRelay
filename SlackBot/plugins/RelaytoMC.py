import time
from slackclient import SlackClient
import json
import sys


token = "SLACK TOKEN"      # found at https://api.slack.com/#auth)
sc = SlackClient(token)

crontable = []
outputs = []

def catch_all(data):
    if data['channel'] == 'SLACK CHANNEL ID' and data['type'] == 'message':
#        print (data['channel'], "from repeat1 \"{}\" in channel {}".format(data['text'], data['channel']))
#        outputs.append([data['channel'], "from repeat1 \"{}\" in channel {}".format(data['text'], data['channel']) ])
#       print data
        userdata = json.loads(sc.api_call("users.info", user=data['user']))
        username = userdata['user']['name']
        messagetext = data['text']
        print 'Received message from', username
        f = open('../../SpockBotMC/slacktomc.txt','a')
        f.write("{} : {}".format(username, messagetext + '\n'))
#        f.write('\n')
        f.close()
#        outputs.append([str(data)])
