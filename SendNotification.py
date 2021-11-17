# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 17:14:59 2021

@author: Daniel Kuknyo

This script will be the template to send a notification to a phone via the Telegram API

STEPS TO TAKE BEFORE:
1) Get a Telegram account (free) using your phone number
Web: https://web.telegram.org Also download the Telegram Android. 

2) Go into settings (web or app) and set a username
This is needed to obtain an id which your bot will use to send messages to.

3) Send a message to RawDataBot to get your id
Just search for RawDataBot and send any message (hi will do). Take a note of your id.

4) Create your bot (which you'll command with HTTP requests)
Now search for BotFather and send the message /start. Help is displayed. 
Send the message /newbot and follow the instructions. 
Take a note of your token to access the HTTP API

TELEGRAM E-CHANNEL ID FOR WEDS
Alina: 923197636
Dani: 2140059741
Sofien: 2132359615
"""

import requests

token = "2127036493:AAFzTiQxgRNerbsNAD__4NqpWyumUttImL0"

url = f"https://api.telegram.org/bot{token}" # Here comes the token from step 4

params = {"chat_id": "923197636", "text": "Did u get this message?"} # Here comes the token from step 3

r = requests.get(url + "/sendMessage", params=params)
