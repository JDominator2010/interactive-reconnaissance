#!/usr/bin/env python
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

# Create a gradient text banner with fire colors
gradient_banner = Text(
    banner_art,
    colors=["#ff0000", "#ff4500", "#ff8c00", "#ffa500"]  # Fire gradient
)

# Or use rainbow mode: 
# gradient_banner = Text(banner_art, rainbow=True)

console.print(
    Panel(
        gradient_banner,
        border_style="bright_red",
        width=54
    )
)
