# Github Models Telegram Bot
#### This mini-project allows you to quickly create and launch your own simple neural network chat bot in Telegram based on any model provided by GitHub Models.

## Installation

 1. Create telegram bot via @BotFather and get bot token
 2. Clone this repo:\
 `git clone https://github.com/S0lnyx/GitHub-Models-Telegram-Bot.git`
 3. Go to repo directory:\
 `cd GitHub-Models-Telegram-Bot`
 4. Create python3 venv and install reuired modules (before make sure you installed python3-full package):
 ```bash
 python3 -m venv .venv
 source .venv/bin/activate
 python3 -m pip install -r requirements.txt
 ```
 5. Create config file:
 ```bash
 sudo touch .env
 sudo nano .env
 ```
 6. Write required parameters:
 ```
 GITHUB_KEY = "Your_presonal_access_token_goes_here"
 TOKEN = "Your_telegram_bot_token"
 BOT_USERNAME = "@YourBotUsername"
 MODEL_NAME = "Model_name_from_models_marketplace"
 ```
 Your personal GitHub key that be used as API Key to authenticate in Azure module and get access to GitHub models service, you can generate it here: https://github.com/settings/tokens, no special permissions for the token needed.

 Save .env file

 7. Customize bot responses for `/help` `/start` and `/test`
 To change bot responses on these commands, edit cofig.ini file
 ```
 Help_command_response - Text of the message after /help command
 Start_command_response - Text of the message after /start command
 Test_command_promt - Prompt for model to check functionality (/test)
 ```
 8. Start the bot
 ```
 python3 main.py
 ```

 Done!

 ## Note from author
 #### This is my first repository like this written in Python for practical purposes, this repository is still subject to improvement, but you are also free to take this code, modify it or leave any comments or suggestions, I will read them all and take them into consideration.
