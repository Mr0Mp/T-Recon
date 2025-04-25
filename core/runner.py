import threading
from config import AVAILABLE_TOOLS

tool_map = {
    "nmap": nmap.run,
    "sqlmap": sqlmap.run,
    "whatweb": whatweb.run,
    "dirb": dirb.run,
    "httpx": httpx.run,
    "nuclei": nuclei.run,
    "subfinder": subfinder.run,
    "amass": amass.run,
    "ffuf": ffuf.run,
    "waybackurls": waybackurls.run,
}

def run_selected_tools(tools, target, folder):
    threads = []
    for tool in tools:
        if tool in tool_map:
            t = threading.Thread(target=tool_map[tool], args=(target, folder))
            t.start()
            threads.append(t)
    for t in threads:
        t.join()