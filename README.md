# TL-DR
This is a Python CLI tool that analyzes New York Times articles and does fundamental text analysis on them, creating visualizations of their data. The purpose of this “TL;DR” tool is to help readers be able to read in an efficient and well-informed manner, as well as provide an archive mechanism for users to be able to save and organize their favourite online content in file form. 

Dependencies (may need to pip3 install): numpy, matplotlib, nltk, pandas, sklearn, googletrans, wordcloud
may also need to in Python:
>>>import nltk
>>>nltk.download('wordnet')


TL-DR performs sentiment analysis by default, using AFINN data, but also can perform topic recommendation analysis using the “-topic” tag. AFINN uses a per word ranking between -3 (most negative) and 3 (most positive) to analyze the sentiment of each word. 

The -v or --visualize tags visualize the data of all articles, with parameters 0 creates a wordcloud image for the article, 1 creates a sentence sentiment graph where each sentence is plotted based on its total AFINN sentiment value. Option 2 creates both.

usage: main.py [-h] [-url URL] [-filename FILENAME] [-language LANGUAGE] [-topic] [-save [SAVE]] [-v {0,1,2}]

a TL;DR news reader for the New York Times

optional arguments:
  -h, --help                            show this help message and exit
  -url URL                            the news article url
  -filename FILENAME       the filename that contains the news article urls
  -language LANGUAGE    language suffix to translate to (ja : Japanese, fr : French, gr : 
         German, es: Spanish)
  -topic                                  option to suggest topics in which user may be interested
  -save [SAVE]                     the directory in which a tl;dr file will be saved
  -v {0,1,2}, --visualize {0,1,2}         visualize data of all articles, 0: word cloud | 1: sentiment 
                                                           graph | 2: both
Examples:
This command would get the article in quotes and return the headline, author, summary, complete text, and sentiment analysis of the article.
python3 main.py -url "www.nytimes.com/2020/04/23/opinion/skype-coronavirus-news.html?action=click&module=Opinion&pgtype=Homepage"

This command would get the article(s) in the file “test_file.txt” and return the headline, author, summary, complete text, and sentiment analysis of the article for each article.
python3 main.py -filename "test_file.txt"

This command would get the article in quotes and return the headline, author, summary, complete text, sentiment analysis, and translation to Italian of the article
python3 main.py -url "www.nytimes.com/2020/04/23/opinion/skype-coronavirus-news.html?action=click&module=Opinion&pgtype=Homepage" -language "Italian"

This command would perform topic analysis on each article in “test_topics.txt”
python3 main.py -filename "test_topics.txt" -topic
