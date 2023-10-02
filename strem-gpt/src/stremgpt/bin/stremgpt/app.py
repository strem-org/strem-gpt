import sys
import openai

from stremgpt.translator import Translator

class Application():
    """The main application.
    """

    def __init__(self, key: str, org: str, query: str) -> None:
        """Initialize the application.
        """

        self._key = key
        self._org = org
        self._query = query

        # Set the API key used for OpenAI requests.
        openai.organization = self._org
        openai.api_key = self._key

    def run(self, model: str) -> None:
        """Run the main application.
        """

        translator = Translator(model)

        if self._query:
            translation = translator.run(self._query)
            print(translation)

            return

        # Run the application interactively to submit multiple requests to the
        # translator without resetting.
        while True:
            line = input(">> ")
            print(translator.run(line))
