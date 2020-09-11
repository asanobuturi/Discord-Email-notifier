# Discord-Email-notifier
A discord bot which send an e-mail when a message was sent on a specific channel.

## REQUIRED MODULES
Expect for standard modules,we need

* Discord.py
* python-dotenv

## config.env settings
|  name  |  content  |
| ---- | ---- |
|  sender-adress  |  sender's email adress(ex. example@gmail.com)  |
|  sender-pw |  sender's email pw  |
| distination | distination email adress.you can use comma like "example@gmail.com,instance@gmail.com".
| token | token of your discord-bot.

# source.py settings

| line | content |
| ---- | ---- |
| 21 | the mail-provider's smtp-server adress and its port here.
| 34 | bot will send an email when a message was sent on the channel which was mentionned here. |
| 35 | you can set the email's subject here. |