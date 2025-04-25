# config.py

# تنظیمات عمومی پروژه
TARGET_URL = None  # می‌تونید یک URL پیش‌فرض هم اینجا بذارید
OUTPUT_FOLDER = "scan_results"  # مسیر پیش‌فرض ذخیره نتایج اسکن

# ابزارهای پیش‌فرض که می‌خواهید همیشه اجرا بشه
DEFAULT_TOOLS = [
    "nmap", "sqlmap", "whatweb", "dirb", "httpx", "nuclei"
]

# لیست ابزارها برای نمایش در منو
AVAILABLE_TOOLS = [
    "nmap", "sqlmap", "whatweb", "dirb", "httpx", "nuclei", "subfinder",
    "amass", "ffuf", "waybackurls"
]

# تنظیمات متغیرها و پیکربندی‌های اضافی (مثل مسیرهای wordlistها یا URLها)
WORDLIST_PATH = "/path/to/wordlist.txt"  # برای ابزارهایی مثل ffuf