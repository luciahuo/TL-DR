from bs4 import BeautifulSoup


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