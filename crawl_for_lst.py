from bs4 import BeautifulSoup as bs
import urllib2
import sys


def main():
    url = raw_input("Please enter a url: ")
    response = urllib2.urlopen(url)
    page_src = response.read()
    soup = bs(page_src)
    lst_of_locations = soup.findAll('strong')





if __name__ == '__main__':
    sys.exit(main())
