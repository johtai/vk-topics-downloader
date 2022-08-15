import requests, urllib, sys, os
from bs4 import BeautifulSoup


url = sys.argv[1]
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
links = soup.find_all('a')

for link in links:
    url = link.get('href')
    if url and "@" in url:
        url = "https://vk.com" + url[:url.index("?")]
        
        print(url)
        
        response = urllib.request.urlopen(url)
        webContent = response.read().decode('UTF-8')

        if os.path.isdir("topics"):
            os.mkdir("topics")
            
        f = open(f"topics/{url[url.find('@'):]}.html", 'w', encoding="UTF-8")
        f.write(webContent)
        f.close