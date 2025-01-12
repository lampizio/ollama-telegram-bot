from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Let's get started!")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("No help :D")


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)
