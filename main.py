# file with the basic parsing and I/O functionality
import argparse
import requests
from bs4 import BeautifulSoup
import pprint as pp


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='the news website url to parse', type=str)
    # args = parser.parse_args()


def get_html(url):
    page = requests.get(url)
    cover = page.content
    return cover


def parse_NYT(page):
    soup = BeautifulSoup(page, 'html.parser')
    article_props = {}

    # get the name
    a = soup.find("span", itemprop="name")
    article_props["author"] = a.get_text(strip=True)

    # get the article title
    hl = soup.find("h1", itemprop="headline")
    article_props["headline"] = hl.get_text(strip=True)

    # get the body
    body_sec = soup.find("section", itemprop="articleBody")
    p = body_sec.findChildren("p", recursive=True)
    article_text = ""
    for para in p:
        article_text += para.get_text(strip=True)
        article_text += " "
    article_text = article_text.strip() # eliminate all white space
    article_props["body"] = article_text

    # get the subtext
    summary = soup.find("p", id="article-summary")
    if summary:
        article_props["summary"] = summary.get_text(strip=True)

    return article_props


if __name__ == '__main__':
    # args = parse_args()
    page = get_html("https://www.nytimes.com/2020/04/19/books/review/stephen-king-if-it-bleeds.html?action=click&module=Editors%20Picks&pgtype=Homepage")
    props = parse_NYT(page)
