import re
import string
from typing import List

import html2text
import requests
from lxml import html
from nltk.tokenize import word_tokenize
from requests import Response


def get_response(url: str) -> Response:
    return requests.get(url)

def get_sitemap_content(url: str):
    url_with_sitemap = url + 'sitemap.xml'
    response_sitemap = requests.get(url_with_sitemap)
    if response_sitemap.status_code == 200:
        site_map_content = response_sitemap.text
        return site_map_content
    else:
        return response_sitemap.status_code

def get_robots(url: str):
    url_with_robots = url + 'robots.txt'
    response_robots = requests.get(url_with_robots)
    return response_robots

def extract_title_from_response(response: Response) -> str:
    if response.status_code == 200: #title не обязательно в статус код 200
        html_content = response.text
        title_regex = r'<title>(.*?)</title>'
        title_match = re.search(title_regex, html_content, re.IGNORECASE)
        title = title_match.group(1) if title_match else 'Title not found'
        return title
    else:
        return f'Failed to retrieve the web page. Status code: {response.status_code}'

def extract_description_from_response(response: Response) -> str:
    if response.status_code == 200:
        html_content = response.text
        description_regex = r'<meta name="description" content="(.*?)">'
        description_match = re.search(description_regex, html_content, re.IGNORECASE)
        description = description_match.group(1) if description_match else 'Description not found'
        return description
    else:
        return f'Failed Status code: {response.status_code}'

def get_text_without_tags(response: Response) -> str:
    h = html2text.HTML2Text()
    h.ignore_links = True
    text_without_tags = h.handle(html.text)
    return text_without_tags

def remove_punctuation(text: str):
    PUNCT_TO_REMOVE = string.punctuation
    return text.translate(str.maketrans(' ', ' ', PUNCT_TO_REMOVE))

def remove_urls(text: str) -> str:
    text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)
    return(text)

def get_tokens(text: str) -> List[str]:
    tokens = word_tokenize(text)
    return tokens

def check_redirect(url):
    try:
        response = requests.get(url, allow_redirects=False)
        if response.status_code >= 300 and response.status_code < 400:
            # Extract the final destination URL from the 'Location' header
            final_url = response.headers['Location']
            return True, final_url
        else:
            return False, url
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False, None
    



