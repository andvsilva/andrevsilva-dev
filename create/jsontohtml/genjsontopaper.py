from dateparser.search import search_dates
import re
import json
import os

paper = '''
Date: April 27, 2024
Author: Andre V. Silva
Title: "10 Money Secrets To Make Your First $1,000,000"

Introduction:
Ladies and gentlemen, you are gonna want to listen 
very closely to today's article because I'm gonna show you 
the 10 money secrets to make your first million these are the 
money secrets I use to make my first million 
dollars and my first ten million dollars and then tens of millions. 
since then This is not gonna be your hey save money on Starbucks 
or your hey invest in a 401k and eventually You'll make a million.
this is for the people that are serious about making their first 
million and not only that, But turning one million into many 
millions more not only for yourself but for your future family. 
So on that note grab a pen and paper and let's get into it.

Body:
1.-Money is a Never-Ending Game:
So the first secret is that money is a never ending game and you 
should treat it as such I understand your position. You're looking 
at a million dollars in your thinking. If I had a million dollars 
my life would totally change and yes, of course your life will get better 
But just understand when you reach your first million, what do you think 
you're gonna stop the game? you're gonna be happy? You're gonna keep playing 
the game. 

You're gonna keep going and the only way to stay sane is understand 
that money is a never ending game! the only people that get depressed or think
that money will ruin your life are the people that think that money is a 
destination some sort of number is the end of your life. You can be very proud with 
your financial situation, But doesn't mean that you'll ever be content or you'll be happy 
because this is a never ending game So treat it as such./endsection

2.-Learn When to Say No:
The next money secret is learn when to say I don't have the appetite for that right now,
one of the reasons I did so well in my career is I understand that my main businesses now 
which are software companies I understood that these were very difficult businesses.

so you need to understand when to pick the right vehicle and when to pick 
the right opportunity for your career stage. It's kind of like you're doing bench press, 
you start off with one plate until you can work your way up to two plates three plates, etc. 
One of the worst things that you can do is commit to a business idea to venture to an endeavor 
and say that you're gonna give it your all or say that you're gonna push when you know that 
either you don't have the ability or you simply just don't have the Commitment and the hunger 
by the way that is totally fine. It's fine to understand that there are certain opportunities 
that you simply don't have the appetite for right now and that doesn't mean that you'll 
never have the appetite for it./endsection

3.-Seeing is Believing:
The next money secret is that it's never possible until you see it and Either 
you see it online or even more powerful you see it in person. There are certain 
people with 250,000 dollars, on their wrist when you look at truly wealthy people 
and you realize, hey Most of times they don't really wear brands most of times, they are 
very under the radar when you look at wealthy people and you see the way that they move 
and the way that, they act you first of all start to observe it, but you also start to realize 
if your reality is. I can't imagine making more than $50,000 a year and someone is literally 
sitting down with a hundred fifty thousand dollars on their wrist or whatever the number may 
be it totally changes in its shifts your reality. This is also why if you can just walk 
around affluent, areas whatever the nice area of your city is go there walk around 
see all the money, see all of the wealth and it will start to sink into your 
subconscious that it is possible to win!/endsection

4.-Fast Money vs. Slow Wealth:
Now the next money secret is aim to make money fast, but build wealth slowly, so listen there's no such 
thing as get rich quick, but there is such a thing as get rich quicker and there's certain vehicles in 
life where you can get compensated far more for your time, that you put in for the talent and the skill 
that you develop in that vertical, then you would if you spent a thousand hours working in a different 
industry, so listen never rush the process, but of course try to make money as fast as possible, try to 
become rich as quick as you can, but rich and wealthy are two very different things! so aim to build your 
wealth slowly, because true wealth is only built through years and years and Decades of wisdom of learning 
the right money lessons, again and again and again, so aim to become rich quick but aim to become wealthy 
slowly because that's the only way that you will keep it! /endsection

5.-Ignore Financially Illiterate Advice:
Number five is ignore money advice from the Financially illiterate, I truly believe that in this world It 
is a matter of the financially literate and the financially illiterate and it doesn't matter, what background 
and what color race religion whatever it is it doesn't matter where you come from it's simply a matter of 
financially illiterate and financially illiterate! but the only difference between us is I made sure that 
I was gonna learn from a young age the language of money, what money is where it comes from how it works? 
So there are people in your life that have the best intentions for you, the love you they care for you,
But you have to ignore their advice, so that way you can take care of not only you, but in future take 
care of them./endsection

6.-Money is Energy:
Number six money is energy and energy can never stay stagnant, I see this law where people make money and 
they are so afraid to spend that money, they're so afraid to circulate that money back into the economy, 
they're so afraid to release that energy and they're living in such scarcity mindset that they just end 
up losing it all. Somehow or they may not lose it but more money never flows them, money is energy It's 
inflow and it's outflow and that doesn't mean that everything that comes in must go out No, in fact especially 
in your 20s you should be saving and investing majority of the money that you make, but never hoard that 
money because if you do, the money becomes stagnant and you have cut off the flow of energy./endsection

7.-Build Your Peace of Mind Pot:
Number seven is you need to build your peace of mind pot, this is a fun that gives you true peace of mind 
this needs to be a safety net, where you know that no matter what happens no matter how ambitious how big a risk,
you may even take that you always have something to fall back on, I do not believe the money buys happiness, 
But I believe the money can if you do it right buy you peace of mind and bear mine That doesn't mean making a lot 
of money because the person who makes $200,000 a year and only spends $40,000 and has a very big peace of mind pot 
that person has far more peace in their life than the person who makes $20 million a year and manages to spend $19 million, 
because they're running on such thin margins, they're playing such a dangerous game so from day one if you can build 
your peace of mind pot. You need to enjoy your life! And if you don't want to enjoy your life go spend it on your loved ones on the 
ones that you care about let them enjoy the spoils of your work, but as I said always keep your peace of mind pot./endsection

8.-Money is an Identity:
The next one is money is an identity and it truly is! I'm telling you right now you could work extremely hard, But if you 
have the identity of a poor person, it will always chain you in life, you do not get what you deserve you get what you 
think you deserve, because what you think you deserve dictates your actions and your actions dictate what you actually 
get in life. You know, it's very unfortunate, you see a lot of people in abusive relationships and the reason they stay 
in those relationships is, because they have some part of their Identity that thinks they deserve it, because the crazy 
thing is after they get out of one abusive relationship, They find their way into another so it is ingrained as a part 
of their identity, So you can have something that is as heartbreaking and unfortunate as that. But also from the extreme
side of things all the way to the person that just has an identity, they are not someone who is worthy or deserving of 
money. This is why I was tell people go buy that $12 coffee at the hotel go into these affluent areas and just 
understand that these are normal people they move differently. They talk differently. 
They carry themselves differently, but at the end of the day, these are just normal people now./endsection

9.-Reputation is Priceless:
The next one is the reputation can never be reborn, so act accordingly in life you need to understand that you will 
always have the opportunity to make more money, but your reputation is almost impossible to claw back, so the next 
time you think about f***ing over some business partner or cutting someone out of a deal when you made a promise or 
In general just making money from dirty means understand that your reputation will live with you for the rest of time, 
your reputation carries on because just like Chinese whispers People will talk and talk and it will continue to 
permeate, So when you understand their your reputation is probably one of the most fragile things on earth never 
ever put it at risk, because it's very hard to rebuild!/endsection

10.-Ask the Hard Questions:
Now number 10 is that one man's opportunity is another man's downfall, there is a certain business opportunity that 
will probably make you a billionaire, but will probably wreck my career and vice versa, So just understand that not 
all opportunities are created equal you need to assess an opportunity based on where you are in your career what 
you're like as a person, you know your strengths your weaknesses as well as your risk tolerance, how averse you are to 
risk and not only risk, but stress I'm the sort of person that can deal with immense amounts of stress and I just have 
this ability to take on stress and responsibility because from a young age I had to take care of me and my mom Whereas 
for another person they may crumble that doesn't mean that they're a bad entrepreneur or a bad business person or whatever 
It is it just means that they're different so my opportunity could be their downfall So really just understand that concept 
when assessing what the next step is for you./endsection

Conclusion:
To finish this article, I give to you 10 lessons about language of money that can truly can change
your life! And remember money is not the end of the game, but the tool to build a prospect and succe­ssful
life. Kee­p going, my friend.
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