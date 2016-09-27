"""
This module is basic web crawler built for shoppig.com site.

Two queries can be performed using this program.
The first query is getting the  total number of results for a given keyword.
The second query is to find all results  for a given keywords on a specified
page.

"""
import sys
import re
from bs4 import BeautifulSoup
import urllib
import urllib.request
from urllib.parse import urlparse


pattern = re.compile("^https?://")


def make_url_proper(url):
    """Method reformats url given and makes it appropriate."""
    www_match = re.match(pattern, url)
    if not www_match:
        url = "http://" + url
    parsed = urlparse(url)
    return parsed.geturl()


def get_html_page(url):
    """Method simply returns html page using urllib library."""
    print("Please wait getting results from {}!!!!".format(url))
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError:
        print("Your net seems to be down or site is down.Please try again.")
        sys.exit()
    return html


def crawl_a_page(html):
    """Method returns links on html page given in input."""
    soup = BeautifulSoup(html, 'html.parser')
    a_tags = soup.findAll('a', attrs={'href': re.compile("^https?://")})
    links = []
    for a_tag in a_tags:
        links.append(a_tag.get("href"))
    return list(set(links))


def main():
    """
    Main method from where the execution starts.

    Here we ask for seed url to begin with.
    - check if it is proper url or not.
    - If not http prepand it to url.
    - call craw_a_page() method.
    """
    seed_url = input("Enter a seed page to begin with: ")
    seed_url = make_url_proper(seed_url)
    retrieved_links = [seed_url]
    crawled_links = []
    for link in retrieved_links:
        if len(retrieved_links) < 100:
            html = get_html_page(link)
            links = crawl_a_page(html)
            retrieved_links.extend(links)
            crawled_links.append(link)
        else:
            print("-------------------We have crawled enough links!!---------------")
            print("-------------------Exiting program!!----------------------")
            print("====================Crawled urls=====================")
            print(crawled_links)
            print("====================Retrieved links==============================")
            print(retrieved_links)

            break

if __name__ == "__main__":
    main()
