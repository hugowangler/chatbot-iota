"""
The CLI of the chatbot
"""
import sys
import click

# Fixes import problem
sys.path.append(".")
sys.path.append("..")

from src.subjects import get_subject  # pylint: disable=E0401, C0413


def respond(subject: str, positive: bool):
    """
    Returns a predefined response about the specified subject depending on if
    positive is true or not.
    """
    if positive:
        return f"You like {subject}."
    return f"You dislike {subject}."


@click.command()
def cli():
    """
    Starts the CLI and keeps it running until the user exits the application
    """
    click.clear()
    click.secho("Chatbot Iota - Welcome!", fg="green", bold=True)
    click.secho(
        "\nThe bot will prompt you about a subject and wait for your response,"
        + " it will then analyze the response and determine if you are"
        + " positive or negative towards the subject.",
        fg="green",
        bold=True,
    )

    suffix = click.style(">>> ", bold=True, fg="bright_cyan")

    try:
        # Continously asks questions about a subject until the user decides not
        # to continue or exit the CLI
        while True:
            subject = get_subject()
            click.echo(f"\nWhat do you think about {subject}?")
            answer = click.prompt("", prompt_suffix=suffix).strip()
            if answer == "":
                continue
            prediction = False  # TODO: get prediction here (boolean)
            click.echo(respond(subject, prediction) + "\n")

            click.confirm("Do you want to continue?", default=True, abort=True)

    except Exception:  # pylint: disable=W0703
        click.secho("Exiting Chatbot Iota...", bold=True, fg="green")
        click.clear()


if __name__ == "__main__":
    cli()
