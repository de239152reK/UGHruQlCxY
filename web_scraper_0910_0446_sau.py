# 代码生成时间: 2025-09-10 04:46:15
import requests
from bs4 import BeautifulSoup
import numpy as np

"""
A simple web scraper tool using Python and NumPy.
This tool fetches content from a webpage and extracts text data.
"""

def fetch_webpage(url):
    """Fetches the content of a webpage given a URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return None

def parse_content(html_content):
    """Parses HTML content using BeautifulSoup and extracts text."""
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.get_text()
    except Exception as e:
        print(f"Error parsing content: {e}")
        return None

def main():
    # Define the target URL
    target_url = "http://example.com"

    # Fetch the webpage content
    html_content = fetch_webpage(target_url)
    if html_content is not None:
        # Parse the content and extract text
        text_data = parse_content(html_content)
        if text_data is not None:
            print("Extracted Text Data: ")
            print(text_data)
        else:
            print("Failed to extract text data.")
    else:
        print("Failed to fetch webpage content.")

if __name__ == "__main__":
    main()