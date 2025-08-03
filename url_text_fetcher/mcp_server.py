# url_text_fetcher/mcp_server.py
from mcp.server.fastmcp import FastMCP
import requests
from bs4 import BeautifulSoup
from typing import List  # for type hints

mcp = FastMCP("URL Text Fetcher")

@mcp.tool()
def fetch_url_text(url: str) -> str:
    """Download the text from a URL."""
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    return soup.get_text(separator="\n", strip=True)

@mcp.tool()
def fetch_page_links(url: str) -> List[str]:
    """Return a list of all URLs found on the given page."""
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    # Extract all href attributes from <a> tags
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

def main():
    mcp.run()

if __name__ == "__main__":
    main()