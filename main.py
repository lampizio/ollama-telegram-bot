from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from bot import reply


def main(api_token: str) -> None:
    application = Application.builder().token(api_token).build()

    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, reply))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    api_token = "YOUR_API_TOKEN_HERE"

    main(api_token)
