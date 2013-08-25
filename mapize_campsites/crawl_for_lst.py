from bs4 import BeautifulSoup as bs
import urllib2
import sys
import re


def format_lst_of_locations(lst_of_locations):
    formatted_lst = []
    for i in range(2):                
        lst_of_locations.pop(0)
    for elem in lst_of_locations:
        elem_str_split = re.split('[0-9_]+. ',elem.string)
        formatted_lst.append(elem_str_split[1])
    return formatted_lst


def get_lst_of_locations(url_to_crawl):
    response = urllib2.urlopen(url_to_crawl)
    page_src = response.read()
    soup = bs(page_src)
    lst_of_locations = soup.findAll('strong')
    formatted_lst_of_locations = format_lst_of_locations(lst_of_locations)
    return formatted_lst_of_locations

def main():
    url_to_crawl = raw_input("Please enter a url: ")
    lst_of_locations = get_lst_of_locations(url_to_crawl)
    print lst_of_locations


if __name__ == '__main__':
    sys.exit(main())
