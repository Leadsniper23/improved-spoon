import requests
from bs4 import BeautifulSoup

# Fetch a webpage
url = "https://example.com"
response = requests.get(url)

# Parse the webpage content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract and print the title
print("Page Title:", soup.title.string)
