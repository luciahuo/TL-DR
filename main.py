# file with the basic parsing and I/O functionality
import argparse
import requests
from our_parser import parse_NYT
from analyze import get_keywords
from archive import write_articles_to_file
from analyze import get_topics
from visualize import visualize_wordcloud
from visualize import visualize_sentiment
import sentiment
import translator
import pprint
import re
import sys
pp = pprint.PrettyPrinter(indent=4)


def parse_args():
    parser = argparse.ArgumentParser(description='a TL;DR news reader for the New York Times')
    parser.add_argument('-url', help='the news article url', type=str)
    parser.add_argument('-filename', help='the filename that contains the news article urls', type=str)
    parser.add_argument('-language', help='language suffix to translate to (ja : Japanese, fr : French, gr : German, es: Spanish)', type=str)
    parser.add_argument('-topic', help='option to suggest topics in which user may be interested', action='store_true')
    parser.add_argument('-save', help='the directory in which a tl;dr file will be saved', nargs='?', const=" ", type=str)
    parser.add_argument('-v','--visualize', help="visualize data of all articles, 0: word cloud | 1: sentiment graph | 2: both", nargs=1, type=int, choices=range(0, 3))
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
            if 'http' not in l and l.strip(): #ignores lines with only whitespace
                l = "https://" + l.strip()
            covers.append(requests.get(l).content)
        f.close()
        return covers


if __name__ == '__main__':
    args = parse_args()
    pages = []
    if args.url:
        args.url = re.sub("\"", "", args.url)
        if 'http' not in args.url and args.url.strip(): #ignores lines with only whitespace
            args.url = "https://" + args.url.strip()
        url = args.url
        pages = get_html(url)
    elif args.filename:
        pages = get_html_from_file(args.filename)
    else:
        print("need either url or filename")
        sys.exit()
    # array of props for all input articles
    props_arr = parse_NYT(pages)

    # sentiment data
    mainSentimentData = []
    sentencesSentiment = []
    # translation data
    translations = []

    #saves to appropriate files in folder
    if args.save:
        if args.save == " ":
            write_articles_to_file(props_arr)
        else:
            write_articles_to_file(props_arr, "/" + args.save) 

    for article in props_arr:
        # each element is [totalSentiment (number), avgWordSentiment (number), sentimentDescription (string)]
        mainSentimentData.append(sentiment.analyzeSentiment(article['body']))
        # each element is [sentence (string), sentenceTotalSentiment (number)]
        sentencesSentiment.append(sentiment.getSentencesSentiment(article['body']))

        # graph sentiment per sentence over sequentially
        sentencesGraphData = []
        for sentence in sentencesSentiment[-1]:
            sentencesGraphData.append(sentence[1])

        if args.visualize and (args.visualize[0] == 1 or args.visualize[0] == 2):
            if args.save and args.save != " ":
                visualize_sentiment(sentencesGraphData, article, "/" + args.save)
            else:
                visualize_sentiment(sentencesGraphData, article, "")
                
        #prints basic attributes of an article
        pp.pprint(article['headline'])
        pp.pprint("By: " + article['author'])
        pp.pprint("Date Published: " + article['date'])
        pp.pprint("Keywords: " + ", ".join(article['keywords']))
        if "summary" in article:
            pp.pprint("Summary: " + article['summary'])
        pp.pprint(article['body'])
        # translate
        if args.language:
            translations.append(translator.translateText(args.language, article['body']))
            pp.pprint("Translation to " + args.language + ":")
            pp.pprint(translations[-1])
        
        # print sentiment last
        pp.pprint("Total AFINN sentiment: " + str(mainSentimentData[-1][0]))
        pp.pprint("Average word AFINN sentiment: " + str(mainSentimentData[-1][1]))
        pp.pprint("Overall this article has " + str(mainSentimentData[-1][2]) + " sentiment")
        pp.pprint(" ")

    #gets all body text from all documents
    all_text = [ obj['body'] for obj in props_arr]

    #topic matches - prints suggested topics to look into
    if args.topic and not args.url:
        get_topics(all_text)

    #visualizes wordcloud
    if args.visualize:
        all_text_string = " ".join(all_text)
        if args.visualize[0] % 2 == 0:
            if args.save:
                if args.save == " ": #did not specify directory --> put directly in archive
                    visualize_wordcloud(all_text_string, "")
                else: # put in user-specified directory
                    visualize_wordcloud(all_text_string, "/" + args.save)
            else:
                visualize_wordcloud(all_text_string)


