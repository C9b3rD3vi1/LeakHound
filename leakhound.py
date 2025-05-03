import requests
from urllib.parse import urljoin
import sys
import os
import time


# Common backup files and extensions and sensitive files 
common_files = [
    ".env",
    ".git/config",
    ".git/HEAD",
    ".git/objects",
    ".git/refs",
    ".gitignore",
    ".htaccess",
    ".htpasswd",
    ".idea/",
    ".svn/",
    ".DS_Store",
    "wp-config.php",
    "config.php",
    "config.inc.php",
    "config.yaml",
    "config.yml",
    "config.json",
    "settings.py",
    "settings.json",
    "settings.yml",
    "settings.ini",
    "settings.xml",
    "web.config",
    "appsettings.json",
    "appsettings.yml",
    "appsettings.xml",
    "appsettings.ini",
    "appsettings.php",
    "appsettings.config",
    "appsettings.py",
    "appsettings.properties",
    "appsettings.rb",
    "appsettings.yaml",
    "appsettings.env",
    "appsettings.env.example",
    #backup files
    "backup.zip",
    "backup.tar.gz",
    "backup.tar.bz2",
    "backup.tar.xz",
    "backup.tar",
    "backup.tgz",
    "backup.tgz.bz2",
    "backup.tgz.xz",
    "backup.tgz.z",
    # PHP sensitive files
    "php.ini",
    "phpinfo.php",
    "phpmyadmin/config.inc.php",
    "phpmyadmin/config.php",
    "phpmyadmin/config.inc.php.bak",

]

# function to check if a file exists on the server
def check_file(base_url, file):

    print(f"[+] Scanning ...")

    print(f"[-] Checking {file}...")

    # Construct the full URL
    if not base_url.endswith('/'):
        base_url += '/'

    for file in common_files:
        full_url = urljoin(base_url, file)
        print(f"[-] Checking {full_url}...")
        # Check if the file exists
        try:
            # Send a HEAD request to check if the file exists
            response = requests.head(full_url, allow_redirects=True, timeout=5)
            if response.status_code == 200:
                print(f"[+] Found: {full_url}")
                # forbidden files
            elif response.status_code == 403:
                print(f"[+] Found: {full_url} (403 Forbidden)")
                # not found files
            elif response.status_code == 404:
                print(f"[-] Not Found: {full_url} (404 Not Found)")

        except Exception as e:
            print(f"[-] Error checking {full_url}: {e}")
            continue
    print(f"[+] Finished scanning {base_url} for common files.")




# Main function to run the script
def main():
    if len(sys.argv) < 2:
        print("Usage: python leakhound.py <url>")
        sys.exit(1)

    base_url = sys.argv[1]

    # Check if the URL starts with http:// or https://
    if not base_url.startswith("http://") and not base_url.startswith("https://"):
        print("[-] Invalid URL. Please provide a valid URL starting with http:// or https://")
        sys.exit(1)

    # Call the check_file function
    check_file(base_url, common_files)
    