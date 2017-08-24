"""
Implementation of a simple web crawler for Python Web Data, Coursera
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

start_url = 'http://py4e-data.dr-chuck.net/known_by_Alessandro.html'

def find_selected(url, n, pos):
    """Finds the content of a link recursively
    Args:
        url: url to follow
        n: counter
        pos: position of the link
    Return:
        None
    """
    n += 1
    html = urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    # 7 is the number of recursions to make
    if n>7:
        return
    print(tags[pos].contents)
    url = tags[pos].get('href', None)
    find_selected(url, n, pos)

find_selected(start_url,0,17)
find_selected(start_url,0,4)
