from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path

parent_dir = str(Path(__file__).resolve().parents[0])

#creastes word cloud from text
def visualize_wordcloud(text, dir=""):
    wordcloud = WordCloud(max_font_size=70, max_words=100, background_color="white").generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    if dir != "":
        filename = os.path.join(parent_dir, "My_TLDR_Archive") + dir
        plt.savefig(filename + "/wordcloud.png")
    plt.show()
    
#creates sentiment of time grahph for a particlular article
def visualize_sentiment(sentencesGraphData, article, dir=None):
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
    if dir is not None:
        plt.savefig(dir + "/temp-" + article['headline'], dpi=196, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format=None,
            transparent=False, bbox_inches='tight', pad_inches=0.5, metadata=None)
