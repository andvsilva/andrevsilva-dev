from dateparser.search import search_dates
import re
import snoop

@snoop
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
    

filetxt = "paperinfo.txt"

with open(filetxt, 'r') as file:
    article_content = file.read()

date = list(search_dates(article_content)[0])
date = date[0]

title = find_between(article_content, 'Title: "', '"\n')
author = find_between(article_content, 'Author:', '\n')
introduction = find_between(article_content, 'Introduction:', 'Body:')
body = find_between(article_content, 'Body:\n', 'Conclusion:')

sections = re.findall('[0-9]+', body)

nsections = int(sections[-1])

for isection in range(1, nsections+1):
    textbody = body

    if isection <= (nsections-1):
        sectionname = find_between(textbody, f'{isection}.- ', ':')

        print(isection)
        section = find_between(textbody, f'{isection}.- ', f'{isection+1}.-')
        print(sectionname)
        print(section)
    else:
        print(isection)
        sectionname = find_between(textbody, f'{isection}.- ', ':')
        content = find_between(textbody, f'{sectionname}:', '.\n')
        content = content + '.'
        
        print(sectionname)
        print(content)

conclusion = find_between(article_content, 'Conclusion:', '\n/End')
print(conclusion)