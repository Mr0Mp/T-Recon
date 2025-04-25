import os
import threading
from rich.console import Console
from rich.panel import Panel
import questionary
from datetime import datetime
from core.runner import run_selected_tools  # استفاده از تابع جدید برای اجرای ابزارها

console = Console()

def scan_menu():
    # اضافه کردن تمام ابزارها به منوی انتخاب
    return questionary.checkbox(
        "📌 Select tools to run:",
        choices=[
            "nmap", "sqlmap", "whatweb", "dirb", "httpx", "nuclei", "subfinder",
            "amass", "ffuf", "waybackurls"
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

    # اجرای ابزارهای انتخابی با استفاده از multithreading
    run_selected_tools(tools, target, folder)

    console.print(Panel(f"[bold green]✅ Done! All scan results saved in [italic]{folder}[/italic][/bold green]", expand=False))

if __name__ == "__main__":
    main()