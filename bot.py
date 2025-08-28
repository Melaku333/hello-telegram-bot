from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# Option A: hardcode your token
# BOT_TOKEN = "YOUR_BOT_TOKEN"

# Option B: use environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Command handler function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello World!")

def main():
    # Build the bot application
    app = Application.builder().token(BOT_TOKEN).build()

    # Register the /start command
    app.add_handler(CommandHandler("start", start))

    # Run the bot until you stop it
    app.run_polling()

if __name__ == "__main__":
    main()
