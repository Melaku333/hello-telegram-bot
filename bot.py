from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# Get bot token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello World! Your bot is online on Render 🚀")

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing! Please set it in Render environment variables.")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
