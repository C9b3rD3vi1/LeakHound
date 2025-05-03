import sys
import time
import requests
from urllib.parse import urljoin
from colorama import Fore, Style
from colorama import init
from concurrent.futures import ThreadPoolExecutor, as_completed


init(autoreset=True)
# LeakHound - File Leak Finder


# Common backup files and extensions and sensitive files 
common_files = [
    "config.php", "config.inc.php", "config.json", "config.yaml", "config.yml","wp-db.php", "wp-config.php",
    "wp-config.inc.php", "wp-config.json", "wp-config.yaml", "wp-config.yml", "wp-settings.php",
    "wp-settings.inc.php", "wp-settings.json", "wp-settings.yaml", "wp-settings.yml", "wp-config-sample.php",
    "wp-config-sample.inc.php", "wp-config-sample.json", "wp-config-sample.yaml", "wp-config-sample.yml",
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

# banner
def banner():
    print(f"""{Fore.CYAN}
  __          __        _    _                 _ 
  \ \        / /       | |  | |               | |
   \ \  /\  / /__  _ __| | _| | ___   ___ __ _| |
    \ \/  \/ / _ \| '__| |/ / |/ _ \ / __/ _` | |
     \  /\  / (_) | |  |   <| | (_) | (_| (_| | |
      \/  \/ \___/|_|  |_|\_\_|\___/ \___\__,_|_|
                       LeakHound - File Leak Finder
                     Author: C9b3rD3vi1
    {Style.RESET_ALL}""")


# function to check if a file exists on the server
def check_file(base_url, file):
    full_url = urljoin(base_url, file)
    try:
        response = requests.head(full_url, allow_redirects=True, timeout=5)

        if response.status_code == 200:
            return f"{Fore.GREEN}[+] Found: {full_url} (200 OK) Exist {Style.RESET_ALL}"
        elif response.status_code == 403:
            return f"{Fore.YELLOW}[+] Found: {full_url} (403 Forbidden){Style.RESET_ALL}"
        elif response.status_code == 404:
            return f"{Fore.LIGHTRED_EX}[-] Not Found: {full_url} (404 Not Found){Style.RESET_ALL}"
        else:
            return f"[?] {full_url} returned status code {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"[-] Error checking {full_url}: {e}"
    


# function to check if a file exists on the server
def scan_target(base_url, max_threads=10):
    print(f"{Fore.BLUE}[+] Scanning {base_url} with {max_threads} threads...{Style.RESET_ALL}")

    if not base_url.endswith('/'):
        base_url += '/'

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        future_to_file = {executor.submit(check_file, base_url, file): file for file in common_files}

        for future in as_completed(future_to_file):
            result = future.result()
            print(result)

    print(f"\n{Fore.GREEN}[+] Scan complete.{Style.RESET_ALL}")


# Main function to run the script
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 leakhound.py <url>")
        sys.exit(1)

    base_url = sys.argv[1]

    # Check if the URL starts with http:// or https://
    if not base_url.startswith("http://") and not base_url.startswith("https://"):
        print(f"{Fore.RED}[-] Invalid URL. Please provide a valid URL starting with http:// or https://{Style.RESET_ALL}")

        sys.exit(1)

    try:
        scan_target(base_url)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Scan interrupted by user. Exiting...{Style.RESET_ALL}")
        sys.exit(1)

  
if __name__ == "__main__":
    banner()
    main()