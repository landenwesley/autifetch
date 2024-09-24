## Autify Fetch

#### Compile and Run:
CD to the repo,
```commandline
docker build -t fetch .
docker run -i -t fetch
```

#### Example Usage:
```commandline
Enter the web page(s) you'd like to fetch, space separated.
You can also search metadata for a single URL by adding the '--metadata' tag before a URL.
You can quit with 'q'
fetch: https://google.com
fetch: --metadata https://autify.com
metadata for https://autify.com
site: https://autify.com
imgs: 15
links: 29
last checked: 2024-09-24 03:11:01.817265
fetch: https://autify.com https://google.com asdf
Unable to fetch: asdf
fetch: q
quitting
```
