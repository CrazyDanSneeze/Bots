from telegram import Update
from youtube import channel_handle, channel_info, view_count, sub_count, video_count, thumbnail
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Start making bot commands


async def start(update:Update, *args):
    await update.message.reply_text(f"Welcome to the YT Bot, don't forget to subscribe to {channel_handle}")


async def channel_stats(update: Update, *args):
    import requests
    from pathlib import Path

    Path("channel_photo.jpg").write_bytes(requests.get(thumbnail).content)
    await update.message.reply_photo("channel_photo.jpg")
    await update.message.reply_text(f"""
        Here's all the details of your Youtube channel master Joseph\n
        Videos: {video_count}, \n
        Total Views: {view_count}, \n
        Subscriber Count: {sub_count}
    """)

async def handle_messages(update:Update, *args):
    await update.message.reply_text("As a youtube chatbot, my job is to provide information about your channel, not engage in meaningless conversations with you")

if __name__ == "__main__":
    api_token = "7602831168:AAEz9U3Hx2_a-rGvnJMsYNGUJ4zqlpHOgwI"

    app = Application.builder().token(api_token).build()

    # Commands
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('stats', channel_stats))

    app.add_handler(MessageHandler(filters=filters.TEXT, callback=handle_messages))

    app.run_polling(poll_interval=3)