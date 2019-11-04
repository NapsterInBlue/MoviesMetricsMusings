Title: A Big Ol' Page of Resources
Author: Nick
Slug: resources
Date: 2018-04-01
Tags: python, technical, tools, wellness

[TOC]

# Data and CS

## Where I Started with this Stuff

Where I'm at today in my skillset/career is the result of a ton of trying, sucking, pivoting, and all around figuring it out as I went. I didn't know a damn thing about programming (hell, I barely knew how to use Excel) until my Senior year of college. To anyone trying reading this post to figure out how to get started, I feel that it bears benchmarking where I was when I decided to go down the Data Analyst rabbit hole. There's a whole lot of great stuff to engage with, and as far as I can tell, no best road map to navigate it with. This is how I got started, but YMMV.

- I was studying to be an Actuary for a good while. Got through Calc 1-4, Linear Algebra, Stats, Probability, Interest Theory. Didn't have good study habits and hit a real block in my Exam progression. I definitely use all of them in one capacity or another, but wish I'd understood how absolutely fundamental solid Linear Algebra chops are.
- Near the end of undergrad, I started dipping my toes into Computer Science, and if I could do it all over again, I'd have, for sure, focused on this route. Learned the fundamentals (data structures, abstraction, OOP, resource management) in C++, took a Discrete Math class, and then they handed me a diploma before I could take any more. Wound up graduating with a B.S. in Econ, but with a far greater micro than macro focus.
- And so during my last semester, while I was only taking two classes, I decided to simultaneously learn R and Python. I'd read all over that they were great tools to have in the Data Analyst role I was entering, but was unclear which would be better. I read The [Art of R Programming](https://www.amazon.com/Art-Programming-Statistical-Software-Design/dp/1593273843/ref=sr_1_1?ie=UTF8&qid=1499489909&sr=8-1&keywords=the+art+of+r+programming) and [Learn Python the Hard Way](https://www.amazon.com/Learn-Python-Hard-Way-Introduction/dp/0321884914/ref=sr_1_1?ie=UTF8&qid=1499489885&sr=8-1&keywords=learn+python+the+hard+way), but unfortunately didn't find myself much closer to picking one. Then I stumbled across a blog where using Python, a guy had:
    - [Ripped off old piano reels of a lost Gershwin tune (love Gershwin) and made sheet music from it. It blew my damn mind.](http://zulko.github.io/blog/2014/02/12/transcribing-piano-rolls/)
    - [Pulled down YouTube videos and made gifs (pronounced gifs) out of them.](http://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/)

I was sold.

## My Python Essentials


For anyone getting started with programming, one of the biggest barriers to entry is, IMO, the frustration of getting set up properly (read: why I still don't know Scala). Save yourself the headache and download the following:

- The [Anaconda](https://www.anaconda.com/download/) distribution of Python, which pre-configures a whole mess of tools and libraries together so you don't have to. Expanding on what comes in the box is also super easy. I still use this today. Also, unless you have a reason to otherwise, [I think you should download the latest version of 3.]({filename}/articles/2018-05-01 why I switched to python 3.md)

- Secondly, get yourself a better text editor than Notepad, where you can write all of your code. I personally love Sublime Text Editor.


To reiterate, when I first learned Python, I already had a pretty fair knowledge base of the underlying concepts-- I was more reading for syntax. HOWEVER, the first two courses in the free [Python for Everybody Coursera track](https://www.coursera.org/specializations/python) appear to be excellent, gentle introductions to Python and Computer Science fundamentals. It's the first place I steer anybody wanting to know the basics. And honestly, once you've got these down, the scope of things that you could learn on your own just explodes.

Another excellent primer is [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/), which is about as straight forward as its premise suggests. It gives you a rundown of the basics in the first few chapters and then has a real emphasis on making your bothersome, tedious everyday tasks become scripts that you can run so you can free up time. I love its practical approach and have a copy of this one on my shelf.

After I got down the basics, [Python for Data Analysis](http://shop.oreilly.com/product/0636920023784.do) became my bible. This is such a great book and I'd say a must have for anybody hoping to do Data Anything.


## Honorable Mention: Grokking

Might be a bold stance, but once you get comfortable using Python, you should really think of [Grokking's Algorithms](https://www.manning.com/books/grokking-algorithms) as a required reading. It's crucial in your development as a programmer to understand how things are working and how you could improve them-- all style aside, just because something runs doesn't mean that it's good. It gave me a real intuition for what was going on under the hood and turned me on to so many practical ways to solve problems. Really can't stress enough how much I love this book. I've lifted whole chapters and taken them as topics to Knowledge Shares and had whole rooms of people following along, near-effortlessly, because of how well this book is written.

## 3Blue1Brown Essence of Linear Algebra

I struggled so hard with Linear Algebra in college. It felt very byzantine, lousy with "just memorize it," and never once made intuitive sense. Extremely thankful to have come across [this youtube series](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) when I sat down to smooth over the gaps in my knowledge. It's seriously a masterclass in teaching intuitive mathematics and completely illuminated all of the topics I'd had a vague recollection of.

Solid Linear Algebra understanding is paramount to doing good data science and this is an exceptional head start on getting just that.

## GitHub


I don't have a lot to say about this one. If you're going to be working on cool projects, it's a good idea to share them. Furthermore, if you need a tool for something, it's likely already been built. Being literate in how people work in an era of Open Source, and considering what workflows/best practices that you could leverage to bang out cleaner and better-structured projects is crucial.

- I 100% unironically recommend watching [Git for Ages 4 and Up](https://www.youtube.com/watch?v=1ffBJ4sVUb4&t=1s) for a clear illustration of what Git is and how it works.
- From there I checked out [think-like-a-git](http://think-like-a-git.net/) to reinforce what I'd learned.
- Finally I'm using principles I got in [this read](https://www.atlassian.com/git/tutorials/comparing-workflows) to shape the way I'm architecting a Git-based Data Science workflow at QL.
- Git is great. [Here's my GitHub account](https://github.com/napsterinblue) where I'll post every solution that powers the things I write about.

## Learning How to Learn

As I outline in the beginning of my [Trivial Pursuits in Sports and Web Scraping post]({filename}/articles/2017-06-04 trivial pursuits in sports and web scraping.md), things really started clicking for me after taking the free, 4-week [Learning How to Learn Coursera course](https://www.coursera.org/learn/learning-how-to-learn/home/welcome). There's a ton of invaluable information on the way that your brain works and how you can use that understanding to your advantage as you find yourself up against new information.

Additionally, I absolutely swear by [Anki](https://apps.ankiweb.net/), which is a free flashcard software that you can use to keep useful nuggets of information fresh for just minutes a day. A fantastic alternative to the dopamine kicks you get from checking Reddit/Facebook in those brief pockets you find in everyday life.

## Blogs/Websites

I'm certain that it'd take me well over an hour or so to exhaustively find all of the subreddits worth checking out to grow skills relevant to Data Analysis. I've got a couple dozen subscribed on my work account, but I'd say that my big three are:

- [DataIsBeautiful](https://www.reddit.com/r/dataisbeautiful/): A collection of awesome/interesting data visualization projects, more often than not with the code/underlying data used to make them.
- [LearnPython](https://www.reddit.com/r/learnpython/): For when Google/Stack Overflow fails you, and friendlier, in my narrow-ish experience.
- [DailyProgrammer](https://www.reddit.com/r/dailyprogrammer/): Because practice makes perfect. There are a whole host of programming challenges, complete with test cases and a comment section full of clarifying questions and user-submitted solutions. Learned a TON of neat Python tricks seeing some of the clever stuff people come up with.

## Courses

- The [Duke Data Viz in Tableau course](https://www.coursera.org/learn/analytics-tableau) was invaluable when I sat down to learn it. In addition an excellent overview of the tool (and a cool "how much do data jobs actually pay" data set), this course provides some seriously fantastic insight into managing business relationships, the best ways to do up-front due diligence that projects require, and a rough primer into visualization theory that will help you make your data stories come across crystal clear.
- It's in Matlab/Octave (the free Matlab), but [Andrew Ng's Machine Learning course](https://www.coursera.org/learn/machine-learning) is an absolute mainstay in the Data Science community. Great overview of the underpinnings of regressions, Neural Networks, model tuning, ensemble methods, and much more. Took this once a year and some change ago, but am slowly but surely going back through and trying to reimplement the whole thing in Python to solidify my understanding.
- Follow-up to that is [Andrew Ng's Deep Learning course](https://www.coursera.org/specializations/deep-learning). It's all in Python and is a fantastic progression from the basics to deep networks, exploring Convolutional Networks, computer vision, text and sequence models, and many more. Really solid stuff.
- It wasn't very exhaustive, but [Udacity had a really good Intro to Hadoop and MapReduce course](https://classroom.udacity.com/courses/ud617) that really helped me better conceptualize deserializing my code for parallel processing. Have lifted concepts of this code into some of the datasets at work to do some Process Mining, and am excited to get my hands dirty with the whole Big Data ecosystem. This course really turned that light bulb on for me.

## Podcasts

- Data Skeptic: Alternates between digestible explanations of tools and methods and talks with guests within the industry.
- Linear Digressions: Put on by Udacity, explores some interesting/fringe applications of Data Science techniques.
- Not So Standard Deviations: Really enjoy the data-analysis-as-software-development slant that this podcast always champions.
- Partially Derivative: Two dudes drink and banter about Data Science headlines. Very casual, but often just as interesting.
- Talk Python to Me: Very great, in-depth conversations with various project creators in the Python community. Lot of great insight into design decisions and the cultural underpinnings of the Open Source language.

# Tech Talks

There's a whole host of fantastic talks and tutorials scatted throughout the Internet. I'll try and organize my favorites here.

## Must Watch

- [I Don't Like Notebooks](https://www.youtube.com/watch?v=7jiPeIFXb6U&feature=youtu.be): An excellent look at why and how we should be thoughtful of our use of Jupyter Notebooks 
- [Reproducible Analysis in Jupyter Notebooks](https://www.youtube.com/watch?v=_ZEWDGpM-vM): If Joel got you skeptical about notebooks, Jake instructs an awesome design pattern for getting it right

## Excellent Tutorials

- [Pandas from the Ground Up](https://www.youtube.com/watch?v=5JnMutdy6Fw): Every time I've been asked to do a "Python for Data Science" bootcamp, I'm always sure to borrow as much of this tutorial as I can
- [Learning Data Science Using Functional Python](https://www.youtube.com/watch?v=ThS4juptJjQ): Joel Grus writes a bunch of stunt code to demonstrate how to think about Functional Programming and shows how it applies to quickly solving Data Science problems. Rides the line between this header and the next, tbh

## Novel as Hell

- [Discovering Python](https://www.youtube.com/watch?v=RZ4Sn-Y7AP8): David Beazley locks himself in a vault, recreates Git using Python, and becomes a straight-up wizard of an expert wizard in the discovery phase of a software lawsuit
- [MarI/O](https://www.youtube.com/watch?v=qv6UVOQ0F44): No joke, the reason I started down the AI/ML route. Popular YouTuber SethBling teaches an AI to play the first level in Super Mario World
- [Fighting Climate Change with Python](https://www.youtube.com/watch?v=WQkM3ppuhWo): Matt Gordon perfectly demonstrates just how powerful a full-stack Data Scientist can be.

# The Rest

## Movies 

- [2017, stack ranked](https://letterboxd.com/nick_m3blog/list/2017/)
- [2018, stack ranked](https://letterboxd.com/napsterinblue/list/2018/)
- [2019, stack ranked](https://letterboxd.com/napsterinblue/list/2019/)

## YouTube
- [Blind Covers](https://www.youtube.com/channel/UC_sp6oZDuNfTWzZDfwZyJOg) is hands-down the most exciting/inventive thing I've seen on the Internet. They grab a band, give them the lyrics to a song they've never heard before, and then give them an hour to-- completely blind, save for the lyrics-- come up with a cover for a song that's often a wildly-different genre. The host teases out some hilarious banter with the artists, the production value is top notch, and on more than one occasion I've had to throw the covers up on repeat because they were so damn good. I really can't fathom why this channel doesn't have at least 20-30 times the viewers it does...


## Comics

- I'd recommend the Matt Fraction run of Hawkeye to anyone not terribly familiar with comics-- it's a great standalone series. It's got an entire issue dedicated to the dialogue-less adventures of his animal companion, Pizza Dog. Come on, now.
- Invincible is equal parts hyper-violence and quality writing.
- For anyone looking for something weirder, I loved Scud the Disposable Assassin.
- Even weirder yet, check out God Hates Astronauts.

____

# That's All She Wrote (For Now)

<center>{% youtube T1XgFsitnQw %}</center>
