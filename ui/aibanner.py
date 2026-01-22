#!/usr/bin/env python
from rich.console import Console
from rich_gradient import Gradient
from rich_gradient. text import Text

console = Console()

# Box-drawing characters
uiHoriz = "─"
uiVert = "│"
rndCornerTL = "╭"
rndCornerTR = "╮"
rndCornerBL = "╰"
rndCornerBR = "╯"

# ASCII art for "iRecon"
banner_art = """\
  ██╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
  ██║██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
  ██║██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
  ██║██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
  ██║██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝"""

# Option 1: Custom orange/red gradient (similar to your original)
fire_colors = ["#ff0000", "#ff4500", "#ff8c00", "#ffa500"]

# Option 2: Use rainbow for full spectrum
# rainbow=True

# Create gradient border
border_top = Text(
    rndCornerTL + uiHoriz * 50 + rndCornerTR,
    colors=fire_colors
)

border_bottom = Text(
    rndCornerBL + uiHoriz * 50 + rndCornerBR,
    colors=fire_colors
)

# Create gradient banner text
banner_text = Text(
    banner_art,
    colors=fire_colors  # Or use rainbow=True for rainbow effect
)

# Print the banner
console.print(border_top)
for line in banner_text.split("\n"):
    # Add side borders with gradient
    console.print(
        Text(uiVert, colors=fire_colors),
        line,
        Text("  " + uiVert, colors=fire_colors),
        sep=""
    )
console.print(border_bottom)
