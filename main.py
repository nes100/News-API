import requests
from send_email import send_email

topic = "techcrunch"

api_key = "58bc1a1409de4ec3824701545189e709"
url = "https://newsapi.org/v2/top-headlines?" \
						f"sources={topic}&" \
						"apiKey=58bc1a1409de4ec3824701545189e709&language=en"

# Make request
r = requests.get(url)

# Get a dictionary with data
content = r.json()

body = ""
# Access article titles and descriptions
for article in content["articles"][:20]:
			body = body + article["title"] + "\n"\
										+ article["description"] + "\n"\
										+ article["url"] +  2*"\n"

message = f"""\
Subject: Today's News

{body} 
"""
message = message.encode('utf-8')
send_email(message)


