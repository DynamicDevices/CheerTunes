#!/bin/env python3

import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import paho.mqtt.client as mqtt

broker="mqtt.cheertunes.co.uk"
port=1883

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to Cheerlight Broker with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("cheertunes/spotify/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.topic == "cheertunes/spotify/command/play":
        print("Got a play command: " + msg.payload.decode())
        # Get URI part (I haven't quite sorted out the flow for this so
        # let's catch problems
        try:
            json_cmd = json.loads(msg.payload.decode())
            uri = json_cmd[0]["context_uri"]
            sp.start_playback(context_uri=uri)
        except:
            print("Exception handling message");
    elif msg.topic == "cheertunes/spotify/info/playing":
        print("Got some info: " + msg.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
