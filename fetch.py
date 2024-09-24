import urllib.request
import pickle
from datetime import datetime
from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
    _tags = {}

    def handle_starttag(self, tag, attrs):
        if tag not in self._tags:
            self._tags[tag] = 0
        self._tags[tag] += 1

def metadata(urls):
    url = urls[1]
    if (len(urls) > 2):
        print("Only provide one URL to use with the --metadata tag.")

    try:
        html = fetch(url)
        parser = CustomHTMLParser()
        parser.feed(html)
        parser._tags["timestamp"] = datetime.now()
        printMetadata(url, parser._tags)
        saveMetadata(parser._tags, url)
    except:
        print("Unable to fetch metadata for: " + url)
        return
    
def printMetadata(url, metadata):
    print("site: " + url)
    print("imgs: " + str(metadata['img'] or 0))
    print("links: " + str(metadata['a'] or 0))
    print("last checked: " + str(metadata['timestamp'] or "err"))

# hacky filename split to get everything right of http(s)// ...
def urlToFilename(url):
    return url.split("//")[1]

def saveHTML(html, url):
    filename = urlToFilename(url) + ".html"
    f = open(filename, "w")
    f.write(html)
    f.close()

def saveMetadata(metadata, url):
    filename = urlToFilename(url) + ".metadata"
    f = open(filename, "wb")
    pickle.dump(metadata, f)
    f.close()

def readMetadataFile(url):
    filename = urlToFilename(url)
    f = open(filename + ".metadata", "rb")
    metadata = pickle.load(f)
    f.close()
    return metadata

def getHTML(url):
    website = urllib.request.urlopen(url)
    return website.read().decode()

def fetch(url):
    try:
        html = getHTML(url)
        saveHTML(html, url)
        return html
    except:
        print("Unable to fetch: " + url)
        return

def main():
    print("Enter the web page(s) you'd like to fetch, space separated.")
    print("You can also search metadata for a single URL by adding the '--metadata' tag before a URL.")
    print("You can quit with 'q'")

    i = input("fetch: ")

    while i != "q":
        # simple input cleanup
        i = i.strip()
        urls = i.split(" ")
        if (urls[0] == "--metadata"):
            metadata(urls)
        else:
            for url in urls:
                fetch(url)
        print("")
        i = input("fetch: ")

    print("quitting")

main()

    