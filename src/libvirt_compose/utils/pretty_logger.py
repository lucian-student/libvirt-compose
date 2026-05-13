

from rich.console import Console

console = Console()

class Log:
    @staticmethod
    def info(message: str):
        console.print(f"[bold blue]INFO[/bold blue]    | {message}")

    @staticmethod
    def success(message: str):
        console.print(f"[bold green]SUCCESS[/bold green] | {message} :white_check_mark:")

    @staticmethod
    def error(message: str):
        # Using 'stderr=True' is best practice for errors
        console.print(f"[bold red]ERROR[/bold red]   | {message} :pout:", style="red", stderr=True)

    @staticmethod
    def warn(message: str):
        console.print(f"[bold yellow]WARN[/bold yellow]    | {message} :warning:")