import requests
from send_email import send_email


api_key = "58bc1a1409de4ec3824701545189e709"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=" \
						"58bc1a1409de4ec3824701545189e709"

# Make request
r = requests.get(url)

# Get a dictionary with data
content = r.json()

body = ""
# Access article titles and descriptions
for article in content["articles"]:
			body = body + article["title"] + "\n" + article["description"] + 2*"\n"

message = f"""\
Subject: News

{body} 
"""
message = message.encode('utf-8')
send_email(message)


