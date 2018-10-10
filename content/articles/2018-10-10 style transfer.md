Title: Ruff Style Transfer
Tags: viz, light, data science, deep learning

<!-- PELICAN_BEGIN_SUMMARY -->

The last couple months have been blog-dark as I worked through the [Deep Learning Specialization](https://www.deeplearning.ai/courses/) on Coursera. After the first couple courses of fundamentals, we brought some practitioners on site at work to give us a two-day-long bootcamp on a whole range of topics. I've since worked my way through the next couple of courses regarding project structures and computer-vision applications; I also got my computer doing all of my model-training on my GPU (which equals *dramatically-faster* code!).

Getting handy with Deep Learning techniques has been a goal of mine for some time now and so I'm excited to be able to start sharing some of the stuff I'm figuring out!

## Overview

<center>{% img {filename}/images/deep_nets.png %}</center>

This is an alarmingly-reductive representation of what's happening under the hood, but if you're not familiar with Neural Networks/Deep Learning, the idea is that you feed some data in on the left, it comes out on the right with some sort of prediction. Along the way, Data Science™ happens as a result of our model iteratively figuring out the equations to affix to the black lines and blue circles. Provided that we give the program enough data and let it run for a long time, it can "learn" some really interesting behavior.

An interesting application of these techniques is called *Neural Transfer Learning* where basically, we crack open one of these structures, show it two pictures, and let it figure out how to splice the two of them together by borrowing the **Content** from one and **Style** from the other. Some of the more famous examples look like the following:

<center>{% img {filename}/images/style_transfer.png %}</center>
<center>Screenshot taken from Course 4 Week 4 of the Specialization linked above</center>

But this isn't intended to be a tutorial post (that's been expertly done [here](https://medium.com/artists-and-machine-intelligence/neural-artistic-style-transfer-a-comprehensive-look-f54d8649c199) and [here](https://medium.com/tensorflow/neural-style-transfer-creating-art-with-deep-learning-using-tf-keras-and-eager-execution-7d541ac31398)), but instead a look at some of the more ridiculous applications of these techniques I've stumbled into.

<!-- PELICAN_END_SUMMARY -->

## A Dog Day Afternoon

Instead of visiting with friends and playing in the Alumni Marching Band at Michgan last weekend, I spent my Saturday at home sick as hell and tinkering with the [keras deep learning framework.](https://keras.io/). It took awhile to get everything up and running, but once I was set up, I was able to enjoy a "fire-and-forget" model training workflow where I could provide a couple images, then let the program do its thing while I went and napped.

And hey, check it out, it works!


<center>{% img {filename}/images/style_transfer/images/castle.png %}</center>
<center>I took a picture of the castle my best friend got married in</center>


<center>{% img {filename}/images/style_transfer/images/space.png %}</center>
<center>And weighed that against [a really cool painting I found on /r/imaginarylandscapes](https://www.reddit.com/r/ImaginaryLandscapes/comments/8rf9n2/eclipse/)</center>


<center>{% img {filename}/images/style_transfer/output/castle/space_castle_at_iteration_45.png %}</center>
<center>And while the result didn't really mesh whatsoever...</center>

... it was obvious that it was figuring out some sort of way to combine the pink, streaky elements of the second picture, while still preserving the content of the first.

So now that I was capable of using this technique, the question became

>"What's the single-most **impactful** use of this new skill in my toolkit that I can employ *today*?"

<br></br>
<br></br>
<br></br>


### Anyways, Look at My Dog

This is Daisy. She's a goof.

<center>{% youtube YeGAwpZFetY 400 %}</center>

And so I initally set out to see if I could use Style Transfer to punch up a picture this old girl

<center>{% img {filename}/images/style_transfer/images/loaf_daisy.jpg %}</center>

I tried for bombastic

<center>{% img {filename}/images/style_transfer/images/delaware.jpg %}</center>
<center>{% img {filename}/images/style_transfer/output/daisy/loaf_at_iteration_50.png %}</center>

Then stately.

<center>{% img {filename}/images/style_transfer/images/queen.jpg %}</center>
<center>{% img {filename}/images/style_transfer/output/daisy/queen_at_iteration_50.png %}</center>

Finally, I let the algorithm get carried away Miazaki-fying her, lol

<center>{% img {filename}/images/style_transfer/images/totoro.jpg %}</center>
<center>{% img {filename}/images/style_transfer/output/daisy/totoro_at_iteration_50.png %}</center>

Perhaps it had less to do with style transfer, and more to do with starting with a flattering picture.

<center>{% img {filename}/images/style_transfer/images/jedi_daisy.jpg %}</center>
<center>Like this one.</center>

Then apply transfer learning, we do.

<center>{% img {filename}/images/style_transfer/images/yoda.jpg %}</center>
<center>{% img {filename}/images/style_transfer/output/daisy/daisy_yoda_at_iteration_50.png %}</center>

Or this one

<center>{% img {filename}/images/style_transfer/images/happy_daisy.jpg %}</center>

What if we decide that she should look more like a snow leopard?

<center>{% img {filename}/images/style_transfer/images/snow_leopard.png %}</center>
<center>{% img {filename}/images/style_transfer/output/daisy/daisy_bigcat_at_iteration_50.png %}</center>

And so this was certainly amusing for awhile.

But what if it was weirder?

## Unleash THE_PACK

Before we launch into this next section, I feel it bears a quick bit of explanation for friends out there that spend less time indoors than I do.

### Rules of the Road

[/r/THE_PACK](https://www.reddit.com/r/THE_PACK/) (NSFW) is a funny corner of Reddit where nearly 100k subscribers are all rallied around the same, ironic in-joke.

At its core, the entire sub is sarcastically derivative of the kind of machismo, curse-word laden, skeleton-bearing images like you might see on shirts like this

<center>{% img {filename}/images/style_transfer/images/origin.png %}</center>

But often lousy with Early 2000s-era Microsoft Office WordArt...

<center>{% img {filename}/images/style_transfer/images/cats_dogs.jpg %}</center>

...about hysterically-specific things...

<center>{% img {filename}/images/style_transfer/images/almond_milk.png %}</center>

...written from the persona of an edgy middle-schooler who's *just* getting the hang of computers and swear words.

<center>{% img {filename}/images/style_transfer/images/ipad.png %}</center>

They're occasionally pretty wholesome...

<center>{% img {filename}/images/style_transfer/images/step_son.png %}</center>

...and almost always steeped in irony.

<center>{% img {filename}/images/style_transfer/images/irony.png %}</center>

<br></br>

But that's the long-and-short of it. It's genuinely one of my favorite subreddits. If this isn't the funniest thing you've seen all day, I don't know what to tell you.

<center>{% img {filename}/images/style_transfer/images/shoes.png %}</center>


### An Unholy Marriage

So naturally, I was going to Style Transfer THE_PACK. I took to [/r/aww](https://www.reddit.com/r/aww) to find some prime, dog-shaped candidates.

<center>{% img {filename}/images/style_transfer/images/pack3.png %}</center>
<center>{% img {filename}/images/style_transfer/images/book_smart.png %}</center>
<center>{% img {filename}/images/style_transfer/output/the_pack/pack2_booksmart_at_iteration_100.png %}</center>

<center>{% img {filename}/images/style_transfer/images/pack2.png %}</center>
<center>{% img {filename}/images/style_transfer/images/sunchips.jpg %}</center>
<center>{% img {filename}/images/style_transfer/output/the_pack/pack3_sunchips_at_iteration_100.png %}</center>

<center>{% img {filename}/images/style_transfer/images/pack1.png %}</center>
<center>{% img {filename}/images/style_transfer/images/trevor.png %}</center>
<center>{% img {filename}/images/style_transfer/output/the_pack/pack1_trevor_at_iteration_500.png %}</center>
<center>True riders of THE_PACK will be as excited as I was to see "Rocco" turn into a ROOOO </center>


## Bonus: Simpsons Couch Gags

I was outlining the premise of this post to someone earlier and after the initial wave of confusion, they offered that it might be interesting to try and generate some variations on the classic couch gag.

<center>{% youtube T5vuzfdmsDo 400 %}</center>
<center>This one stands out as one of my more memorable favorites.</center>

And so we start with a base image

### The Good

<center>{% img {filename}/images/style_transfer/images/banksy.jpg %}</center>
<center>{% img {filename}/images/style_transfer/output/simpsons/banksy_at_iteration_50.png %}</center>


<center>{% img {filename}/images/style_transfer/images/psychadelic.jpg %}</center>
<center>{% img {filename}/images/style_transfer/output/simpsons/psychadelic_at_iteration_50.png %}</center>

<center>{% img {filename}/images/style_transfer/images/takeonme.jpg %}</center>
<center>{% img {filename}/images/style_transfer/output/simpsons/takeonme_at_iteration_50.png %}</center>

<center>{% img {filename}/images/style_transfer/images/tattoo.jpg %}</center>
<center>{% img {filename}/images/style_transfer/output/simpsons/tattoo_at_iteration_50.png %}</center>

<center>{% img {filename}/images/style_transfer/images/up.jpg %}</center>
<center>{% img {filename}/images/style_transfer/output/simpsons/up_at_iteration_50.png %}</center>


### The Bad


<center>{% img {filename}/images/style_transfer/images/batman.jpg %}</center>
<center>{% img {filename}/images/style_transfer/output/simpsons/batman_at_iteration_50.png %}</center>

<center>{% img {filename}/images/style_transfer/images/dali.jpg %}</center>
<center>{% img {filename}/images/style_transfer/output/simpsons/dali_at_iteration_50.png %}</center>

<center>{% img {filename}/images/style_transfer/images/south_park.jpg %}</center>
<center>{% img {filename}/images/style_transfer/output/simpsons/south_park_at_iteration_50.png %}</center>

<center>{% img {filename}/images/style_transfer/images/spongebob.jpg %}</center>
<center>{% img {filename}/images/style_transfer/output/simpsons/spongebob_at_iteration_50.png %}</center>



### ...the Hell is That??


<center>{% img {filename}/images/style_transfer/images/buscemi.jpg %}</center>
<center>{% img {filename}/images/style_transfer/output/simpsons/buscemi_at_iteration_300.png %}</center>



______

All blundering aside, I hope that if you made it this far down you enjoyed reading. [Here's a link to the repository that I used to put everything together](https://github.com/NapsterInBlue/Academy-Awards), including the raw box office data that I spent a day getting at-- [hit me up on Twitter](https://twitter.com/NapsterInBlue) if you wind up doing anything cool with it!

Cheers,

-Nick

