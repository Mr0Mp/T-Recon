# 🦖 T-Recon - Terminal Reconnaissance Toolkit

T-Recon is a fast, modular, and highly extensible terminal-based reconnaissance automation toolkit for ethical hackers, bug bounty hunters, and CTF players.

Built specifically for Termux, but also includes a powerful Linux version, T-Recon wraps popular security tools into a sleek and interactive Python interface for smooth recon sessions.

---

## ✨ Features

- Terminal-based interactive UI using rich and questionary
- Multi-threaded execution for faster scans
- Output neatly organized per tool and session
- Both Termux and Linux versions included
- Easy to extend — just add your tool to the config!

---

## ⚙️ Tools Integrated (Termux Version)

| Tool        | Purpose                          |
|-------------|----------------------------------|
| Nmap        | Port scanning                    |
| WhatWeb     | Web technology fingerprinting    |
| Dirb        | Directory brute-forcing          |
| sqlmap      | SQL injection automation         |
| wpscan      | WordPress vulnerability scanner  |
| httpx       | Web server probing               |
| subfinder   | Subdomain discovery              |
| amass       | Passive and active subdomain enum|
| ffuf        | Fast web fuzzer                  |
| nuclei      | Templated vulnerability scanner  |

> *Note: Make sure these tools are installed in your Termux before use.*

---

## 📥 Installation (on Termux)

### Step 1: Install required packages
pkg update && pkg upgrade -y
pkg install python git curl wget nmap -y
pkg install golang -y

Step 2: Clone the repository

git clone https://github.com/Mr0Mp/T-Recon.git
cd T-Recon

Step 3: Install Python dependencies

pip install -r requirements.txt

Step 4: Install Go-based tools

go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/ffuf/ffuf@latest

Step 5: (Optional) Add Go bin to your path

echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc && source ~/.bashrc


---

▶️ Usage

python main.py

You will be prompted to:

Enter a target domain/IP

Select tools you want to run

Sit back and let T-Recon do the magic


All outputs will be saved in a session folder.


---

🗂️ Sample Output Structure

scan_results_example.com_2025-04-25_15-00/
├── nmap.txt
├── whatweb.txt
├── dirb.txt
├── sqlmap.txt
├── subfinder.txt
├── httpx.txt
├── nuclei.txt
└── ...


---

🐧 Linux Version Support

T-Recon includes support for tools more commonly found on Linux distros like Kali:

You can run the original Linux-compatible script like this:

cd linux
python3 Mr0Mp-recorn.py

> This script requires tools typically found on Kali Linux or Parrot OS, and may need root access for some modules.




---

🚀 Extend T-Recon

Want to add your own tools?

Just update config.py and define new logic inside tools/. The modular design makes adding tools super easy!


---

📜 ASCII Art

Here's a simple ASCII representation of the tool. You can replace this with your own:

               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
   
Mr0Mp

Feel free to enhance this section later with more complex ASCII art!


---

☕ Contributing

Suggestions? Found a bug? Want to collaborate?

Open an issue or PR — we'd love to have your help making T-Recon even stronger!


---

⚠️ Disclaimer

This tool is intended for educational and authorized penetration testing purposes only. Do not use it on targets you don’t have permission to scan.


---

Created with passion by Mr0Mp

---

### 2. **Install Script (install.sh)**

bash
#!/bin/bash

# Update and upgrade packages
echo "Updating Termux and installing dependencies..."
pkg update && pkg upgrade -y
# Install Python and other necessary tools
echo "Installing Python, Git, and curl..."
pkg install python git curl wget nmap -y

# Install Go for Go-based tools (httpx, subfinder, etc.)
echo "Installing Go..."
pkg install golang -y

# Install required Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Install Go-based tools
echo "Installing Go-based tools..."
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/ffuf/ffuf@latest

# Add Go binary to PATH (optional)
echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc
source ~/.bashrc

# Success message
echo "All tools and dependencies installed successfully! You can now run T-Recon using 'python main.py'."

3. FOLDER STRUCTURE

Make sure your project folder looks something like this:

T-Recon/
├── main.py
├── config.py
├── tools/
├── requirements.txt
├── install.sh
└── README.md

4. requirements.txt

rich
questionary
requests


---
