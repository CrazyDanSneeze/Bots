from facts import get_fact
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os

load_dotenv()

# What do we wanna do
# A bot needs commands, so let's create some for it
# When we're done, we want the bot to package everything
api_token = os.getenv("API_KEY")
async def start(update:Update, *args):
    await update.message.reply_text(text="Welcome to the bot of useless information, request away, and ill tell you what you didn't care to know")

async def random_fact(update:Update, *args):
    msg = get_fact()
    await update.message.reply_text(text=msg)

async def handle_error(update:Update, *args):
    await update.message.reply_text(text="Sorry, we seem to be running into a bit of an issue, ill see what's going on")

async def handle_messages(update:Update, *args):
    await update.message.reply_text(text="I don't understand what you're saying.")

if __name__ == "__main__":
    app = Application.builder().token(api_token).build()
    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("facts", random_fact))


    app.add_handler(MessageHandler(filters=filters.TEXT, callback=handle_messages))

    app.run_polling(poll_interval=3)