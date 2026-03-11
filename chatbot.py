import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler


# We create different commands for different processes that get executed

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    # this is the most important command, just to welcome the user
    await update.message.reply_text(text="Hello user, welcome to the best chatbot in the whole world")

async def echo(update:Update, context:ContextTypes.DEFAULT_TYPE):
    # this is a command that repeats whatever the user said back
    text = update.message.text
    await update.message.reply_text(text=text)

async def handler(update:Update, context:ContextTypes.DEFAULT_TYPE):
    # this is used to handle text
    await update.message.reply_text(text="I'm just a simple retarded chatbot, I don't know anything")

if __name__ == "__main__":
    app = Application.builder().token("8147604268:AAHzjjVPFnD4e8nbBGqkB_NjRzpXIMLcGSU").build()
    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("echo", echo))

    app.add_handler(MessageHandler(filters=filters.TEXT, callback=handler))

    app.run_polling(5)