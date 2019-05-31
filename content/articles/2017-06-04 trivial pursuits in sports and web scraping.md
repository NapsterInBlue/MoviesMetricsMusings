Title: Trivial Pursuits in Sports and Web Scraping
Slug: trivial-pursuits
Tags: python, scraping, tools, trivia

<!-- PELICAN_BEGIN_SUMMARY -->

## High Volume, but to what End?

So in the past couple of years, I've gone on tears where I'm addicted to MOOC's (or Massive Open Online Courses, like Coursera, Khan Academy, etc). Occasionally, I'll really connect with some exceptional material, for instance

- I'm currently revisiting [Andrew Ng's Machine Learning course](https://www.coursera.org/learn/machine-learning), which I loved, and trying my damnedest to implement the whole thing in Python, not Matlab/Octave.
- I got a ton out of the [Data Visualization and Communication in Tableau](https://www.coursera.org/learn/analytics-tableau) course.
- And I recently had a ton of fun learning the fundamentals of MapReduce with [Udacity](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617.

Though, perhaps equally often, I'll engage with a course for a few then give up-- like that time [I was really excited about Jazz Improvization](https://soundcloud.com/manifes7o/coursera-week1) and then got distracted with other things. More perilous, I'm coming to understand that get addicted to the dopamine rush of bookmarking the hell out of everything, and never following up. It's a low-effort, high-"feels"-dividend to imagine all of the cool things that I WILL be learning..........someday. (For real, don't ask me how many O'Reilly manuals I own but haven't read.)

Eventually, it occurred to me that I got really good at watching YouTube videos and following along. Ultimately, though, I was kind of shit at keeping all of the information in my head. Truth be told, looking back-- even at courses that I really enjoyed-- my experience in academia can largely be summarized with the phrase

"Okay. I'll do what I need to to get the grade now, but I'm going to come back and really learn this later."

<!-- PELICAN_END_SUMMARY -->

> **"Okay. I'll do what I need to to get the grade now, but I'm going to come back and really learn this later."**

I don't regret my time at school-- I had some fantastic experiences with some of the best people I'll ever know. But looking back, I'm coming to find that I really short-changed myself by not learning how to learn and retain information.

And then I stumbled across [Barbara Oakley's fantastic "Learning How to Learn" course](https://www.coursera.org/instructor/barboakley). It serves as an excellent primer in all things meta-cognition (thinking about how your brain thinks and grows), and overall I'd highly recommend it. Many people cite various books that they make it a point to revisit to ensure that they're growing in line with the things they read. To wit, books like

- ["GTD: The Art of Stress-Free Productivity"](https://www.amazon.com/Getting-Things-Done-Stress-Free-Productivity/dp/0142000280), which I read, loved, and implemented to great effect
- [Dale Carnegie's classic, "How to Win Friends and Influence People"](https://www.amazon.com/How-Win-Friends-Influence-People-ebook/dp/B003WEAI4E/ref=sr_1_1?s=books&ie=UTF8&qid=1496597074&sr=1-1&keywords=how+to+win+friends+and+influence+people) which should honestly be a required reading for just about anything.
- [The Happiness Trap](https://www.amazon.com/Happiness-Trap-Struggling-Start-Living/dp/1590305841), which a good friend of mine recently recommended and I'm looking forward to digging into soon™.
- And various others

I'd contend that this course should be worked into that rotation as well, as a solid-principled study routine is fundamental to your development in whatever endeavors you're after.

### Anki

But, what this course re-ignited in me, and the reason that I'm writing, is a love for the FREE flashcard software Anki. Essentially, Anki is a really cool tool used to drill and develop deep memorization of information using a concept called spaced-repetition, which is just a $2 phrase that means "you see the cards about only as often as you need them." So when you build a deck of cards for, say, some vocab words, you might get re-served the card every day or so. But the more consistently you get the card correct (when you reveal the back of a card, you can rate how difficult it was to recall on a sliding scale from AGAIN to EASY; more on this later), the longer Anki waits to serve it back up to you. Theoretically, the more comfortable that you are with a card, the fewer and fewer times it'll get served back up to you. When you get to the point where you haven't seen a card in several months and can easily answer the reverse side after a long waiting period, you know that you've achieved deep memorization! Hot dang.

I had a TON of success with this back in my days of university-level Spanish. It's been years, and I can't conjugate worth a damn, but I still retain a great deal of my vocab because of how ingrained it is in my memory. It was a great return on my time spent studying, but for whatever reason, I never thought to utilize this tool for, well, everything else. Until this course reminded me of how damn cool it was, then I got a little carried away, lol

When I started with QL a couple years ago, it was one of the first bits of software that I threw onto my work laptop, and I've since used it for everything from remembering bits of factoids and business knowledge, to memorizing back-end status codes, to having useful code snippets on hand

* I got tired of Googling "How do you get the pandas library in Python to stop showing you all of your numbers in scientific notation?"

``` python
pd.set_option('float.display_format', lambda x: '%.2f' %x)
```

* What's that snippet of code that you put at the top of your SQL queries to check for and auto-drop temp tables so your queries don't break trying to write over pre-existing tables?

``` sql
IF OBJECT_ID('tempdb..#temp') IS NOT NULL DROP TABLE #temp
```

I love trivia. I used to play a ton back in college, but it was more or less me going to be with friends and enjoy hella-cheap apps. Was never really good at it. Then recently, I just started writing down every single question that I got wrong on some scratch paper and throwing it into Anki. Furthermore, my good friend Scott got me into [Learned League](https://learnedleague.com/) which is a more-or-less daily trivia league where you get dumped on with some punishingly hard trivia that I more often than not whiff hard on... and then put into cards.

And it's great. Nowadays, I try to refrain from Reddit and Facebook until I'm caught on all of my cards for the day (because recall, the more I get them right, the less they show up. Some days are light, some days aren't, but it's always optimized for my retention). Leveraging those small pockets of time in my day-- elevator rides, in between reps at the gym, procrastinating getting out of bed in the morning-- to drill and keep fresh knowledge that otherwise escapes me is a real thrill for me. I feel like I'm getting smarter for free, and weaning myself off of my bad dopamine-seeking habits to boot.

## Examples from my Decks

### Presidents

Learning the different presidencies is a really useful bit of trivia anchoring. If I can map the whole history of the US to which president was reigning, then general-purpose history trivia questions have a bit of context, ya know? And so the front side is short and sweet.

<center>{% img {static}/images/anki/jamesMonroe.PNG 400 %}</center>

And then the reverse

<center>{% img {static}/images/anki/jamesMonroe_reverse.PNG 400 %}</center>

1. Which president number he was
2. What years they were in office
3. The aforementioned "How easy was this for you" rater. If I need it again, I'll see it during that same session, if it's easy, I'll see it in 5 days. These values have a repeated multiplicative scaling effect-- thus my card for Obama's term has been marked "EASY" so many times, that I don't see it for another couple of years.

### Movies


The reverse side of my Movie Trivia is a bit more rigorous. It includes

- The year
- Notable cast members
- Notable Directors
- Notable Writers
- Any and all information about how they did at the Academy Awards

<center>{% img {static}/images/anki/jungleBook.PNG 400 %}</center>

If about every movie I watch gets a [Letterboxd review](https://letterboxd.com/nick_m3blog/films/reviews/), every single movie I watch gets an Anki card.

### Quotes

Finally, I have a deck for quotes that I like or want to remind myself. These can be things that I read somewhere, something someone said in a movie that resonated with me, or snippets of conversations that I've had that I want to hold onto. Here, I re-purpose the re-serve ratings at the bottom, not as my ability to remember them, but as a benchmark for how soon I want to wait before I hear them again.

<center>{% img {static}/images/anki/bangs.PNG 400 %}</center>

### The Rest

Here's the broad swath of decks that I keep current with on my home PC. Buncha other, more technically-leaning, stuff in a separate account on my work computer.

<center>{% img {static}/images/anki/decks.PNG 200 %}</center>

### I Suck at Sports

I love watching them. I enjoy playing them. During my years in the Michigan Marching and Basketball Bands, I was thinking about them constantly. Now that I'm graduated, I keep a bead on Michigan, but otherwise I don't really follow them at all. I'm certain that I would love hockey if I gave it a chance. Or the NBA. Hell, even NASCAR. But on the whole, sports are just one more thing to follow, so I don't. Which makes it my worst trivia subject by a huge margin. So in an effort to be less garbage at it, I decided to start learning the championships of various sports and leagues over the past few years. I took to Wikipedia and started poking around, typing up some new Anki cards, but it got monotonous fast and just felt like something that I should be automating. And so I spent this weekend tinkering around in Python so I can procedurally pull back new information, for whatever years I requested, as I start to get these factoids under my belt, to keep growing these decks.

### <center>[At long-last your mood music for the remainder of the read](https://soundcloud.com/jhlodin/oppa-spacejam-style)</center>

## Sucking less at Sports

### World Series

Blame it on my crap attention-span, I don't watch a lick of baseball. And I've got a real cognitive dissonance about that. As a numbers/data nerd, this should be the sport that I'm most dedicated to watching, stereotypically. I love the movie Moneyball and get fired up about it every time I watch it, but then I turn on a baseball game and make it minutes, not hours, before I'm doing something else. Football and basketball just more my speed, I guess. Anyhow, to get at World Series information, I just jumped right to the "List of World Series Champions" page of Wikipedia and clicked into the years of each game, in red below.

<center>{% img {static}/images/anki/worldseries1.PNG 600 %}</center>


From here, I would basically mine the info box in the right pane for pretty much everything I'm interested in memorizing.

<center>{% img {static}/images/anki/worldseries2.png 600 %}</center>

For you unawares, any time that you're trying to figure out how to scrape a site, the F12 and CTRL+SHIFT+C keys are your best friends. The former opens up the underlying HTML, while the latter allows you to click on elements of the page to highlight where they are in the garbly-goop (a very-technical Computer Science term) of web code your field of interest lies. From here, I used the [Requests](http://docs.python-requests.org/en/master/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) libraries for Python to pick out the pieces that I wanted.

My objectives were pretty straight-forward. I was grabbing:

<center>{% img {static}/images/anki/worldseries3.PNG 400 %}</center>

1. The winning team, which was thankfully always the first of the two teams on these pages
2. The losing team, just the opposite
3. The MVP of the series
4. And, of course, the year, but that was implicit in whatever page metadata I was hitting for this info

Then I'd transform those fields into Anki cards where the front read "`[YEAR OF INTEREST] World Series`" and the reverse had "`[WINNING TEAM] > [LOSING TEAM]`" and then a couple lines down would list the `[MVP]`.

### NBA Playoffs

Hey, what do you know, this approach translated more or less seamlessly to figuring out the NBA Finals!

<center>{% img {static}/images/anki/nba1.png 600 %}</center>
<center>{% img {static}/images/anki/nba2.PNG 400 %}</center>

### Stanley Cup Finals

And then for whatever reason, I stopped being able to rely on this format.

<center>{% img {static}/images/anki/nhl1.PNG 600 %}</center>

This chunk of the algorithm was fine.

<center>{% img {static}/images/anki/nhl2.PNG 450 %}</center>

But then I couldn't use the "team on top was the winner" heuristic anymore. Bleh.

My work-around was kind of janky:

- First, I grab anything that looks like a team

<center>{% img {static}/images/anki/nhl3.png 400 %}</center>

- Then, give me all of the teams who are listed with a bold font, like the Red Wings above. This was the winning team.

<center>{% img {static}/images/anki/nhl4.png 400 %}</center>

- Using that result, I'd then 'subtract' whatever team this was from the list of teams.

<center>{% img {static}/images/anki/nhl5.png 400 %}</center>

- Finally, this list of teams, only having one value, is now the list of losers in this series (length 1)

<center>{% img {static}/images/anki/nhl6.png 400 %}</center>

And grabbing the MVP worked as intended.

## One Last Hiccup

It was like 2am. I finally got to that huge sigh of relief that celebrated being done code-monkeying, and I start running this damn thing.

I grab the last 20 years of NBA Finals without a hitch.

World Series works great, too.

Then the last 20 years of Stanley Cup Finals breaks. Balls.

<center>{% img {static}/images/anki/lockout1.PNG 550 %}</center>

And so I toss in a Try/Except block, which is the coding equivalent to saying "I know this is busted, but do it anyways, lol." with a print statement to zero in on the year that this thing goes off the rails on the last line.

<center>{% img {static}/images/anki/lockout2.PNG 550 %}</center>

Ran it again. Huh. What's going on in 2005?

<center>{% img {static}/images/anki/lockout3.PNG 500 %}</center>

Again, the universe reminds me that coding skills are a complement, not a substitute, for some good old-fashioned common sense and practical knowledge.

<center>{% img {static}/images/anki/lockout4.PNG 550 %}</center>

## Conclusion

There's still work to go on this one, but I was excited to share the process I used to get at it with you all. I'm going to expand this out to get SuperbOwl stuff (with the addition of stadium information), March Madness final games, and likely a few others that aren't coming to me right now. But when I sat down to expand these decks a bit, I realized that it was going to be more time that it was worth typing everything out by hand, introducing the possibility (or likelihood...) of human error and all-around brain fry of monotonous data entry. Of course, after a couple hours of blowing the dust off of my Web Scraping tools and another couple of writing this thing up, I don't really have a leg to stand on from a "this was a huge time-saver!" perspective, lol. Nevertheless, I hope that you had as much fun reading this as I did working on it.

## Links

Seriously, use [Anki](https://apps.ankiweb.net/). It's so useful that it's basically cheating.

Huge thank you to GitHub user DrLulz, who I'm sure will never read this ever, for stitching together [some code I leveraged to write to my existing decks.](https://gist.github.com/DrLulz/fc802d43e310cec1ecd7)

And as always, a [GitHub link to the hacky code I used to put this together.](https://github.com/NapsterInBlue/SportsAnkiCards)

*Editor's note: To actually write the cards that I built to my deck, I needed to use a library that I didn't write. And for that, I was finally forced to use Python 3. You win this round, Jim Keena.*
