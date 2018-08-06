from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

url = 'http://casesearch.courts.state.md.us/casesearch/'

# HTTP POST data
post_fields = {
    'disclaimer': 'Y', 
    'action': 'Continue'
    }

# Save HTML to file function
def save_html(name, source_str):
    # optional relative to global link function call
    source_str = fix_links(source_str)
    # write html source to file
    with open(name, "w") as f:
        f.write(source_str)

# OPTIONAL relative to global Link function
def fix_links(source_str):
    from bs4 import BeautifulSoup
    import re

    # select relative links
    soup = BeautifulSoup(source_str, 'html.parser')
    src_links = [x['src'] for x in soup.find_all(src=True)]
    href_links = [x['href'] for x in soup.find_all(href=True)]

    # replace links starting with ...
    for link in set(src_links + href_links):
        if link.startswith('images') or link.startswith('css'):
            source_str = source_str.replace(link, url + link)

    return source_str

# Connect to URL and get source code
try:
    html_source = urlopen(Request(url)).read().decode('utf-8')
except (HTTPError, URLError) as e:
    print("Error:", str(e))


# save first page html source to file
save_html('a5-1.html', html_source)

# send HTTP POST with form data
try:
    request = Request(url + 'processDisclaimer.jis', urlencode(post_fields).encode())
    html_interior_page = urlopen(request).read().decode('utf-8')
except (HTTPError, URLError) as e:
    print(str(e))

# save second page html source to file
save_html('a5-2.html', html_interior_page)
