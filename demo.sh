# article in url form
python3 main.py -url "www.nytimes.com/2020/04/23/opinion/skype-coronavirus-news.html?action=click&module=Opinion&pgtype=Homepage"
# articles in file
python3 main.py -filename "test_file.txt"
# save the articles into local file
python3 main.py -filename "test_file.txt" -save
# language translation
python3 main.py -url "www.nytimes.com/2020/04/23/opinion/skype-coronavirus-news.html?action=click&module=Opinion&pgtype=Homepage" -language "Italian"
# topic analysis on a group of articles
python3 main.py -filename "test_topics.txt" -topic
# visualize both wordcloud and sentiment graph 
python3 main.py --visualize 2

