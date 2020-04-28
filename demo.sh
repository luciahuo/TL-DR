#!/usr/bin/env bash
# article in url form
python3 main.py -url "www.nytimes.com/2020/04/23/opinion/skype-coronavirus-news.html?action=click&module=Opinion&pgtype=Homepage"
# articles in file
python3 main.py -filename "test_file.txt"
# save the articles into local file (no specified directory)
python3 main.py -filename "test_file.txt" -save
# save the articles into local file in specific directory
python3 main.py -filename "test_file.txt" -save "NYTimes"
# language translation
python3 main.py -url "www.nytimes.com/2020/04/23/opinion/skype-coronavirus-news.html?action=click&module=Opinion&pgtype=Homepage" -language "it"
# topic analysis on a group of articles
python3 main.py -filename "test_topics.txt" -topic
# visualize both wordcloud and sentiment graph 
python3 main.py -url "https://www.nytimes.com/2020/04/22/sports/football/patriots-nfl-draft-bill-belichick.html?action=click&module=Top%20Stories&pgtype=Homepage" --visualize 2

