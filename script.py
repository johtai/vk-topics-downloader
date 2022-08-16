import requests, urllib, sys, os
from bs4 import BeautifulSoup

# get url from terminal
url = sys.argv[1]

# get the page of all topics
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# get all "a" tags, which contains urls of topics
links = soup.find_all('a')

# go through all the links
for link in links:
    # get url of topic
    url = link.get('href')

    # check this is a topic link
    if url and "@" in url:
        # get url without params
        url = url[:url.index("?")]
        https = "https://vk.com" + url

        # get a topic page
        response = urllib.request.urlopen(https)
        webContent = response.read().decode('UTF-8')
        
        # make a dir
        if not os.path.isdir("topics"):
            os.mkdir("topics")

        print(https)
        
        # create, write and open a topic
        f = open(f"topics/{url}.html", 'w', encoding="UTF-8")
        f.write(webContent)
        f.close