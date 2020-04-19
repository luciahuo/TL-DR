# file with the basic parsing and I/O functionality
import argparse
import requests
from parser import parse_NYT

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='the news website url to parse', type=str)
    parser.add_argument('news_name', choices=['NYT', 'New Yorker'], help='name of the paper')
    args = parser.parse_args()
    return args


def get_html(url):
    page = requests.get(url)
    cover = page.content
    return cover


if __name__ == '__main__':
    # args = parse_args()
    page = get_html("https://www.nytimes.com/2020/04/19/books/review/stephen-king-if-it-bleeds.html?action=click&module=Editors%20Picks&pgtype=Homepage")
    props = parse_NYT(page)
