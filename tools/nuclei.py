import subprocess
import shutil
from rich.console import Console

console = Console()

def run(target, folder):
    if not shutil.which("nuclei"):
        console.print("[red]nuclei not installed.[/red]")
        return
    output_file = f"{folder}/nuclei.txt"
    console.print(f"[green]Running Nuclei on {target}...[/green]")
    subprocess.run(f"nuclei -u {target} -o {output_file}", shell=True)