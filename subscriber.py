#!/usr/bin/env python3
# -*- coding:utf-8 -*-
print ("Content-type: text/html\n\n")

import paho.mqtt.client as mqtt
import struct
import requests
import json
import time
from stressdetector.estimate.Model import CalcStress

array = []
data = [0] * 13
model = CalcStress()
# for debug
#data = [0.026666667, 0.038333333, 0.035, 0.034166667, 3.441666667, 2.605833333, 0.003333333, -9.423516667, 44.066525, 325.55855, 2.166822917, 8.16390625, -11.674375]
def on_connect(client, userdata, flags, respons_code):
    topic = 'jins-meme/#'
    print('watch %s' % topic)
    client.subscribe(topic)


def on_message(client, userdata, msg):
    global data
    d2 = struct.unpack('>d', msg.payload)
    if msg.topic == 'jins-meme/EyeMoveUp':
        data[0] = d2[0]
    elif msg.topic == 'jins-meme/EyeMoveDown':
        data[1] = d2[0]
    elif msg.topic == 'jins-meme/EyeMoveLeft':
        data[2] = d2[0]
    elif msg.topic == 'jins-meme/EyeMoveRight':
        data[3] = d2[0]
    elif msg.topic == 'jins-meme/BlinkSpeed':
        data[4] = d2[0]
    elif msg.topic == 'jins-meme/BlinkStrength':
        data[5] = d2[0]
    elif msg.topic == 'jins-meme/Walking':
        data[6] = d2[0]
    elif msg.topic == 'jins-meme/Roll':
        data[7] = d2[0]
    elif msg.topic == 'jins-meme/Pitch':
        data[8] = d2[0]
    elif msg.topic == 'jins-meme/Yaw':
        data[9] = d2[0]
    elif msg.topic == "jins-meme/AccX":
        data[10] = d2[0]
    elif msg.topic == 'jins-meme/AccY':
        data[11] = d2[0]
    elif msg.topic == 'jins-meme/AccZ':
        data[12] = d2[0]
        value = model.Calc(data)
        return_message(struct.pack('>d', value))
        print(value)
        array.clear()
        array.append(value)
#        f.write(str(value))
        if ( value >= 3) :
            send_message_to_slack(value, "Detect stress. finish your work and go back to home!!!")
        else :
            send_message_to_slack(value, "stress not detected. work harder")
        with open('/home/ubuntu/value.csv', 'w') as f:
            for row in array:
                f.write(str(row)+'\n')
        f.close()

def send_message_to_slack(value, msg):
    WEB_HOOK_URL = "https://hooks.slack.com/services/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"
    text = msg+"(stress rate):"+str(value)
    print(text)
    array.append(str(text))
    requests.post(WEB_HOOK_URL, data = json.dumps({
        'text': text,  #CONTENTS
        'username': u'JiNS-MEME-AWS-Bot',  #USER NAME
        'icon_emoji': u':smile_cat:',  #ICON
        'link_names': 1,  #LINKING NAME
    }))
    print('Message sent to slack')

def on_publish(client,userdata,result):
    time.sleep(0.2)
    pass

def return_message(value):
    try:
        client_publish = mqtt.Client()
        client_publish.connect('ec2-13-125-237-148.ap-northeast-2.compute.amazonaws.com', 1883, keepalive=60)
        client_publish.on_publish = on_publish
        client_publish.publish('jins-meme-stress', value, 0, retain=True)
    except:
        print('Error at returning message')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('ec2-13-125-237-148.ap-northeast-2.compute.amazonaws.com', 1883, keepalive=60)
client.loop_forever()

