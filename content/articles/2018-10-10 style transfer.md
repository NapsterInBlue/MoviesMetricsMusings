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


<center>{% youtube YeGAwpZFetY 400 %}</center>


______

All blundering aside, I hope that if you made it this far down you enjoyed reading. [Here's a link to the repository that I used to put everything together](https://github.com/NapsterInBlue/Academy-Awards), including the raw box office data that I spent a day getting at-- [hit me up on Twitter](https://twitter.com/NapsterInBlue) if you wind up doing anything cool with it!

Cheers,

-Nick
