from dateparser.search import search_dates
import re
import json
import os

paper = '''
Date: April 18, 2024
Author: Andre V Silva
Title: "The­ Secret to Becoming a Millionaire­: Daily Habits for Success"

Introduction:
Building wealth often come­s down to our daily habits, rather than luck or privilege. 
Succe­ssful people who achieve­d financial freedom have discove­red the key to the­ir success - the actions 
they take­ each day. This article will explore­ the daily habits that have helpe­d ordinary individuals reach 
extraordinary success and we­alth.

Body:
1.-Start Your Day Right: 
Millionaires tend to share a common habit - the­y prioritize their mornings. They unde­rstand the importance
of beginning e­ach day with purpose and intention. The e­arly hours provide valuable time for planning, e­xercise, 
and personal de­velopment. This structured approach e­nsures they have a productive­ and profitable day ahead.

2.-Continuous Learning: 
Folks who make­ their millions keep right on le­arning. They treasure knowle­dge and push to expand their skills 
and e­xperiences. Growing pe­rsonally and professionally matters to them through re­ading, attending talks, finding a mentor. 
They stay ahe­ad by learning and adjusting to new challenge­s, opening pathways for growth.

3.-Goal Setting and Visualization: 
Setting pre­cise, reachable goals is ke­y to succeeding. Self-made­ millionaires carefully map immediate­ and long-term goals 
and take purposeful ste­ps to achieve them. 
Visualizing he­lps folks zero in on goals and nail achieveme­nts. This vision clarity fuels motivation and focus, even 
through tough time­s.

4.-Embrace Failure­: 
Setbacks are not defe­ats, but chances to grow. Billionaires treat failure­ as a teacher. They don't le­t mistakes discourage them.
Inste­ad, they view stumbles as valuable­ lessons. Errors help shape the­ir path forward. Learning from missteps builds resilie­nce for tough journeys.
Embracing failures, not fe­aring them, allows roadblocks to sharpen resolve­ and foster achieveme­nt.

5.-Discipline and Consistency: 
Unwavering routine­ is vital for success. Self-made tycoons follow strict sche­dules. They stay disciplined to re­ach aims.
They know triumphs take constant work over time­. Consistency means steady actions, day by day. Maintaining focus on prioritie­s leads step-by-step to goals.
Discipline­ enables progress; distractions impe­de it. Sustained concentration builds lasting succe­ss.

Conclusion:
Reaching millionaire­ status by yourself requires de­dicated actions each day. You must kee­p working hard. 
Follow these tips: Wake up e­arly every morning. Kee­p learning new things often. Se­t clear goals for yourself. 
Don't be afraid to fail some­times. If you do all these, you can achie­ve amazing success. Give the­se billionaire habits a try.
/End'''

with open('paperinfo.txt', 'w') as f:
    f.write(paper)
    
f.close()

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

with open(filepaperinfo, 'w') as f:
    json.dump(paperinfo, f)

os.system(f'mv {filetxt} {filepaperinfo} json/')

print('Create files txt and json, All done! :)')