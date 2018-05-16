Title: for frame in movie: make_bars()
Tags: data, movies, python, viz

<!-- PELICAN_BEGIN_SUMMARY -->

[Related mood music (see below)](https://www.youtube.com/watch?v=GI6CfKcMhjY). Revisited this one for the first time in a long while today and have been listening to it on repeat while I typed up this blog.

**Total Plays at the Time I Hit Publish: 21**

Anyhow, I stumbled across a wildly amusing Reddit thread a couple years ago where a user had basically:

- Got ahold of various movies through one mean or another
- Went through and calculated the average color in each frame
- Used those values to make a bunch of vertical bars that mapped the progression of color through the movie

[Check it out. It's pretty cool.](https://imgur.com/gallery/Pw6LD/)

The Internet has taken to calling these Movie Bar Codes (which drives the pedant in me insane, lol) and other users have some pretty cool galleries of their takes on the project. One of my favorites is a [tumblr user whose been cranking out dozens of them](http://moviebarcode.tumblr.com/), with a grainier, hand-brushed aesthetic. So I bookmarked the links into my "would be cool to do" folder, then totally forgot about it.

<center>{% img {filename}/images/moviebars/jackmkv.png 700 400 %}</center>
<center>**The Jack Sparrow music video:** Look at how starkly that first Jack Sparrow scene pops at the first white bar, lol</center>


<!-- PELICAN_END_SUMMARY -->

## Fast Forward


And so a couple years go by, and [another album](https://imgur.com/a/pfJ8N) hits it big on the movies subreddit. I remember how much I wanted to take a crack at doing this myself-- after all I've learned a hell of a lot of Python between then and now-- and lo and behold, [someone shows up in the comments with some relevant Python code. Nice.](https://www.reddit.com/r/movies/comments/6ce2df/the_average_color_of_every_frame_of_a_given_movie/dhu8otu/)

And so I pull it down from GitHub and try and throw it up against an episode of Detroiters, which I loved and you should totally check out, and I botched the hell out of it. First off, it took longer than the runtime of the episode to compile, and when it was finished, the image was so big that I couldn't open it in any of the software on my computer. Bummer.

But the cool thing about living in the future is that you can just talk to strangers on the Internet until you suck less, [which is precisely what I did](https://www.reddit.com/r/movies/comments/6ce2df/the_average_color_of_every_frame_of_a_given_movie/dipd3om/?context=3). Huge thanks to /u/flashman for playing along. Basically, the code he'd hosted needed some love/tweaking before someone could use it in the way I was intending (hosted my changes at the bottom of this post!). My blundering was twofold:

1. I had no idea what the video resolution was (nor did I understand exactly how those arguments were working), so I was telling it to ingest a file several times smaller than it actually was.
2. I was grabbing and drawing a bar for every single frame. Let's do some napkin math.
- The episode in question was about 24 minutes. So that's **1440 seconds**
- Then consider the fact that the show is filmed at 24 Frames per Second; **34,560** frames.
- Finally, by telling it to read the episode as if it were, idk, ~320x240 resolution, not the 1280x720 that it was, multiply that by 10 or so.

Go figure my computer was giving me grief about trying to open up a 345,600x720 image.

## Under the Hood


[I love the way /u/flashman explain how this works](http://timbennett.github.io/movie-barcodes/)-- check it out, I'll wait here.

But from an implementation standpoint here's an overview of what's going on:

- FFMPEG gets pointed at a video file and chunks it into all of its component frames.
- Because we tell the script the width, height, and length of the video it breaks the images into their vector representations.
    - After all, each frame has dimensions width x height x 3, where the 3 represents the RGB values in each pixel. That's a lot, right?
- Then, using the above, it calculates the average RGB values and assigns that average color to the frame for later use.
- Using this list of average RGBs, it makes a blank white image and then, left to right, colors in the bars.

And that's the long-and-skinny of it. But what of the comically-long width issue I was having? The answer was obviously some good old-fashioned mod division.

For the uninitiated, mod division is a $2 Computer Science term that we all learned back before we did long division. Recall that if we took, say, 53 / 6, it'd divide neatly 8 times, before leaving us remainder 7. Well mod division (53 % 6) would simply output that 7.

This is super useful when we want to construct an "Every nth frame" scheme, because all you have to do is take the total number of frames, and only draw a line where (frameIndex % nthFrame == 0). This nthFrame value becomes a lever that we can adjust to determine the final width of our dimensions. Which is basically what I wound up doing.

## Now We're Cooking


Hard part out of the way, this is where I got to start having fun with it. My ideal final product was a 4096x2160 (standard 4k resolution) image, so making that happen was a two-step process:

- Get the movie. Ez pz.
- The following napkin math
    - Fire up the movie in VLC and hit CTRL+J to get the video metadata I was interested in.
    - Write down the video width and height
    - Convert the Hour:Minutes:Seconds into seconds
    - Multiply that runtime by Frames per Second to get total frames
    - Algebra: To get 4096 bars, we want to grab every _______ frames. This was the value, rounded to the nearest whole number, I'd pipe in as `nthFrame`

## Gallery

Historically-speaking, there's about a 600 year gap between **Gladiator** and **300**, but I thought it would be interesting to compare the two.

<center>{% img {filename}/images/moviebars/Gladiatoravi.png 700 400 %}</center>
<center>**Gladiator**: Was really surprised by how much the blues stood out. I only really remember the sunburnt Colosseum scenes.</center>

<center>{% img {filename}/images/moviebars/300mkv.png 700 400 %}</center>
<center>**300**: I anticipated a lot of red. The Spartan capes really stand out in memory, but alas, on average, we've got the standard Snyder, gritty palette.</center>

Wait, what about a movie famous for it's lack of color? [Sin City](http://www.imdb.com/title/tt0401792/) was all in black and white, save for a few objects/characters that are vibrant shades of electric yellow and deep red. Maybe that would show up?

<center>{% img {filename}/images/moviebars/sinmkv.png 700 400 %}</center>
<center>**Sin City**: Hell yes it does!</center>

I fired off some context-less texts-- "Hey, what's your favorite movie?"

<center>{% img {filename}/images/moviebars/sunshinemkv.png 700 400 %}</center>
<center>**Eternal Sunshine of the Spotless Mind**: Soul-crushing movie, decidedly gorgeous palette.</center>

<center>{% img {filename}/images/moviebars/scottmkv.png 700 400 %}</center>
<center>**Scott Pilgrim vs the World**: Love how glaringly obvious the bright-white techno ghost-dragon sequence stands out near the end.</center>

<center>{% img {filename}/images/moviebars/fifthmkv.png 700 400 %}</center>
<center>**The Fifth Element:** Might be my favorite render to come out of this whole thing. What an awesome spattering of color.</center>

Lastly, I remember [this awesome read from awhile back](https://screenmuse.wordpress.com/2012/11/03/colour-symbolism-red-in-the-sixth-sense/) that called out the importance of the color red in the Sixth Sense as a foreshadowing element. A number of times throughout the movie, when the screen is saturated with the color, a vision of a dead person is soon to follow.

<center>{% img {filename}/images/moviebars/sixthmkv.png 700 400 %}</center>
<center>**The Sixth Sense:** The double-bars at the ~2/3 mark are the following:</center>

<center>{% img {filename}/images/moviebars/sixth1.PNG 700 400 %}</center>

<center>{% img {filename}/images/moviebars/sixth2.PNG 700 400 %}</center>

And then the slow ban through the tent to the dead girl sitting across him vomiting in horror. Scared the hell out of me when I was a kid. Still does, lol.

## What Next?


I've spitballed this project to a few friends as it's progressed over the past few weeks. A lot of good reception and egging me on to check out this movie or that-- but like, twist my arm, this stuff is super cool to me. A few times I've gotten "You know, you could make some money doing this!" And for sure, [people do](https://www.redbubble.com/people/moviebarcode/portfolio), but then it feels like work, ya know? I'm just really excited that I thought this was cool a couple of years ago and have figured out how to to it myself.

But you'd better believe that this is high on my list of Birthday/Christmas/Just Because gift ideas.

In terms of script improvements, I was getting pretty tired of doing the VLC poking a looked into a way to procedurally get the metadata so I didn't have to manually pass it in when I'd run the script. If I could do that, I'd be able to just point it at a folder full of movies, fire off the job, and come back to a bunch of cool, near-effortless data art.

Alas, I found some Python methods to get at this stuff, but couldn't, for the life of me, get it to work correctly/consistently. For some files, it just wouldn't recognize any runtime at all, which is a downright crucial part of calculating the nthFrames parameter. And it wasn't specific to file formats-- it would work for some mkv's but not others, avis were typically good, but mp4 was also hit or miss. Before I knew it, I had spent 3 hours spinning my wheels and it dawned on me that I wasn't nearly as interested in continuing work on this as I was when I'd started. Had a real Rick moment and started writing this post before I lost interest in doing even that.

<center>{% youtube cPEnRb6aaS4 %}</center>

Finally, my motivation for getting my hands dirty with this in the first place is to check out what the Cornetto Trilogy looked like. Hot Fuzz is my favorite movie of all time. Love the other two. Toss in Scott Pilgrim (pictured above) for good measure.

<center>{% img {filename}/images/moviebars/shaunmkv.png 700 400 %}</center>
<center>**Shaun of the Dead**</center>

<center>{% img {filename}/images/moviebars/hotfuzzmkv.png 700 400 %}</center>
<center>**Hot Fuzz**</center>

<center>{% img {filename}/images/moviebars/worldendmkv.png 700 400 %}</center>
<center>**The World's End**</center>

Gonna get some stretched canvas prints and hang them together in my living room. Will update the post with pictures when they come in!

**Update: Thrilled with how these turned out.**

<center>{% img {filename}/images/moviebars/edgarwright.png 700 400 %}</center>

As always, [GitHub link](https://github.com/NapsterInBlue/movie-barcodes) if anyone's interested in tinkering themselves.
