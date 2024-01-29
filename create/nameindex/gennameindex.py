import json

papernumber=14


# Opening JSON file
with open(f"../jsonfile/{papernumber}paperinfo.json", 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)

# inputs:
date = json_object['date']
papernumber = json_object['papernumber']
papername = json_object['papername']
description = json_object['description']

# Creating the HTML file
file_html = open(f"{papernumber}nameindex.html", "w")

# html to index
nameindex = f'''
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
        <h2 class="entry__title"><a href="{papernumber}paper.html">"{papername}"</a></h2>
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
        {description}
        </p>
    </div>
</div>
</article> <!-- end article -->
'''


# Adding the input data to the HTML file
file_html.write(nameindex)

# Saving the data into the HTML file
file_html.close()