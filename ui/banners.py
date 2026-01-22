#!/bin/python
from rich.console import Console
from rich. panel import Panel
from rich_gradient. text import Text

console = Console()

banner_art = """\
  ██╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
  ██║██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
  ██║██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
  ██║██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
  ██║██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝"""


gradient_banner = Text(
    banner_art,
    colors=["#ff0000", "#ff4500", "#ff8c00", "#ffa500"]
)

def print_banner():
    console.print(
        Panel(
            gradient_banner,
            border_style="bright_red",
            width=54
        )
    )


