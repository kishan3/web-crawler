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
from urllib.parse import urlsplit

pattern = re.compile("^https?://")


def make_url_proper(url):
    """Method reformats url given and makes it appropriate.

    Then it can be be called by urllib.
    """
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
        print("Your net seems to down or site is down.Please try again.")
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

    Here we check for number of arguments if it is 0 or more than 2 then
    we raise error and exit.
    After that depending on number of arguments we call different methods.
    If arguments is 1 we call scrape_a_page() method.
    If arguments are 2 we call scrape_all_pages() method.
    """
    number_or_args = len(sys.argv[1:])
    if number_or_args > 1 or number_or_args == 0:
        print("Usage: python web_crawler.py <arg1>")
        print("Note: <arg1> is name of the url from where crawling will start.")
        sys.exit(1)
    url = sys.argv[1]
    url = make_url_proper(url)
    retrieved_links = [url]
    crawled_links = []
    for link in retrieved_links:
        if len(retrieved_links) < 100:
            html = get_html_page(link)
            links = crawl_a_page(html)
            retrieved_links.extend(links)
            crawled_links.append(link)
        else:
            print("-------------------We have crawled enough links!!----------------")
            print("-------------------Exiting program!!----------------------")
            print("====================Crawled urls=====================")
            print(crawled_links)
            print("====================Retrieved links==============================")
            print(retrieved_links)

            break

if __name__ == "__main__":
    main()
