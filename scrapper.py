import os
from trafilatura import sitemaps, fetch_url, extract
import re
from dotenv import load_dotenv

load_dotenv()

def get_pagename_from_url(url):
    pagename = url.rsplit('/', 1)[-1]
    cleaned_pagename = re.sub("[^A-Z]", "", pagename, 0, re.IGNORECASE)
    return cleaned_pagename[:100] if len(cleaned_pagename) > 100 else cleaned_pagename

def get_urls_from_sitemap(sitemap_url: str) -> str:
    return sitemaps.sitemap_search(sitemap_url, target_lang='en')

def load_sitemap_to_dirfiles(dir: str, sitemap_url: str) -> None:
    urls = get_urls_from_sitemap(sitemap_url)
    for url in urls:
        page_name = get_pagename_from_url(url)
        downloaded = fetch_url(url)
        if downloaded:
            result = extract(downloaded, include_comments=False, include_tables=True, no_fallback=True)
            with open(f'{dir}/{page_name}.txt', 'w', encoding="utf-8") as f:
                f.write(result)

if __name__ == "__main__":
    sitemap_url = "https://knowledge.exlibrisgroup.com/Alma"
    output_dir = "alma_docs"
    os.makedirs(output_dir, exist_ok=True)
    load_sitemap_to_dirfiles(output_dir, sitemap_url)
    print(f"Alma documentation scraped and saved to {output_dir}")
