import subprocess
import shutil
from rich.console import Console

console = Console()

def run(target, folder):
    if not shutil.which("httpx"):
        console.print("[red]httpx not installed.[/red]")
        return
    output_file = f"{folder}/httpx.txt"
    console.print(f"[cyan]Running httpx on {target}...[/cyan]")
    subprocess.run(f"httpx -title -status-code -tech-detect -l {target}", shell=True, stdout=open(output_file, "w"))