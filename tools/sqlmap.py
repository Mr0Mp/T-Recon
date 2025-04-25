import subprocess
import shutil
from rich.console import Console

console = Console()

def run(target, folder):
    if not shutil.which("sqlmap"):
        console.print("[red]sqlmap not installed.[/red]")
        return
    output_file = f"{folder}/sqlmap.txt"
    console.print(f"[red]Running sqlmap on {target}...[/red]")
    subprocess.run(f"sqlmap -u http://{target} --batch", shell=True, stdout=open(output_file, "w"))