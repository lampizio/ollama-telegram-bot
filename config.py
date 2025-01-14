from os import getenv

from dotenv import load_dotenv


class Config:
    """
    This class includes configuration variables.
    """
    api_token: str = ""
    llama_model: str = ""

    @classmethod
    def load_credentials(cls):
        load_dotenv()

        cls.api_token = getenv("API_TOKEN")
        cls.llama_model = getenv("LLAMA_MODEL")
