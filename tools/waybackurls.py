import subprocess
import shutil
from rich.console import Console

console = Console()

def run(target, folder):
    if not shutil.which("waybackurls"):
        console.print("[red]waybackurls not installed.[/red]")
        return
    output_file = f"{folder}/waybackurls.txt"
    console.print(f"[purple]Running waybackurls on {target}...[/purple]")
    subprocess.run(f"waybackurls {target} > {output_file}", shell=True)