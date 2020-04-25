# file with the basic parsing and I/O functionality
import argparse
import requests
from our_parser import parse_NYT
from analyze import get_keywords


def parse_args():
    parser = argparse.ArgumentParser(description='a TL;DR news reader for the New York Times')
    parser.add_argument('-url', help='the news article url', type=str)
    parser.add_argument('-filename', help='the filename that contains the news article urls', type=str)
    args = parser.parse_args()
    return args


# returns an array of the content given a url
def get_html(url):
    page = requests.get(url)
    cover = page.content
    return [cover] 


# return an array of the content given a file of urls
def get_html_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        covers = []
        for l in lines:
            if 'http' not in l:
                l = "https://" + l.strip()
            covers.append(requests.get(l).content)
        f.close()
        return covers


if __name__ == '__main__':
    args = parse_args()
    pages = []
    if args.url:
        url = args.url
        pages = get_html(url)
    else:
        pages = get_html_from_file(args.filename)
    # array of props for all input articles
    props_arr = parse_NYT(pages)

