import smtplib, ssl
from email.mime.text import MIMEText

import os
from os.path import join, dirname
from dotenv import load_dotenv

import discord

from datetime import datetime

dotenv_path = join(dirname(__file__), 'config.env')
load_dotenv(dotenv_path)

# mail-settings
mail_from = os.environ.get("sender-address")
mail_pw = os.environ.get("sender-pw")
mail_to = os.environ.get("destination")

# mail log in
server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
    context=ssl.create_default_context())#smtp adress and port here.(this is gmail settings)
server.login(mail_from, mail_pw)

client = discord.Client()

# discord log in
@client.event
async def on_ready():
    print("Login succeeded!")

@client.event
async def on_message(message):
    if message.channel.id == 12345 or message.channel.id == 12345:#discord channel ID here(int)
        subject = "subject(like 'notice from discord')"
        info = message.content
        body = info
        message = MIMEText(body, "html")
        message["Subject"] = subject
        message["To"] = mail_to
        message["From"] = mail_from
        
        server.send_message(message) # send an  email
        print(datetime.now())#timestamp
        print("An e-mail was sent.\n")

client.run(os.environ.get("token"))