import subprocess
import shutil
from rich.console import Console

console = Console()

def run(target, folder):
    if not shutil.which("ffuf"):
        console.print("[red]ffuf not installed.[/red]")
        return
    output_file = f"{folder}/ffuf.txt"
    console.print(f"[magenta]Running ffuf on {target}...[/magenta]")
    subprocess.run(f"ffuf -w /path/to/wordlist.txt -u http://{target}/FUZZ -o {output_file}", shell=True)