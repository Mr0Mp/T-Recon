import subprocess
import shutil
from rich.console import Console

console = Console()

def run(target, folder):
    if not shutil.which("amass"):
        console.print("[red]amass not installed.[/red]")
        return
    output_file = f"{folder}/amass.txt"
    console.print(f"[blue]Running Amass on {target}...[/blue]")
    subprocess.run(f"amass enum -d {target} -o {output_file}", shell=True)