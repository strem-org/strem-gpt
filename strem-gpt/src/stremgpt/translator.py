import os
import openai

class Translator:
    """A natural language to SpRE translator.
    """

    def __init__(self, model: str) -> None:
        """
        """

        with open(os.path.join(os.path.dirname(__file__), "data/template.txt"), "r") as infile:
            self._template = infile.read()

        self._model = model

    def run(self, query: str) -> str:
        """Run the translation procedure.
        """

        translation = openai.ChatCompletion.create(
            model=self._model,
            messages=[
                {"role": "system", "content": "You are a translator."},
                {"role": "assistant", "content": "Given a query as a natural language statement, you must translate the statement into a valid Spatial Regular Expression (SpRE)."},
                {"role": "user", "content": self._template},
                {"role": "user", "content": query}
            ],
            temperature=0,
        )

        return translation["choices"][0]["message"]["content"]
