from telegram import Update
from telegram.ext import ContextTypes
from ollama import chat, ChatResponse

from config import Config


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Let's get started!")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("No help :D")


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response: ChatResponse = chat(model=Config.llama_model, messages=[
        {
            "role": "user",
            "content": update.message.text
        }
    ])

    await update.message.reply_text(response.message.content)
