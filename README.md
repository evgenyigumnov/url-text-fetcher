# url-text-fetcher

##  URL Text Fetcher Tools

This MCP server provides two utilities for web content analysis. 

## How to install
```bash
pip install -e .
```
## How to use with LM Studio
`mcp.json` file:
```json
{
  "mcpServers": {
    "url-text-fetcher": {
      "command": "python",
      "args": [
        "-m",
        "url_text_fetcher.mcp_server"
      ]
    }
  }
}
```

## Tools Description

### 1. `fetch_url_text(url: str) → str`

**Description:**  
Extracts all visible text content from a webpage, stripping HTML tags and normalizing whitespace.


**Output Format:**  
Cleaned plain text with:
- All HTML removed
- Line breaks normalized (`\n`)
- Leading/trailing whitespace stripped

---

### 2. `fetch_page_links(url: str) → List[str]`

**Description:**  
Finds all absolute and relative links (from `<a href>` tags) on a webpage.


**Output Format:**  
List of URLs including:
- Absolute paths (`/about`)
- Relative paths (`../contact`)
- Full domain URLs (`https://example.com/page`)

