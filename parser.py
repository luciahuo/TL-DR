from bs4 import BeautifulSoup
import re


from analyze import get_keywords
from analyze import get_topics

from visualize import visualize_wordcloud
 

def parse_NYT(pages):
    articles = []  # list of articles properties
    for p in pages:
        soup = BeautifulSoup(p, 'html.parser')
        article_props = {}

        try:
            # get the name
            a = soup.find("span", itemprop="name")
            article_props["author"] = a.get_text(strip=True)

            # get the article title
            hl = soup.find("h1", itemprop="headline")
            article_props["headline"] = hl.get_text(strip=True)

            # get the date
            date = soup.find("time", {'datetime': re.compile(r'.*')})
            article_props["date"] = date.get_text(strip=True)

            # get the body
            body_sec = soup.find("section", itemprop="articleBody")
            p = body_sec.findChildren("p", recursive=True)
            article_text = ""
            for para in p:
                article_text += para.get_text(strip=True)
                article_text += " "
            article_text = article_text.strip()  # eliminate all white space
            article_props["body"] = article_text

            # get the subtext if it exists
            summary = soup.find("p", id="article-summary")
            if summary:
                article_props["summary"] = summary.get_text(strip=True)

            articles.append(article_props)

            # get the keywords
            article_props["keywords"] = get_keywords(article_props["body"])

        except:
            print("an article has encountered parsing error")
            continue # ignore the error and continue parsing
    return articles