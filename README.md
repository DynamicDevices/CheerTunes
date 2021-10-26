# Overview

CheerTunes is an idea based on the awesome [CheerLights](https://cheerlights.com) by Hans Scharler.

The idea is that we have a shared big shared mystery jukebox. People can tweet playlists @CheerTunes and any connected devices will play them.

In future we want to support natural language tweets and a range of platforms including Spotify, Amazon Music, and Google Play Music.

For now this prototype is limited to tweeting Spotify URIs which are then played on a Spotify Premium account.

- we support Spotify albums, playlists and artists, but not indivdual tracks at this time.
- you need to follow the instructions to set up a Spotify developer account for your Spotify premium account and then create your own "app" to use
- you can play on your local desktop Spotify app or any other connected device, including Amazon Alexas.

There is a Python script which provides the "glue" between CheerTunes publishing commands via MQTT and controlling the Spotify web API.

# How to tweet to CheerTunes

An example is this tweet: "Hey @CheerTunes play spotify:album:5dN7F9DV0Qg1XRdIgW8rke"

- To find the Spotify URI run up Spotify and search for an artist or album or playlist you want to play.
- Then click ... and "Share->". This will show "Copy Album Link". Then press the ALT key and this will change to "Copy Spotify URI"
- Copy the URI and it will be of a similar form to "spotify:album:5dN7F9DV0Qg1XRdIgW8rke"
- Then tweet as in the above example
- Cheertunes will tweet what is currently playing in response

# Grabbing the code

You can check out from the GitHub repo with

```
git clone https://github.com/DynamicDevices/cheertunes
```

Or if you prefer to download and unzip you can download from

```
https://github.com/DynamicDevices/cheertunes/releases
```

# Dependencies

- You need to have Python3 and "pip" installed. For details see [here](https://www.python.org/downloads) and [here](https://www.makeuseof.com/tag/install-pip-for-python)
- Then install the two required packages (Paho.MQtt and SpotiPy) with

```
$ cd cheertunes
$ pip install -r requirements.txt
```

# Configuration

Follow these steps to configure up your local PC system to play tunes from CheerTunes.

- Firstly we assume you have an existing Spotify account and have installed the Spotify application. **YOU NEED A PREMIUM SPOTIFY ACCOUNT FOR THIS TO WORK**
- Next create a Spotify developer account here [https://developer.spotify.com](https://developer.spotify.com)
- Log in and go to the developer dashboard here [https://developer.spotify.com/dashboard/](https://developer.spotify.com/dashboard)
- Create an "app" and give it a name, e.g. CheerTunes

![Spotify Dashboard App](https://www.cheertunes.co.uk/images/SpotifyDevDash.png)

- Edit the app settings and add a dummy "redirect" say [http://127.0.0.1/dummy](http://127.0.0.1/dummy) and save these settings
- Copy down the client ID (e.g. 5c2e949d1ee548xxxxxxx ) and the client secret (e.g. c7c6c4d471f74e.....)
- Edit the `cheertunes_spotify.sh` file to set `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` to what you have just copied down.
- If you have changed the dummy URL then change `SPOTIPY_REDIRECT_URI` to what you have used.
- Next run `./cheertunes_spotify.sh`. This will run `cheertunes_spotify.py`, connect to the CheerTunes broker and wait for MQTT messages to be received
- When a Spotify play command is received the script will connect to your application via the Spotify Web API to play the required URI
- **NOTE** The first time the script connects to Spotify Web API you will be asked to authenticate via a browser. Click "Agree".

![Spotify Accept Page](https://www.cheertunes.co.uk/images/SpotifyAccept.png)

- The browser will be directed to the "dummy" URL you provided with extra "token" information. The browser will fail to go to the URL as it is a dummy but copy this.

![Spotify Browser URL example](https://github.com/DynamicDevices/cheertunes/blob/main/images/SpotifyAuthCopyURL.png)

- Then enter it into the waiting command line for the script to authenticate. 

![CheerTunes Script Entry](https://www.cheertunes.co.uk/images/SpotifyAuthURIEntry.png)

- This information is cached in a `.cache` file so if you ever need to re-authenticate remove this file

- The next time you connect to the Spotify Web API the cached authentication token will be used and it will all "just work"(tm)

# Playing Tunes !!!

Then tweet something like the example above, you will see an MQTT message received with the Spotify URI and it should play.

**NOTE**: The script does not currently automatically start playing tunes on your Spotify account as that could be very irritating. You must **first** already be playing some tune on either the local system or some other Spotify device and playback will switch to the new UID
