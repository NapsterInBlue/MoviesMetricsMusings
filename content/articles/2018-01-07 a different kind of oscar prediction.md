Title: A Different Kind of Oscar Prediction
Tags: meta, movies, python, scraping, viz

<!-- PELICAN_BEGIN_SUMMARY -->

I sat down the other day to start piecing together a tentative "Best of 2017" list. It's been a busy year and I didn't get around to seeing everything that I'd meant to, and it occurred to me that making such a list before seeing like a dozen good movies feels like a miss. Which isn't really a huge issue-- most of the gaps in my watchlist have only just started screening near me. Still, the question remained of "what sort of arbitrary deadline was I going to hold myself to?"

To that end, it felt like the Academy Awards were probably a good a cutoff point as any. But when are those again? I checked out their site and turns out they're on March 4th this year. Which was a lot earlier than I would have guessed. They must be getting ready to announce nominees soon.

# So When?

I thought it'd be a fun, dumb little exercise in making an educated, data-driven guess. So I took to all of the various Wikipedia pages and started manually tabulating historical announcement and award show dates by year, going back to 1990.

<!-- PELICAN_END_SUMMARY -->

## Day of Week

First, I tried narrowing it down by day of week announced. And by the looks of it, they only really announce on Tuesday, Wednesday, and Thursday.

<center>{% img {filename}/images/oscars1/dayofweek.PNG %}</center>

for award shows on Sunday and Monday.

<center>{% img {filename}/images/oscars1/dayofweekshows.PNG %}</center>

A bit more digging would reveal that they actually haven't announced on a Wednesday since 1993, so that's out.

<center>{% img {filename}/images/oscars1/nowed.PNG %}</center>

## Days Before Show

Next, I wanted to get an idea of how many days typically span the time between announcement and award show.

<center>{% img {filename}/images/oscars1/ddiff.PNG %}</center>

So about 38, plus or minus 4.

## Survey Says

So, equipped with these two nuggets of information and the 3/4/18 show date, I did a bunch of date checking. Ultimately, it turns out that 3 dates meet that criteria:

- Tues, Jan 23rd, 40 days before
- Thurs, Jan 25th, 38 days before
- Tues, Jan 30th, 33 days before

# Estimating Visually

I had a list of announcement and show dates, but thought it useful to try and visualize them to make a more educated guess. I plotted out each year to see if there was any visual pattern that would help inform my guess.

<center>{% img {filename}/images/oscars1/byyearblank.PNG 600 %}</center>

Wait, what?

<center>{% img {filename}/images/oscars1/byyear1.PNG 600 %}</center>
<center>Did someone forget to set their alarm clock in 2009?</center>

A bit of wikipedia digging would reveal that between 2008 and 2009, they nominated 10 movies for Best Picture-- twice what it'd been for decades beforehand. Not certain that that's the definite cause, but was interesting nevertheless.

<center>{% img {filename}/images/oscars1/byyear2.PNG 600 %}</center>
More wiki-ing, there was a whole section in the page for the 2003 awards outlining how "in light of the record low viewership from the preceeding year's ceremony," the Academy was seeking to make several changes, including a new producer and moving the ceremony up a month.

## How Were the Ratings?

This was easy enough information to get, if tedious. Each award page has viewer ratings up in the corner, so marrying them with my existing dataset was as straight-forward as adding a new column to my .csv and updating records.

What I saw surprised me.

<center>{% img {filename}/images/oscars1/nielsen.PNG 600 %}</center>

I didn't follow the Oscars whatsoever until 2014. I was on Spring Break with a group of friends and we spent one of our nights watching that year's show. At that point, the only movie I'd seen from the entire line up was Gravity and thus spent the whole show arbitrarily rooting for it to win (which turned out to be a decent-enough strategy, given that it took home 7 of the 10 it was nominated for). Looking back, I don't remember a ton about the show besides the [absurdly popular Ellen selfie](https://twitter.com/theellenshow/status/440322224407314432?lang=en), John Travolta butchering Idina Menzel's name, a Leo "snub" that I was only really aware of for the meme, and Matthew McConaughey giving us an "Alright, alright, alright" in his acceptance speech.

And so once more, I found myself combing through Wikipedia articles trying to pin an underlying story to the data:

- With the exception of 1997 (the year Titanic became the highest-grossing Best Picture winner ever), 1990 to 2000 was characterized by on-and-off-again success trying out a handful of hosts, themes, and production crews. The low point in '96 is, in part, attributed to lethargic hosting and viewers checking out in boredom while The English Patient cleaned house (9 wins over 12 nominations).
- The 2001 and 2002 shows (airing in 2002 and 2003 respectively) both have sections on their pages that pin a level of causation to 9/11 and the War in Iraq.
- Curiously, they've hired a guy named Gil Gates to produce 14 of the shows between 1990 and 2008, and it seems like more often than not when they do, it winds up being worse than the year before it. For instance, after record-low viewership for the 2002 show, they brought in a totally new production crew and moved the date of the show up a month. Large viewer bump. Then they bring Gil back the next year (drop), the next year (drop), skip a year (up), and then one last time (big drop). Weird.
- Hugh Jackman hosts in 2009 and Dan Harmon, Rob Schrab (of my favorite comic *Scud: The Disposable Assassin* fame), and Jean-Ralphio pick up an Emmy for writing him an excellent opening number. Things are good for a few years.
- The 2014 and 2015 pages heavily cite social consciousness as a reason for declining viewership. Both years went 40 for 40 nominating white actors for best performance categories. 2015 has a section where they discuss the movie Carol (wherein two women fall in love in the 50s) and how its lack of a nod might be a sign of the Academy's indifference to the LGBT community.

And if that were the whole explaining factor, you'd think that 2016 would be a turnaround year. The Best Picture winner was, ironically, about a gay, black man's journey through life. Mahershala Ali became the first Muslim to win an acting Oscar that year. Best Documentary wound up going to a series examining systemic racism in America against the backdrop of a high-profile murder. Viola Davis won Best Supporting Actress and gave, for my money, one of the best acceptance speeches in the history of the show.

<center>{% youtube YHTXbGG68T8 %}</center>

But then 2016 came in even lower than the years proceeding it. I think consciousness and accountability played a large part in the decline, sure, but don't think that's the whole picture. Even at it's best in the last decade, the show still struggles to compete with pre-Internet era viewership. Because frankly, 3 1/2 - 4 hours is a long time to sit through commercials and hit-or-miss gags. Especially when I can go to any number of sites the next day and get the highlights that I'm watching the show for in the first place.

Hell, I keep a blog that has the word "movies" in the title and spend more time than I care to admit writing about them and even I'm not watching the damn show. Sure, I watched in 2014. But every year since, I didn't. It was totally off my radar in 2015. I spent the entirety of the show in 2016 watching Superbad with friends and occasionally refreshing a Reddit thread with live updates. Last year, I went and saw Get Out and got home just in time to watch the Moonlight/La La Land debacle (which perfectly satisfied my indecision between which of the two I thought would win).

So if you find yourself thinking "What's the Academy's goal in creating an award show?" and your best guess is "To put butts in seats, watching their program" then you might reconsider. They're hardly nailing it in the digital age. As far as a announcement prediction goes, you might look at the trend of declining viewership over the past five years, and expect the same "move the show up a month" maneuver that worked once for them. But recall that the March 3rd show date is already on the books. So where does that leave us?

# Zeroing in on a Prediction


I'd narrowed down my best guess at the 2017 nomination announcement to three dates.

- Tues, Jan 23rd
- Thurs, Jan 25th
- Tues, Jan 30th

But before I was going to make any sort of guess, I wanted to get an intuition for how the Academy was behaving over the past couple decades. In doing so, I found myself stumped at the seemingly-erratic jumps in their announcement and award show dates, particularly in the last twenty years or so. Digging in, some of the movement was deliberately ratings-based, but more interestingly, later jumps coincided with the expansion of movies considered for their coveted award.

<center>{% img {filename}/images/oscars1/byyear3.png 600 %}</center>

Maybe that thread's worth pulling. If the show itself isn't doing so hot in recent years, maybe they're achieving something else behind the scenes. Otherwise, why continue doing the show? I found myself asking "What's the relationship between the Academy Awards and the movies that it promotes?"


So obviously I spent my New Year's Day scraping weekly box office info on nearly 30 years worth of Best Picture Nominees.

<center>{% img {filename}/images/oscars1/theaterruns.PNG 600 %}</center>

# To Be Continued
Have already done a good deal of digging into this-- I'm pretty excited about the things I've been finding and am writing the follow up this week. [Follow me on Twitter](https://twitter.com/NapsterInBlue) if you're mildly amused at this point and care to go off the deep end with me.

Otherwise, as always, here's the [link to the repository I used to whip together this post.](https://github.com/NapsterInBlue/Academy-Awards)

Til next time!

-Nick

# ...Sort Of
Welp. This post was live for a whole 15 minutes when I learned that this was [wholesale Google-able information.](https://deadline.com/2017/04/oscars-2018-airdate-abc-academy-awards-dates-1202061171/)

<center>¯\\\_(ツ)\_/¯</center>

Oh well. Time to lose this "predict the date" angle. Still a lot of good stuff in the next post!
