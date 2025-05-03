import requests
from urllib.parse import urljoin
import sys
import os
import time


# Common backup files and extensions and sensitive files 
common_files = [
    "config.php", "config.inc.php", "config.json", "config.yaml", "config.yml",
    "config.xml", "wp-config.php", "web.config", "db.php", "db.inc.php",
    "db.json", "db.yaml", "db.yml", "db.xml", "settings.php", "settings.inc.php", "admin.bak", "admin.old",
    "admin.php.bak", "admin.php.old", "admin.php~", "admin.php.save", "admin.php.swp",
    "admin.php.save~", "admin.php.swp~", "admin.php.save1", "admin.php.save2", "admin.php.save3",
    "admin.php.save4", "admin.php.save5", "admin.php.save6", "admin.php.save7", "admin.php.save8",
    "admin.php.save9", "admin.php.save10", "admin.php.save11", "admin.php.save12", "admin.php.save13", "git/config", ".git/HEAD", "credentials.json",
    "credentials.yaml", "credentials.yml", "credentials.xml", "credentials.php", "credentials.inc.php",
    "credentials.txt", "credentials.bak", "credentials.old", "credentials.php.bak", "credentials.php.old",
    "credentials.php~", "credentials.php.save", "credentials.php.swp", "credentials.php.save~",
    "credentials.php.swp~", "credentials.php.save1", "credentials.php.save2", "credentials.php.save3","passwd", "passwd.bak", "passwd.old", "passwd.php", "passwd.inc.php",
    "passwd.json", "passwd.yaml", "passwd.yml", "passwd.xml", "passwd.txt", "passwd.bak", "passwd.old",
    "passwd.php.bak", "passwd.php.old", "passwd.php~", "passwd.php.save", "passwd.php.swp",
    "passwd.php.save~", "passwd.php.swp~", "passwd.php.save1", "passwd.php.save2", "passwd.php.save3",

]



# function to check if a file exists on the server
def scan_target(base_url, file):

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
    scan_target(base_url, common_files)
    