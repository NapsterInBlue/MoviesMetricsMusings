Title: Ruff Style Transfer
Tags: viz, light, data science, deep learning

<!-- PELICAN_BEGIN_SUMMARY -->

The last couple months have been blog-dark as I worked through the [Deep Learning Specialization](https://www.deeplearning.ai/courses/) on Coursera. After the first couple courses of fundamentals, we brought some practitioners on site at work to give us a two-day-long bootcamp on a whole range of topics. I've since worked my way through the next couple of courses regarding project structures and computer-vision applications; I also got my computer doing all of my model-training on my GPU (which equals *dramatically-faster* code!).

Getting handy with Deep Learning techniques has been a goal of mine for some time now and so I'm excited to be able to start sharing some of the stuff I'm figuring out.

## Overview

<center>{% img {static}/images/deep_nets.png %}</center>

This is an alarmingly-reductive representation of what's happening under the hood, but if you're not familiar with Neural Networks/Deep Learning, the idea is that you feed some data in on the left, it comes out on the right with some sort of prediction. Along the way, Data Science™ happens as a result of our model iteratively figuring out the equations to affix to the black lines and blue circles. Provided that we give the program enough data and let it run for a long time, it can "learn" some really complex behavior.

An interesting application of these techniques is called *Neural Style Transfer* where basically, we crack open one of these structures, show it two pictures, and let it figure out how to splice the two of them together by borrowing the **Content** from one and **Style** from the other. Some of the more famous examples look like the following:

<center>{% img {static}/images/style_transfer.png %}</center>
<center>Screenshot taken from Course 4 Week 4 of the Specialization linked above</center>

But this isn't intended to be a tutorial post (that's been expertly done [here](https://medium.com/artists-and-machine-intelligence/neural-artistic-style-transfer-a-comprehensive-look-f54d8649c199) and [here](https://medium.com/tensorflow/neural-style-transfer-creating-art-with-deep-learning-using-tf-keras-and-eager-execution-7d541ac31398)). Instead let's look at some of the more ridiculous applications I've stumbled into!

<!-- PELICAN_END_SUMMARY -->

## A Dog Day Afternoon

Instead of visiting with friends and playing in the Alumni Marching Band at Michgan last weekend, I spent my Saturday at home sick as hell and tinkering with the [keras deep learning framework.](https://keras.io/) It took awhile to get everything up and running, but once I was set up, I was able to enjoy a "fire-and-forget" model training workflow where I could provide a couple images, then let the program do its thing while I went and napped.

And hey, check it out, it works!

I took a picture of the castle my best friend got married in and weighed that against [a really cool painting I found on /r/imaginarylandscapes](https://www.reddit.com/r/ImaginaryLandscapes/comments/8rf9n2/eclipse/)

<br></br>
<center>{% img {static}/images/style_transfer/combinations/castle_space.png %}</center>

<br></br>
And while the result didn't really mesh whatsoever...

<br></br>
<center>{% img {static}/images/style_transfer/output/castle/space_castle_at_iteration_45.png %}</center>
<br></br>

... it was obvious that it was figuring out some sort of way to combine the pink, streaky elements of the second picture, while still preserving the content of the first.

So now that I was capable of using this technique, the question became

>"What's the single-most **impactful** use of this new skill in my toolkit that I can employ *today*?"

<br></br>
<br></br>
<br></br>


### Anyways, Look at My Dog

<br></br>
This is Daisy. She's a goof.

<br></br>
<center>{% youtube YeGAwpZFetY 400 %}</center>
<br></br>

I initally set out to see if I could use Style Transfer to punch up a picture this old girl.

<br></br>
<center>{% img {static}/images/style_transfer/images/loaf_daisy.jpg %}</center>
<br></br>

I tried for bombastic.

<br></br>
<center>{% img {static}/images/style_transfer/combinations/bombastic.png %}</center>
<br></br>

Then stately.
<br></br>
<center>{% img {static}/images/style_transfer/combinations/stately.png %}</center>
<br></br>

Finally, I let the algorithm get carried away Miazaki-fying her.

<br></br>
<center>{% img {static}/images/style_transfer/combinations/totoro.png %}</center>
<br></br>
<br></br>

### A More Earnest Attempt

Perhaps it had less to do with style transfer, and more to do with starting with a flattering picture.

<br></br>
<center>{% img {static}/images/style_transfer/images/jedi_daisy.jpg %}</center>
<center>Like this one.</center>
<br></br>

Then apply Style Transfer, we do.

<br></br>
<center>{% img {static}/images/style_transfer/combinations/yoda.png %}</center>
<br></br>

Or this one.

<br></br>
<center>{% img {static}/images/style_transfer/images/happy_daisy.jpg %}</center>
<br></br>

What if we decide that she should look more like a snow leopard?

<br></br>
<center>{% img {static}/images/style_transfer/combinations/leopard.png %}</center>
<br></br>

And so this was certainly amusing for awhile.

But what if it was weirder?

## Unleash THE_PACK

Before we launch into this next section, I feel it bears a quick bit of explanation for friends out there that spend less time indoors than I do.

### Rules of the Road

[/r/THE_PACK](https://www.reddit.com/r/THE_PACK/) (NSFW) is a funny corner of Reddit where nearly 100k subscribers are all rallied around the same, ironic in-joke.

At its core, the entire sub is sarcastically derivative of the kind of machismo, curse-word laden, skeleton-bearing images like you might see on shirts like this

<center>{% img {static}/images/style_transfer/images/origin.png %}</center>

But often lousy with Early 2000s-era Microsoft Office WordArt...

<center>{% img {static}/images/style_transfer/images/cats_dogs.jpg %}</center>

...about hysterically-specific things...

<center>{% img {static}/images/style_transfer/images/almond_milk.png %}</center>

...written from the persona of an edgy middle-schooler who's *just* getting the hang of computers and swear words...

<center>{% img {static}/images/style_transfer/images/ipad.png %}</center>

...and living out power fantasies, sharing the thoughts that they can't in real life.

<center>{% img {static}/images/style_transfer/images/gordon.png %}</center>


They're occasionally pretty wholesome...

<center>{% img {static}/images/style_transfer/images/step_son.png %}</center>

...and almost always steeped in irony.

<center>{% img {static}/images/style_transfer/images/irony.png %}</center>

<br></br>

But that's the long-and-short of it. It's genuinely one of my favorite subreddits. If this isn't the funniest thing you've seen all day, I don't know what to tell you.

<center>{% img {static}/images/style_transfer/images/shoes.png %}</center>
<br></br>

### An Unholy Marriage

So naturally, I was going to Style Transfer THE_PACK. I took to [/r/aww](https://www.reddit.com/r/aww) to find some prime, dog-shaped candidates.


First off, I spied this good boy on a shopping trip and elected to pair him against a needlessly-anthropomorphic dragon with a dash of spelling error.

<br></br>
<center>{% img {static}/images/style_transfer/combinations/pack_1.png %}</center>
<br></br>

I think my favorite thing about how this turned out is that the font on the cart handle adopted the gross, block lettering from its counterpart.

<br></br>
<center>{% img {static}/images/style_transfer/output/the_pack/pack2_booksmart_at_iteration_100.png %}</center>
<br></br>


I was much more excited to run this next one if for the diversity in color/letter style alone.

<br></br>
<center>{% img {static}/images/style_transfer/combinations/pack_2.png %}</center>
<br></br>

And boy did it deliver, lol

<br></br>
<center>{% img {static}/images/style_transfer/output/the_pack/pack3_sunchips_at_iteration_100.png %}</center>
<br></br>


Finally, I paired this cute pup in surgery recovery with, perhaps, my favorite post on the whole subreddit.

<br></br>
<center>{% img {static}/images/style_transfer/combinations/pack_3.png %}</center>
<br></br>
<br></br>
I set it up to run 1000 iterations and then went to bed.
<br></br>
<br></br>
And woke up to a beautiful disaster.
<br></br>
<br></br>
<br></br>
<center>{% img {static}/images/style_transfer/output/the_pack/pack1_trevor_at_iteration_500.png %}</center>
<center>True riders of THE_PACK will be as excited as I was to see "Rocco" turn into a ROOOO </center>
<br></br>

And that was the brunt of what I intended to share.


## Bonus: Simpsons Couch Gags

But then I was outlining the premise of this post to someone earlier and after the initial wave of confusion, they offered that it might be interesting to try and generate some variations on the classic couch gag.

<center>{% youtube T5vuzfdmsDo 400 %}</center>
<center>This one stands out as one of my more memorable favorites.</center>

Why, yes it would.

<br></br>
### Doing It

So we start with a base image

<center>{% img {static}/images/style_transfer/images/simpsons.png %}</center>

And we spend our Work From Home Day doing actual work on the laptop, while periodically firing off

```
python transfer.py images/simpsons.png images/some_garbage.png --iter=100
```

and returning to results of... mixed quality.

### The Good


I started off with [that Banksy piece that's been in the news this week](https://www.reddit.com/r/pics/comments/9lssan/banksys_girl_with_balloon_shreds_itself_after/?st=jn50kdei&sh=9c88f906) and it turned out pretty great.

<br></br>
<center>{% img {static}/images/style_transfer/images/banksy.jpg %}</center>
<br></br>
<center>{% img {static}/images/style_transfer/output/simpsons/banksy_at_iteration_50.png %}</center>
<br></br>


I'd seen other projects have a lot of success transferring psychedelic-style art, so it came as little surprise when it worked well here.

<br></br>
<center>{% img {static}/images/style_transfer/images/psychadelic.jpg %}</center>
<br></br>
<center>{% img {static}/images/style_transfer/output/simpsons/psychadelic_at_iteration_50.png %}</center>
<br></br>


So did a still from the Take On Me music video.

<br></br>
<center>{% img {static}/images/style_transfer/images/takeonme.jpg %}</center>
<br></br>
<center>{% img {static}/images/style_transfer/output/simpsons/takeonme_at_iteration_50.png %}</center>
<br></br>


And the design document for my tattoo, courtesy of [Johnny Andres](https://www.instagram.com/johnnyandres/)

<br></br>
<center>{% img {static}/images/style_transfer/images/tattoo.jpg %}</center>
<br></br>
<center>{% img {static}/images/style_transfer/output/simpsons/tattoo_at_iteration_50.png %}</center>
<br></br>


But I think the house from *Up* wound up being my favorite result.

<br></br>
<center>{% img {static}/images/style_transfer/images/up.jpg %}</center>
<br></br>
<center>{% img {static}/images/style_transfer/output/simpsons/up_at_iteration_50.png %}</center>
<br></br>


### The Bad

I think the **DEEAAAAAAAD** looked similar-enough to Marge's necklace next to the top of Lisa and Maggies' hair that it caused their faces to bleed together.

<br></br>
<center>{% img {static}/images/style_transfer/images/batman.jpg %}</center>
<br></br>
<center>{% img {static}/images/style_transfer/output/simpsons/batman_at_iteration_50.png %}</center>
<br></br>

Dali blurred everything. Go figure.

<br></br>
<center>{% img {static}/images/style_transfer/images/dali.jpg %}</center>
<br></br>
<center>{% img {static}/images/style_transfer/output/simpsons/dali_at_iteration_50.png %}</center>
<br></br>


Apparently South Park is a show about everything melting.

<br></br>
<center>{% img {static}/images/style_transfer/images/south_park.jpg %}</center>
<br></br>
<center>{% img {static}/images/style_transfer/output/simpsons/south_park_at_iteration_50.png %}</center>
<br></br>


And the essence of Spongebob Squarepants is a downright-Lovecraftian number of eyeballs.

<br></br>
<center>{% img {static}/images/style_transfer/images/spongebob.jpg %}</center>
<br></br>
<center>{% img {static}/images/style_transfer/output/simpsons/spongebob_at_iteration_50.png %}</center>
<br></br>


### ...the Hell is That??


Finally, I fed it this picture of Steve Buscemi for about an hour, because why not?

<center>{% img {static}/images/style_transfer/images/buscemi.jpg %}</center>
<br></br>
<center>{% img {static}/images/style_transfer/output/simpsons/buscemi_at_iteration_300.png %}</center>
<br></br>

And if you stare at this like a [Magic Eye puzzle](http://www.magiceye.com/faq_example.htm), legend has it that he actually enters your soul.
______


This was as fun to write as it was weird to read. If you've got the hardware that can swing it, putting two images together is basically a one-liner from the command line. [Source code is here](https://github.com/NapsterInBlue/style_transfer)-- [hit me up on Twitter](https://twitter.com/NapsterInBlue) if you come up with anything particularly bad!

Cheers,

-Nick

