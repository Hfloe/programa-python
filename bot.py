import os, threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("TOKEN")
MENSAJE = "Hola soy asistente de Harold"

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if update.business_message:
            await update.business_message.reply_text(MENSAJE)
        elif update.message:
            await update.message.reply_text(MENSAJE)
    except:
        pass

def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, responder))
    app.run_polling()

threading.Thread(target=run_bot, daemon=True).start()
web = Flask(__name__)

@web.route('/')
def home():
    return "Bot activo"

if __name__ == "__main__":
    web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
