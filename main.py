# file with the basic parsing and I/O functionality
import argparse
import requests
from our_parser import parse_NYT
from analyze import get_keywords
import sentiment
import translator

# visualizer stuff
# will need to 'pip3 install matplotlib'
import matplotlib.pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser(description='a TL;DR news reader for the New York Times')
    parser.add_argument('-url', help='the news article url', type=str)
    parser.add_argument('-filename', help='the filename that contains the news article urls', type=str)
    parser.add_argument('-language', help='language to translate to (Spanish, German, French, Chinese, Japanese, etc)', type=str)
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

    # sentiment data
    mainSentimentData = []
    sentencesSentiment = []
    # translation data
    translations = []
    # do sentiment and translation stuff for each article
    for article in props_arr:
        # each element is [totalSentiment (number), avgWordSentiment (number), sentimentDescription (string)]
        mainSentimentData.append(sentiment.analyzeSentiment(article['body']))
        # each element is [sentence (string), sentenceTotalSentiment (number)]
        sentencesSentiment.append(sentiment.getSentencesSentiment(article['body']))

        # graph sentiment per sentence over sequentially
        sentencesGraphData = []
        for sentence in sentencesSentiment[-1]:
            sentencesGraphData.append(sentence[1])
        plt.figure()
        plt.plot(sentencesGraphData)
        plt.xlabel('sentence number') 
        plt.ylabel('sentence sentiment total')
        plt.ylim([-10, 10])
        plt.grid(True)
        plt.grid(which='major', linestyle='-', linewidth='0.4', color='blue')
        plt.grid(which='minor', linestyle=':', linewidth='0.2', color='gray')
        plt.minorticks_on()
        plt.title('[SENTIMENT] ' + article['headline'] + " by " + article['author'])
        # save the plot into the correct place (NEEDS TO BE CHANGED FOR CORRECT FILE PLACEMENT)
        plt.savefig("temp-" + article['headline'], dpi=196, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format=None,
            transparent=False, bbox_inches='tight', pad_inches=0.5, metadata=None)
        
        # translate
        if args.language:
            print("what")
            print(args.language)
            translations.append(args.langauge, translator.translateText(article['body']))