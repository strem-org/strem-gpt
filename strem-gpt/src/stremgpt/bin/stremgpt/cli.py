import click

from .app import Application

@click.command()
@click.option("-k", "--key", "key", type=str, help="Your API key provided by OpenAI.")
@click.option("-o", "--org", "org", type=str, help="Your organization key to bill the request to.")
@click.option("-m", "--model", "model", default="gpt-3.5-turbo", type=str, help="The LLM identifier to use provided by OpenAI.\n\nModel Identifiers: \"gpt-4\", \"gpt-4-0613\", \"gpt-4-32k\", \"gpt-4-32k-0613\", \"gpt-3.5-turbo\", \"gpt-3.5-turbo-0613\", \"gpt-3.5-turbo-16k\", \"gpt-3.5-turbo-16k-0613\"")
@click.argument("query", required=False, default=None, nargs=1)
def cli(key, org, query, model) -> None:
    """The command-line interface.
    """

    app = Application(key, org, query)
    app.run(model)
