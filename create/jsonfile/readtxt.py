from dateparser.search import search_dates
import re
import json

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
    

filetxt = "paperinfo.txt"
filepaperinfo = "paperinfo.json"

with open(filetxt, 'r') as file:
    article_content = file.read()

date = list(search_dates(article_content)[0])
date = date[0]

title = find_between(article_content, 'Title: "', '"\n')
author = find_between(article_content, 'Author:', '\n')
introduction = find_between(article_content, 'Introduction:', '\nBody:')

paperinfo = {
    'date': date,
    'title': title,
    'author': author,
    'introduction':  introduction
}

body = find_between(article_content, 'Body:\n', 'Conclusion:')

sections = re.findall('[0-9]+', body)
nsections = int(sections[-1])

dbody = {}

for isection in range(1, nsections+1):
    textbody = body

    if isection <= (nsections-1):
        sectionname = find_between(textbody, f'{isection}.-', ':')
        section = find_between(textbody, f'{sectionname}:', '.\n')
        dbody[f'{sectionname}'] = section

    else:
        sectionname = find_between(textbody, f'{isection}.-', ':')
        section = find_between(textbody, f'{sectionname}:', '.\n')
        section = section + '.'
        
        dbody[f'{sectionname}'] = section

paperinfo.update(dbody)
conclusion = find_between(article_content, 'Conclusion:', '\n/End')
paperinfo['conclusion'] = conclusion

print(paperinfo)


with open(filepaperinfo, 'w') as f:
    json.dump(paperinfo, f)