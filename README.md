# CheerTunes

## Overview

CheerTunes is an idea based on the awesome [CheerLights](https://cheerlights.com) by Hans Scharler.

The idea is that we have a shared big shared mystery jukebox. People can tweet playlists @CheerTunes and any connected devices will play them.

In future we want to support natural language tweets and a range of platforms including Spotify, Amazon Music, and Google Play Music.

For now this prototype is limited to tweeting Spotify URIs which are then played on a Spotify Premium account.

- we support Spotify albums, playlists and artists, but not indivdual tracks at this time.
- you need to follow the instructions to set up a Spotify developer account for your Spotify premium account and then create your own "app" to use
- you can play on your local desktop Spotify app or any other connected device, including Amazon Alexas.

There is a Python script which provides the "glue" between CheerTunes publishing commands via MQTT and controlling the Spotify web API.

## How to tweet to CheerTunes

An example is this tweet: "Hey @CheerTunes play spotify:album:5dN7F9DV0Qg1XRdIgW8rke"

- To find the Spotify URI run up Spotify and search for an artist or album or playlist you want to play.
- Then click ... and "Share->". This will show "Copy Album Link". Then press the ALT key and this will change to "Copy Spotify URI"
- Copy the URI and it will be of a similar form to "spotify:album:5dN7F9DV0Qg1XRdIgW8rke"
- Then tweet as in the above example
- Cheertunes will tweet what is currently playing in response

## Setup

Follow these steps to configure up your local PC system to play tunes from CheerTunes.

- Firstly we assume you have an existing Spotify account and have installed the Spotify application. **YOU NEED A PREMIUM SPOTIFY ACCOUNT FOR THIS TO WORK**
- Next create a Spotify developer account here [https://developer.spotify.com](https://developer.spotify.com)
- Log in and go to the developer dashboard here [https://developer.spotify.com/dashboard/](https://developer.spotify.com/dashboard)
- Create an "app" and give it a name, e.g. CheerTunes
- Edit the app settings and add a dummy "redirect" say [http://127.0.0.1/dummy](http://127.0.0.1/dummy) and save these settings
- Copy down the client ID (e.g. 5c2e949d1ee548xxxxxxx ) and the client secret (e.g. c7c6c4d471f74e.....)
- Edit the `cheerlights_spotify.sh` file to set `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` to what you have just copied down.
- If you have changed the dummy URL then change `SPOTIPY_REDIRECT_URI` to what you have used.
- Next run `./cheerlights_spotify.sh`. This will run `cheerlights_spotify.py`, connect to the CheerTunes broker and wait for MQTT messages to be received
- When a Spotify play command is received the script will connect to your application via the Spotify Web API to play the required URI
- **NOTE** The first time the script connects to Spotify Web API you will be asked to authenticate via a browser. Click "Agree" and the browser will be directed to the "dummy" URL you provided with extra "token" information. The browser will fail to go to the URL as it is a dummy but copy this and enter it into the command line for the script to authenticate. This information is cached in a `.cache` file so if you ever need to re-authenticate remove this file
- The next time you connect to the Spotify Web API the cached authentication token will be used and it will all "just work"(tm)

