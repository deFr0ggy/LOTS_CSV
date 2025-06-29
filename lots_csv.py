import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

def banner():
    banner = """
    ############### ############## ##############
    #             # #            # #            #
    #             # #            # #            #
    #                   LOTS_CSV                #
    #             # #            # #            #
    #             # #            # #            #
    ############### ############## ##############
    =========================================
    LOTS_CSV - LOTS Project CSV Extractor
    =========================================   
    Extracts domains and links from the LOTS project website.
    Written by Kamran Saifullah - @deFr0ggy
    https://linkedin.com/in/kamransaifullah
    https://github.com/deFr0ggy
    https://x.com/deFr0ggy

    Usage: python lots_csv.py
    Requirements: requests, beautifulsoup4, lxml
    License: MIT License
    """

    print(banner)

base_url = "https://lots-project.com/"

response = requests.get(base_url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

entries = []
cleaned_urls = []

for a_tag in soup.find_all('a', class_='link', href=True):
    domain_name = a_tag.text.strip()
    relative_link = a_tag['href']
    full_url = urljoin(base_url, relative_link)

    entries.append((domain_name, full_url))

    if domain_name.startswith('*.'):
        domain_name = domain_name[2:]
    cleaned_https_url = f"https://{domain_name}"
    cleaned_urls.append([cleaned_https_url])  

with open('domains_links.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Domain', 'Full URL'])
    writer.writerows(entries)

with open('https_domains_cleaned.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(cleaned_urls)

banner()
print("✅ Saved full domain list to domains_links.csv")
print("✅ Saved cleaned HTTPS URLs to https_domains_cleaned.csv")