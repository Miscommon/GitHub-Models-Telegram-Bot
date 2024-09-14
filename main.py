from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, Updater
import azure_module
import os
from dotenv import load_dotenv

load_dotenv()

#Variables initialization
TOKEN = os.getenv("TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Thank you for testing this bot! \n" + 
                                    "\n" +
                                    "Спасибо за участие в тестировании бота! \n")
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Просто спрашивайте бота о чем либо, и нейросеть ответит на ваш вопрос. Главное: не стоит спрашивать о неприличных и ужасных вещах по типу вреда себе! \n" +
                                    f"Также вы можете добавить GPT в группу, и тогда, любой участник может задать вопрос нейросети просто добавив {BOT_USERNAME} в начало сообщения. \n" +
                                    "\n" +
                                    "Just ask the bot about anything, and the neural network will answer your question. The main thing: do not ask about indecent and terrible things like harming yourself! \n" +
                                    f"You can also add GPT to the group, and then any participant can ask the neural network a question simply by adding {BOT_USERNAME} to the beginning of the message. \n" +
                                    "\n" +
                                    "Contact the developer/Связаться с разоаботчиком: ")

async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(azure_module.response_request("test"))

#Handlers
def response_handler(text: str) -> str:
    response = azure_module.response_request(text)
    return response

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'[LOG] User ({update.message.chat.id}:{update.message.chat.full_name}) ({message_type}): "{text}"')

    if message_type == 'group' or message_type == 'supergroup':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = response_handler(new_text)
        else:
            return
    else:
        response: str = response_handler(text)

    print(f'[LOG] GPT-4o: {response}')
    await update.message.reply_text(f'{response}')

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'[ERROR] Update {update}: {context.error}')

#MAIN
if __name__ == '__main__':
    print("[INFO] Bot initialized...")
    app = Application.builder().token(TOKEN).build()
    print("[INFO] Application.build: SUCCESS")

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('test', test_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, message_handler))

    #Errors handler
    app.add_error_handler(error)

    print("[INFO] Bot polling started...")
    app.run_polling(poll_interval=1)