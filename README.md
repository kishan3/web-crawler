# web crawler
This repository contains program to fetch urls from a url.

## setup

  Install virtualenvwrapper. (http://virtualenvwrapper.readthedocs.io/en/latest/)

  Make a virtual environment using:

      mkvirtualenv web_crawler -p /usr/bin/python3

  Install requirements:

      pip install -r requirements.txt

  Usage:

      python web_crawler.py url

## python version
    Python 3.5.2

## Asumption

    Stop the program after retrieving 100 links.

## web_crawler.py

    Explaination:
    This program runs in two ways:

    This program begins with a url given in sys args while calling the program.

    Before starting number of checks are performed such as
      - Length of sys.argv
       if 0 or more than one we exit with error.
      - Check if given input is url
      - If not proper url we parse it make it proper.
      - Program is ran which returns list of retrieved links and list of visited
        links