import os 
from pathlib import Path
from datetime import datetime
parent_dir = str(Path(__file__).resolve().parents[0])

#always adds files to default of MyTL;DR
def write_articles_to_file(articles, dir=""): #directory optional - passed in the form "/dirname"
    # create overall dir for TLDR
    path = os.path.join(parent_dir, "My_TLDR_Archive") 
    os.makedirs(path, exist_ok = True) 
    
    #get current time for file name
    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d at %H-%M-%S")
    if len(dir) != 0:
        os.makedirs(path + dir, exist_ok = True) 

    for idx, a in enumerate(articles):
        #file names indicate date & time processed and order in file if applicable
        new_filename = path + dir + "/TLDR-" + str(idx) + " " + date_string + ".txt" 

        #write all available features to txt file for archiving
        f = open(new_filename, "w")
        f.write("Headline: " + a['headline'])
        f.write("\n\nAuthor: " + a['author'])
        f.write("\n\nDate Published: " + a['date'])
        f.write("\n\nKeywords: " + ", ".join(a['keywords']))
        if 'summary' in a:
            f.write("\n\nSummary:\n" + a['summary'])
        f.write("\n\nBody:\n" + a['body'])
        f.close()
