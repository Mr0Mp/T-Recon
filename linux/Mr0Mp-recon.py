# Evan:
import os
import subprocess
from datetime import datetime
import questionary
from rich.console import Console
from rich.panel import Panel
import threading

console = Console()

def run_command(command, output_file):
    with open(output_file, 'w') as f:
        process = subprocess.Popen(command, shell=True, stdout=f, stderr=subprocess.DEVNULL)
        process.communicate()

def run_tool(tool, target, folder):
    if tool == "Nmap":
        console.print("[blue][+] Running Nmap...[/blue]")
        run_command(f"nmap -sV -Pn -T4 {target}", f"{folder}/nmap.txt")
    elif tool == "WhatWeb":
        console.print("[cyan][+] Running WhatWeb...[/cyan]")
        run_command(f"whatweb {target}", f"{folder}/whatweb.txt")
    elif tool == "Nikto":
        console.print("[magenta][+] Running Nikto...[/magenta]")
        run_command(f"nikto -host http://{target}", f"{folder}/nikto.txt")
    elif tool == "Dirb":
        console.print("[green][+] Running Dirb...[/green]")
        run_command(f"dirb http://{target}", f"{folder}/dirb.txt")
    elif tool == "wpscan":
        console.print("[yellow][+] Running WPScan...[/yellow]")
        run_command(f"wpscan --url http://{target} --enumerate u", f"{folder}/wpscan.txt")
    elif tool == "sqlmap":
        console.print("[red][+] Running sqlmap...[/red]")
        run_command(f"sqlmap -u http://{target} --batch --risk=3 --level=5", f"{folder}/sqlmap.txt")
    elif tool == "Hydra":
        console.print("[purple][+] Running Hydra (Brute Force)...[/purple]")
        run_command(f"hydra -L user.txt -P pass.txt {target} http-get", f"{folder}/hydra.txt")
    elif tool == "Metasploit":
        console.print("[yellow][+] Running Metasploit...[/yellow]")
        run_command(f"msfconsole -q -x 'use auxiliary/scanner/http/http_version; set RHOSTS {target}; run'", f"{folder}/metasploit.txt")
    elif tool == "Burp Suite":
        console.print("[green][+] Running Burp Suite...[/green]")
        run_command(f"burpsuite", f"{folder}/burp.txt")
    elif tool == "OWASP ZAP":
        console.print("[cyan][+] Running OWASP ZAP...[/cyan]")
        run_command(f"zap-cli quick-scan --url http://{target}", f"{folder}/zap.txt")
    elif tool == "Fimap":
        console.print("[magenta][+] Running Fimap (LFI/RFI)...[/magenta]")
        run_command(f"fimap -u http://{target}/vulnerable_page.php?page=../../../../etc/passwd", f"{folder}/fimap.txt")
    elif tool == "Arachni":
        console.print("[blue][+] Running Arachni...[/blue]")
        run_command(f"arachni http://{target}", f"{folder}/arachni.txt")
    elif tool == "Enum4linux":
        console.print("[purple][+] Running Enum4linux...[/purple]")
        run_command(f"enum4linux -a {target}", f"{folder}/enum4linux.txt")
    elif tool == "Nessus":
        console.print("[green][+] Running Nessus...[/green]")
        run_command(f"nessus -T html -o {folder}/nessus_report.html", f"{folder}/nessus.txt")

def scan_menu():
    return questionary.checkbox(
        "📌 Select tools to run:",
        choices=[
            "Nmap", "WhatWeb", "Nikto", "Dirb", "wpscan", "sqlmap", "Hydra",
            "Metasploit", "Burp Suite", "OWASP ZAP", "Fimap", "Arachni", "Enum4linux", "Nessus"
        ]).ask()

def main():
    console.print(Panel("[bold red]💥 Kali Web Recon Automation Tool[/bold red]\nby Python + Rich + Questionary", expand=False))
    
    target = questionary.text("🔍 Enter target domain or IP:").ask().strip()
    tools = scan_menu()

    if not tools:
        console.print("[bold yellow]⚠️ No tools selected. Exiting...[/bold yellow]")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    clean_target = target.replace("http://", "").replace("https://", "").replace("/", "_")
    folder = f"scan_results_{clean_target}_{timestamp}"
    os.makedirs(folder, exist_ok=True)

    threads = []
    for tool in tools:
        thread = threading.Thread(target=run_tool, args=(tool, target, folder))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    console.print(Panel(f"[bold green]✅ Done! All scan results saved in [italic]{folder}[/italic][/bold green]", expand=False))

if __name__ == "__main__":
    main()