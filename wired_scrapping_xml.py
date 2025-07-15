#!/usr/bin/env python3
from bs4 import BeautifulSoup
from datetime import date
import json
import time
import requests

BASE_URL = 'https://www.wired.com'
SITEMAP_URL = f'https://www.wired.com/sitemap.xml'
DATE_LIMIT = date(year=2022, month=1, day=1)
COUNT = 0
all_data = []

def get_xml_file(url=SITEMAP_URL, COUNT=COUNT):
    response = None
    try:
        response = requests.get(url).text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    
    COUNT += 1
    while not response:
        time.sleep(2)
        try:
            response = requests.get(url).text
        except Exception as e:
            print(f"Retry error for {url}: {e}")
    
    soup = BeautifulSoup(response, features='xml')
    return soup

def process_xml(soup, all_data):
    sitemaps = soup.find_all('sitemap')
    
    if not sitemaps:
        # Process individual URLs
        urls = soup.find_all('url')
        for url in urls:
            article = {}  # Create new dict for each article
            
            lastmod = url.find('lastmod')
            if lastmod:
                year, month, day = lastmod.text.split('T')[0].split('-')
                date_of_publish = date(year=int(year), month=int(month), day=int(day))
                
                if date_of_publish >= DATE_LIMIT:
                    article['URL'] = url.find('loc').text
                    article['index'] = len(all_data) + 1
                    words = url.find('loc').text.split('/')[-2].split('-')
                    article['title'] = " ".join(words)
                    article['date_of_publish'] = lastmod.text.split('T')[0]
                    all_data.append(article)
                    print(f'{len(all_data)}. {article["title"]} - {article["date_of_publish"]}')
    else:
        # Process sitemaps recursively
        for sitemap in sitemaps:
            lastmod = sitemap.find('lastmod')
            if lastmod:
                # Fix: properly parse ISO date format
                year, month, day = lastmod.text.split('T')[0].split('-')
                recent_date = date(year=int(year), month=int(month), day=int(day))
                
                if recent_date >= DATE_LIMIT:
                    link = sitemap.find('loc').text
                    soup = get_xml_file(link)
                    process_xml(soup, all_data)

def main():
    soup = get_xml_file()
    process_xml(soup, all_data)
    
    print(f"\nTotal articles found: {len(all_data)}")
    
    with open(f'wired_data.json', "w") as f:
        json.dump(all_data, f, indent=2)

if __name__ == '__main__':
    main()