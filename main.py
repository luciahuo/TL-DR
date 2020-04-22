# file with the basic parsing and I/O functionality
import argparse
import requests
from parser import parse_NYT
from analyze import get_keywords

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='the news website url to parse', type=str)
    args = parser.parse_args()
    return args

def get_html(url):
    page = requests.get(url)
    cover = page.content
    return cover

if __name__ == '__main__':
    # args = parse_args()
    page = get_html("https://www.nytimes.com/2020/04/21/nyregion/coronavirus-jews-hasidic-ny.html?action=click&module=News&pgtype=Homepage")
    props = parse_NYT(page)
    print(get_keywords(props['body']))
