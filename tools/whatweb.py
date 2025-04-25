import subprocess
import shutil
from rich.console import Console

console = Console()

def run(target, folder):
    if not shutil.which("whatweb"):
        console.print("[red]whatweb not installed.[/red]")
        return
    output_file = f"{folder}/whatweb.txt"
    console.print(f"[cyan]Running WhatWeb on {target}...[/cyan]")
    subprocess.run(f"whatweb http://{target}", shell=True, stdout=open(output_file, "w"))