import json
import sys

papernumber = sys.argv[1]

# Opening JSON file
with open("json/paperinfo.json", 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)

# inputs:
date = json_object['date']
title = json_object['title']
author= json_object['author']
introduction = json_object['introduction']

# Creating the HTML file
file_html = open(f"papertopage/{papernumber}paperindex.html", "w")

# html to index
headindex = f'''
<!-- #{papernumber} paper-->
<article class="masonry__brick entry format-standard animate-this">
    
<div class="entry__thumb">
    <a href="{papernumber}paper.html" class="entry__thumb-link">
        <img src="images/finance/tamb{papernumber}paper.png" 
                srcset="images/finance/tamb{papernumber}paper.png 1x, images/finance/tamb{papernumber}paper.png 2x" alt="">
    </a>
</div>

<div class="entry__text">
    <div class="entry__header">
        <h2 class="entry__title"><a href="{papernumber}paper.html">"{title}"</a></h2>
        <div class="entry__meta">
            <span class="entry__meta-cat">
                <a>Freedom</a>
            </span>
            <span class="entry__meta-date">
                <a href="{papernumber}paper.html">{date}</a>
            </span>
        </div>
    </div>
    <div class="entry__excerpt">
        <p>
        {introduction}
        </p>
    </div>
</div>
</article> <!-- end article -->
'''


# Adding the input data to the HTML file
file_html.write(headindex)

# Saving the data into the HTML file
file_html.close()

print('head for index page, All done! :)')