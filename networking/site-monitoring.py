import requests

urls = [
    "https://www.openai.com",
    "https://www.github.com",
    "https://www.python.org",
    "https://www.stackoverflow.com"
]

for url in urls:
    response = requests.get(url)
    
    if response.status_code != 200: #No error returned
        print(response.url," is currently down with error code:", response.status_code)
    else:
        print(response.url," is working.")