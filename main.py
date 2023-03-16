import requests

api_key = "58bc1a1409de4ec3824701545189e709"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=" \
						"58bc1a1409de4ec3824701545189e709"

# Make request
r = requests.get(url)

# Get a dictionary with data
content = r.json()

# Access article titles and descriptions
for article in content["articles"]:
				print(article["title"])
				print(article["description"])

