import subprocess
import shutil
from rich.console import Console

console = Console()

def run(target, folder):
    if not shutil.which("dirb"):
        console.print("[red]dirb not installed.[/red]")
        return
    output_file = f"{folder}/dirb.txt"
    console.print(f"[green]Running Dirb on {target}...[/green]")
    subprocess.run(f"dirb http://{target}", shell=True, stdout=open(output_file, "w"))