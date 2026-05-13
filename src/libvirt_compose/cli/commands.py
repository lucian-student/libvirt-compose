import typer
from libvirt_compose.utils.pretty_logger import Log

app = typer.Typer()


@app.command()
def up():
    Log.info("Bringing up infrastructure!")


@app.command()
def down():
    pass


@app.command()
def destroy():
    pass


@app.command()
def apply():
    pass
