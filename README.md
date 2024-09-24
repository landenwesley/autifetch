## Autify Fetch

#### Compile and Run:
CD to the repo,
```commandline
docker build -t fetch .
docker run -i -t fetch
```

#### Example Usage:
While the container is running, you can check a URL's fetched file in `/home/usr/*.html`.

If getting metadata, there will also be a `/home/usr/*.metadata` file.
```commandline
Enter the web page(s) you'd like to fetch, space separated.
You can also search metadata for a single URL by adding the '--metadata' tag before a URL.
You can quit with 'q'
fetch: https://google.com

fetch: --metadata https://autify.com
site: https://autify.com
imgs: 15
links: 29
last checked: 2024-09-24 03:11:01.817265

fetch: https://autify.com https://google.com asdf
Unable to fetch: asdf

fetch: q
quitting
```

#### Notes
* There is an unused readMetadataFile method.
* Writing the CustomHTMLParser was the part of this that felt most foreign to me initially. In the end the built in python HTMLParser made this quite easy and clean.

#### Future Improvements
* Better handling of errors. Displaying to the user if it is due to 403, or some issue with writing the file, would be ideal.
* Adding unit tests would also be ideal if I had additional time. Fortunately most of the code is split into functions that would make that easy.
