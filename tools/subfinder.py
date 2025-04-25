import subprocess
import shutil
from rich.console import Console

console = Console()

def run(target, folder):
    if not shutil.which("subfinder"):
        console.print("[red]subfinder not installed.[/red]")
        return
    output_file = f"{folder}/subfinder.txt"
    console.print(f"[yellow]Running Subfinder on {target}...[/yellow]")
    subprocess.run(f"subfinder -d {target} -o {output_file}", shell=True)