# 🐾 LeakHound

**LeakHound** is a lightweight Python-based reconnaissance tool that scans web servers for **sensitive or misconfigured files** such as backup configs, credential files, database dumps, and more. It’s useful for **pentesters**, **bug bounty hunters**, and **security researchers**.

![LeakHound](./leakhound.png)

## 🚀 Features

- 🔍 Scans for over 100+ common sensitive file paths
- 🎨 Colored output using `colorama`
- 🌐 Supports HTTP/HTTPS
- ⏱ Graceful handling of errors and user interruptions
- 💤 Throttled requests to avoid overwhelming the server

## 🛠️ Installation

### 📦 Requirements

- Python 3.6+
- `requests` and `colorama` libraries

Install dependencies:

    pip install -r requirements.txt

Or install manually:

    pip install requests colorama

⚙️ Usage

    python3 leakhound.py <URL>

Example:

    python3 leakhound.py https://example.com

LeakHound will then scan the provided domain for known sensitive files and backups.

📂 Files Detected

LeakHound checks for:

        wp-config.php, config.json, db.yaml, etc.

        .git/HEAD, .env, credentials.txt

        admin.php.bak, passwd.old, and many more

The list is customizable via the common_files array.

🧠 Example Output

    [+] Scanning ...
    [-] Scanning https://example.com for common files...
    [-] Checking https://example.com/wp-config.php...
    [+] Found: https://example.com/wp-config.php (200 OK) Exist
    [-] Not Found: https://example.com/db.json (404 Not Found)


🧩 To Do

    Proxy support

    Random User-Agent rotation

    Save results to file


⚠️ Legal Disclaimer
This tool is intended for educational purposes and authorized testing only. Unauthorized scanning of systems you do not own or have permission to test is illegal and unethical.


📃 License
MIT License

🙋‍♂️ Author
LeakHound by C9b3rD3vi1

Feel free to contribute or suggest improvements!