# 🐾 LeakHound

**LeakHound** is a lightweight Python-based reconnaissance tool that scans web servers for **sensitive or misconfigured files** such as backup configs, credential files, database dumps, and more. It’s useful for **pentesters**, **bug bounty hunters**, and **security researchers**.


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
