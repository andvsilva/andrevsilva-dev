from dateparser.search import search_dates
import re
import json
import os

paper = '''
Date: April 27, 2024
Author: Andre V. Silva
Title: "5 Things to STOP Doing to Get RICH in 2024"

Introduction:
I've spent nearly a decade navigating the world of finance and banking and 
I've seen first hand the mistakes people are making day in and day out that 
are stopping them from becoming rich. So in this article I wanted to share with 
you five of the most commonly overlooked bad habits and tips on how to break out of them. 

Body:
1.-Scarcity Mindset vs. Growth Mindset:
Number one, a scarcity mindset. There's this really interesting study done 
with a group of relatively low achieving students. They were split into two groups. 
The first group was the control group and that group was asked to, together, read out 
loud an article describing how human memory works and then later discuss what they learned.

So they learned about long-term short-term memory using repetition. The second group was taught 
about a growth mindset. So they read and discussed an article about how learning makes their 
brain smarter and discussed how they can apply their learnings in their schoolwork. What they 
found was a second group who learned about the growth mindset showed a significant increase in 
effort and motivation towards their learning compared to the first group and this increased 
motivation had a direct correlation to improved performance./endsection

2.-Skimping on Growth:
Number two is skimping on growth. This is something that I did a lot in my 20s and it's only in 
the last few years that my perspective in paying for education has completely changed because 
before I had this mentality that everything is available on the internet for free. So why should 
I pay for further education or learning? But I could just take the time out to learn those things 
myself without having to pay for it. I even bought a course that has helped me with my social skills and 
that is the level of which I pay for learning and development now. Everything you want to learn or 
anything you want to solve or any part of you that you want to develop but don't skimp out on it 
because there's only going to cost you in other ways and to really grow and build wealth you need 
to keep investing in your learning and education./endsection

3.-Doing it all yourself:
Number three doing it all yourself. I saw a motivational quote the other day that read Beyoncé 
has the same 24 hours in the day that we do. Great quote except it missed the fact that our 24 hours 
aren't the same and she has the ability to outsource pretty much everything that she could possibly 
think of and she has a team to run it all. Although we definitely don't have the same 24 hours that 
she does we can however find ways to achieve more in less time because you don't have to do everything 
yourself anymore and for almost everything I've realized that there is some sort of free tool or sister 
that can help you do the thing that you need to faster and better.  

According to a report by Forbes we spend on average 88% of our work week communicating and written 
communication takes up the largest amount of time in that so whether it's writing a persuasive email 
writing an important document preparing a presentation or a pitch written communication plays a huge 
part in every aspect of our working lives and so the ability to do it well and to do it fast can be 
an absolute game changer./endsection

4.-Relying on Being Physically Present:
Next we have relying on being a physically present. We need to create systems or have investments 
that generate income without the need for us having to continue to work. This concept is very different 
from what most of us are familiar with. We're used to thinking that we need to spend 40 years of our lives working 
and then rely on our retirement funds to live out the remaining years. But in self-going down that route 
if we can look at our active income sources and think how can I turn this into something that won't 
require me to be physically present or at least not so involved in five or ten years time then that 
is a way we can start thinking about how to make our money work for us whilst we sleep. Now at the 
start of your career this is a lot harder to do and most if not all sources of income require either a 
lot of time or a lot of money. But then after that depending on how you play your cards and what you 
focus on after the initial stages that will did bend dictate your path to financial independence. When 
it comes to investing Buffett's investment philosophy is centered around the idea of buying and holding 
a diversified portfolio of high quality companies that can grow over time effectively making money without 
the need for constant involvement./endsection

5.-The Garden Hose Theory:
Number five the garden hose theory think of your attention and energy like a garden hose. When the nozzle 
is tightly controlled and directed at a single point the water flow is really strong and it can effectively 
nurture the plant it's aimed at over time. That is like focusing your energy on a few selected tasks at 
least to affect the results and productive outcomes. If you start poking holes along the hose to water 
multiple plants at once the water pressure drops the more holes you add the weaker the stream becomes 
for each task until eventually there's not enough water pressure to be useful for any of the plants and 
that's the equivalent of saying yes to too many commitments your energy and attention gets bred to them 
and nothing is the full focus it needs to actually thrive with so many opportunities out of fingertips 
so many new ideas so many things to try is tempting to say yes to everything that comes our way 
thinking that we don't do everything we're going to miss out but really during this we'll just slow 
us down you don't need to grasp every single opportunity that comes your way you don't need to try 100 
things all at once and we hope that one of them picks up it's a lot more important to have specific 
strategic focus so there's a five things you need to stop doing to become rich this year thanks for 
watching if you enjoyed these videos you'll enjoy this video over here on six habits that made me six 
figures by 24 thanks for watching and see you there./endsection

Conclusion:
In summary, anyone hoping to accumulate wealth and achieve financial success in 2024 must avoid these 
five bad behaviors. The chances of people reaching their financial goals can be greatly increased by changing their 
perspective from one of scarcity to one of abundance, investing in learning and development, using 
resources rather than trying to do everything on their own, diversifying their sources of income to 
include passive streams, and concentrating their efforts on specific tasks.

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
        section = find_between(textbody, f'{sectionname}:', '/endsection')
        dbody[f'{sectionname}'] = section

    else:
        sectionname = find_between(textbody, f'{isection}.-', ':')
        section = find_between(textbody, f'{sectionname}:', '/endsection')
        section = section + '.'
        
        dbody[f'{sectionname}'] = section

paperinfo.update(dbody)
conclusion = find_between(article_content, 'Conclusion:', '\n/End')

paperinfo['conclusion'] = conclusion

with open(filepaperinfo, 'w') as f:
    json.dump(paperinfo, f)

os.system(f'mv {filetxt} {filepaperinfo} json/')

print('Create files txt and json, All done! :)')