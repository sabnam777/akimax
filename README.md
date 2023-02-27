# Telegram Bot

This is a simple Telegram bot built using Pyrogram that provides some basic features such as joining a group or channel, buying a premium subscription, and making a donation.

## Features

- Join group or channel
- Buy premium subscription
- Make a donation

## Getting Started

To get started, you will need to create a Telegram bot and obtain its API token. Follow these steps to create your bot:

1. Open Telegram and search for the "BotFather" bot.
2. Send "/newbot" to the BotFather and follow the instructions to create a new bot.
3. Copy the API token that the BotFather provides.

Once you have your API token, create a file called `config.ini` in the root directory of your project, and add the following contents to the file:

[pyrogram]
api_id = YOUR_API_ID
api_hash = YOUR_API_HASH
bot_token = YOUR_BOT_TOKEN


```Replace `YOUR_API_ID`, `YOUR_API_HASH`, and `YOUR_BOT_TOKEN` with your own values.

## Usage

To run the bot, simply execute the following command:

```sh
python main.py```


##Contributing
Contributions are welcome! Please create a pull request with your changes.

##License
This project is licensed under the MIT License.

Feel free to customize the contents to better fit your project.
