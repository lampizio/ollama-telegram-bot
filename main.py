from telegram import Update
from telegram.ext import Application, MessageHandler, filters

from bot import reply
from config import Config


def main() -> None:
    application: Application = Application.builder().token(Config.api_token).build()

    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, reply))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    Config.load_credentials()

    main()
