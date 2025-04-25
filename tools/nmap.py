# tools/nmap.py

import subprocess
import shutil
from rich.console import Console

console = Console()

def run(target, folder):
    if not shutil.which("nmap"):
        console.print("[red]Nmap not installed.[/red]")
        return
    output_file = f"{folder}/nmap.txt"
    console.print(f"[blue]Running Nmap on {target}...[/blue]")
    subprocess.run(f"nmap -sT -Pn {target}", shell=True, stdout=open(output_file, "w"))