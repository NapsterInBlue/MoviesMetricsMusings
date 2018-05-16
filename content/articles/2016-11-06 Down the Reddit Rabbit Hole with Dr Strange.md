Title: Down the Reddit Rabbit Hole with Dr. Strange
Tags: analysis, data, movies, pandas, python, reddit, scraping

<!-- PELICAN_BEGIN_SUMMARY -->

### Spoiler Alert: this whole post is predicated on the notion that you've seen Dr. Strange already.

So I saw Dr. Strange over the weekend and [really enjoyed it.](https://letterboxd.com/nick_m3blog/film/doctor-strange-2016/)

While I was waiting for post-credit tag **OF WHICH THERE'S TWO**, I ritualistically went to the [discussion thread on Reddit](https://www.reddit.com/r/movies/comments/5b0zni/official_discussion_doctor_strange_spoilers/) to see what other people thought. I should mention that I have a real affinity for Groundhog Day, so when Stephen saves the world by exploiting an abbreviated plot of one of my favorite movies, I was delighted. It didn't take much digging through the thread to find that others did as well.

<center>{% img {filename}/images/strange/strange1.png %}</center>

Pulling from the scene in question, user FilmsAreQuiteAwesome posted

<center>{% img {filename}/images/strange/strange2.png %}</center>

and then shortly thereafter

<center>{% img {filename}/images/strange/strange3.png %}</center>

and then

<center>{% img {filename}/images/strange/strange4.png %}</center>

<!-- PELICAN_END_SUMMARY -->

which of course lead to an even-more extended thread

<center>{% img {filename}/images/strange/strange5.png %}</center>

oh... oh my... It just keeps going.

<center>{% img {filename}/images/strange/strange6.png %}</center>

### Second Spoiler Alert: this goes on for a very long time.

The second tag started and I put my phone away and watched some newly-minted-bad-guy Chiwetel Ejiofor. I grabbed the popcorn and the ladyfriend and rushed home because I had a web-scraper to build-- I was curious to see where this rabbit hole led.

And so in a nutshell, I did the following:

- Start [here.](https://www.reddit.com/r/movies/comments/5b0zni/official_discussion_doctor_strange_spoilers/d9kwuke/?st=iva22lot&sh=4755d655)
- Grab the highest-voted reply containing just the phrase "Dormammu, I've come to bargain"
- Find the the highest-voted reply to that reply containing just the phrase "Dormammu, I've come to bargain"
- Find the the highest-voted reply to that reply containing just the phrase "Dormammu, I've come to bargain"
- Find the the highest-voted reply to that reply containing just the phrase "Dormammu, I've come to bargain"
- Find the the highest-voted reply to that reply containing just the phrase "Dormammu, I've come to bargain"
- Find the the highest-voted reply to that reply containing just the phrase "Dormammu, I've come to bargain"
- Find the the highest-voted reply to that reply containing just the phrase "Dormammu, I've come to bargain"
- Ad nauseum
- All the while grabbing
    - Author
    - Upvote Score
    - Number of Immediate Child Comments
    - What page you're on (relative to the "Continue this thread" clicks)
    - Time of Post
    - The URL of each post
    - Time since the last post
- Toss that into a Pandas DataFrame
- Poke around for a bit
- Write my first blog post in weeks

If you're curious on the how, I've included a link to the Jupyter notebook containing hacky, unambigiously bad code below. If you just want the data (at the time of writing), I've shared that too. Would love some code feedback if anyone's interested!

Ultimately, I wound up following the chain with the highest amount of votes as far as it would take me until I had a table full of data...

<center>{% img {filename}/images/strange/data1.png 800 %}</center>

...over 300 comments long

<center>{% img {filename}/images/strange/data2.png 800 %}</center>

Wow.

The first thing that I noticed is that the number of upvotes that a post received fell off sharply after the user had to click "Continue this thread" after the 9th post

<center>{% img {filename}/images/strange/graph1.png %}</center>

Every 10 posts, the user has to click to go to a new page. The scores drop with each threshold through the fifth page.

<center>{% img {filename}/images/strange/graph2.png %}</center>

And yet another drop after the 100th post, or the 10th click in

<center>{% img {filename}/images/strange/graph3.png %}</center>

The thread between the 100th and 180th posts baffles the hell out of me. Need I remind you, that every comment is an identical "Dormammu, I've come to bargain." What happened at the 151st comment that people were so enthusiastic about? How does any comment have more votes than the one before it????

<center>{% img {filename}/images/strange/graph4.png %}</center>

People are weird.

Next, I filtered down the table to try and get a handle on how much engagement we'd see if we poked around further on down the chain-- how many comments had replies that weren't part of the main chain.

<center>{% img {filename}/images/strange/table1.png 800 %}</center>

On the second page in, I found a series of posts where user YakMan2 tried his damnedest to force the old ["Lisa needs braces!" meme](http://knowyourmeme.com/memes/dental-plan-lisa-needs-braces)

<center>{% img {filename}/images/strange/braces.png %}</center>

After the 22nd post, a user aptly-named ComboBreakerr tried to interrupt chain and promptly failed (as evidenced by his post being voted below the viewing threshold)

<center>{% img {filename}/images/strange/combo.png %}</center>

After the 152nd post, there was a split where two users posted at the same level. There's a large fork in replies here-- the lower half, perhaps material for another blog post someday.

<center>{% img {filename}/images/strange/fork.png %}</center>

Hilariously, after 212 posts (OR 22 PAGES DEEP), user Monolight finds that they can't take it anymore.

<center>{% img {filename}/images/strange/wtf.png %}</center>

Wait a minute

<center>{% img {filename}/images/strange/clone.png %}</center>

Wait what? I grouped each post by that Author field I'd collected and got the counts of the most frequent poster in the chain.

<center>{% img {filename}/images/strange/authors.png %}</center>

lol

I've got no interest in Ken Boning the hell out of this person (and neither should you), but I had to know what was going on in this thread, so I filtered my table down to posts where the username was 'ggalaximm' and got all 185 posts. Here's the top 10. Note the column in the right, which outlines the time since the post just prior to it.

<center>{% img {filename}/images/strange/table2.png 800 %}</center>

From what I can gather, at the beginning of this thread, this person spent a little over a minute reading all of the parent comments before deciding to get in on the fun as the 28th comment. After a couple seconds of hesitation, they realized that nothing was stopping them from whipping up some good ol' copypasta again. And again. And again.

Over the next 50 posts, they had an average CTRL+C, CTRL+V, submit turnaround time of about 10 seconds. But it didn't stop there. I plotted out the sequential number of their post and how long they waited before posting it.

<center>{% img {filename}/images/strange/graph5.png %}</center>

It would appear to me that ggalaximm took 3 breaks over the course of their spree: One for 5 minutes, one for about 4, and one for ~3, for a grand total of about 35 minutes of glorious shitposting.

<center>{% img {filename}/images/strange/break.png %}</center>

After that, the trail goes cold and /u/ggalaximm disappears from the chain.




...Until new challengers appear.



<center>{% img {filename}/images/strange/next.png %}</center>


The Internet is Strange.


Heh. Strange.

[Link to the files](https://github.com/NapsterInBlue/redditDrStrange)
