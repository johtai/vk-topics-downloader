import requests, urllib, sys, os
from bs4 import BeautifulSoup


url = sys.argv[1]
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
links = soup.find_all('a')

for link in links:
    url = link.get('href')
    if url and "@" in url:

        url = url[:url.index("?")]
        https = "https://vk.com" + url
        response = urllib.request.urlopen(https)
        webContent = response.read().decode('UTF-8')

        if not os.path.isdir("topics"):
            os.mkdir("topics")

        print(https)
        
        f = open(f"topics/{url}.html", 'w', encoding="UTF-8")
        f.write(webContent)
        f.close