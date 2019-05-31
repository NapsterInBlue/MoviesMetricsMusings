Title: American Beauty in 3d
Subtitle: A Math-y Approach to Character Development
Slug: american-beauty-3d
Tags: deep read, movies, musing, wellness

<!-- PELICAN_BEGIN_SUMMARY -->

American Beauty falls off of the US Netflix catalog on the morning of December 1st. I remember loving it last time I gave it a watch and so I sat down to revisit it and write about it. This was at 6:52p the day before so naturally, by the time you're reading this, that train has left the station. Bummer.
Anyhow

### 3D?

The movie ended, and I sat and pored through my notes and doodles that I took down while I was watching. This might not be the most accessible way to share my thoughts, but ultimately, I came away from this movie thinking about a 3-dimensional space. Bear with me.

<center>{% img {static}/images/beauty/xyz.png 400 %}</center>

Chances are, you've probably seen something like the above in one capacity or another. Movement to the bottom-right means that the X value is getting bigger. Movement to the top means the same for Z. Similar deal for Y. Cool. Points can float somewhere in this space that we've cooked up. I'll spare you the lousy sketch and grab something a bit more polished from Google.

<!-- PELICAN_END_SUMMARY -->

<center>{% img {static}/images/beauty/good3d.png %}</center>

Each point represents an observation of some sort of data. The axes could be pretty much anything you'd care to measure. In one of my very favorite examples of Machine Learning (which, if that's something you're interested in, by all means, close this, read this. It's fantastic.), the first step in predicting the location of a house is doing a similar exercise and putting various metrics on their own axes; combining them you wind up with a ton of data points that represent individual houses.

I'm going to be miserably reductive here and say that in our example, each dot is a person, and that the dots live somewhere on 3 personality axes. Couple clarifying points to that:

1. Each axes represents an attribute, sure. But in our housing example, everything starts at zero and grows. For an attribute called <span style="color:lime">rooms</span> a <span style="color:red">small value</span> could mean <span style="color:red">"not many bedrooms"</span> and a large value would mean <span style="color:red">"lots of bedrooms".</span>

2. Here, each axes is still an attribute, but instead values represent a place on a spectrum. A point being closer to one end isn't necessarily better or worse, just more "like" that extreme on each end.

So our spectrums

#### A character's <span style="color:lime">desires</span> being <span style="color:red">genuine</span> or <span style="color:red">superficial</span>

- Ricky, the boy next door, makes money hand over fist selling weed, but his most prized possessions are the tapes that he films
- Lester condemns Carolyn's concern over a $4,000 couch-- "they're just things", yet impulse buys a 1975 Pontiac Firebird-- "The car I've always wanted, and now I have it. I rule! *fist pump*

#### A character's <span style="color:lime">goals</span> being <span style="color:red">self-imposed</span> or <span style="color:red">society-imposed</span>

- Angela's constant obsession (and frequent lying) about her sex life
- Carolyn goes to painstaking lengths to get Lester to behave at realtor functions-- to put on a show.

#### A character's <span style="color:lime">headspace</span> being <span style="color:red">present</span> or <span style="color:red">sedated</span>

- Angela spends most of the movie with an impressive lack of self-awareness, "sick of people taking their insecurities out on [her]" and believing that "everything that's meant to happen will happen eventually" and saying and doing anything to get attention and affirmation.
- The whole first act hinges on Spacey's so-called "awakening" into a state of mindfulness. More on this to come. Time and its perception play a huge role in this movie.

This takes us to something that looks kinda like this

<center>{% img {static}/images/beauty/spectrum.png 400 %}</center>

You can imagine that, like the image above this one, each of the characters in the movie have their own dots, and if you tried mapping those out throughout the story, they'd move and shift. That's storytelling.

### Black Box

Unpacking, and, regrettably, further math-ifying this idea, imagine that there's some actual significance to where a dot falls in this space. Imagine that there's a [Black Box function](https://en.wikipedia.org/wiki/Black_box), an equation that I'm going to call **Turbulence**. Each possible dot at the intersection of these 3 axes maps to some level of turmoil, of inner strife. The complicated mess of personality gets stuffed into this sausage equation that returns a degree of inner peace, or lack thereof. A character that's considered to be 'one-dimensional,' with embarrassingly clear motivations and predictable interactions with the world around them, fits neatly into this paradigm, probably only having strong tendencies in one axis. Hacky writers use these characters as soulless plot drivers, while others consider the effect that this imbalance has on a character.

<center>{% img {static}/images/beauty/allwork.jpg 600 %}</center>
<center>This blog post features original and proprietary ideas.</center>

The important distinction that I want to note is that this Black Box Turbulence function doesn't behave in any uniform fashion. As I've crudely illustrated below, you could be exactly the same in 2 of the 3 spectrums, but one arbitrary and poorly-illustrated unit step on the third behaves wildly different.

<center>{% img {static}/images/beauty/fruits.png 600 %}</center>

But hey, this is all conjecture, generalizations, and some paint.net finagling, but this is life, right? We can't "optimize" Turbulence; nobody's solved for it. I can't possibly imagine that my values and what works for me is what works for you. That's what makes us unique.

Lester and Carolyn share a life together. They come home to the same house, dine with the same unhappy daughter, sleep in the same bed, but they're both miserable in their own way. The stressors and challenges they face are a direct result of their values and perceptions. They're two different dots in the same Turbulence Space.

But if you accept the way that I'm framing this so far-- the inherent randomness in this theoretical Turbulence Space--, then "character development" isn't a parallel trajectory shared by everyone in the story. They aren't all wired the same way and therefore aren't all marching toward the same definition of "healthy," of "happy." Hell, I'd contend that for the majority of the movie, Carolyn barely moves at all. If I asked you to give me a rough sketch of where her dot would be, it'd probably look something like this, right?

<center>{% img {static}/images/beauty/spectrum2.png 400 %}</center>

She's portrayed as someone who has bought into the values of middle-America, hook-line-and-sinker, with very little regard for reflection, reinvention. Her biggest expressions of emotion happen after public failures, and she handles them as privately as she does violently. Nobody is a harder critic on Carolyn than Carolyn, but she's completely blind to this, instead boiling up during the Third Act to race home with a bullet meant for Lester, chanting a mantra about her victimhood.

Ultimately, her stale, self-imposed toxicity is what makes Lester's transformation so damn interesting.

To a degree, he begins the movie, like her, really letting his outside world get to him. Early on he comes home livid that a business is behaving in an extraordinarily predictable fashion and trying to downsize to keep their books balanced. He has spent the last several decades as a passive actor on his own life ("sedated," he calls it) and is jarred by the world changing around him. Ultimately, life piles up, and it's enough that it's impossible for him to not reassess where he's at in life and make adjustments.

American Beauty is primarily about Lester's movement through Turbulence Space, the lucky arrival at his own personal Black Box Turbulence value, and the varying degree that everyone around him struggles to do the same.

### What About Distance?


So we've got this framework. Wandering through Turbulence Space in search of personal happiness is a total crap shoot that follows no rhyme or reason. But despite this, the thing that's going to stay with me when I think about this movie, and this slapped-together idea of reducing and mapping a person's essence, is the importance of the space between any two points in Turbulence Space.

As it relates to the movie, some examples stood out to me more than others:

- Lester is in shock and awe of Ricky's "So don't pay me. I quit. Now leave me alone" line and soon follows suit by getting himself fantastically fired (in a manner that thoroughly scratched an Office Space itch). Despite the fact that Lester enjoys a fair degree of conventional success, an abrupt and very real view into someone else's value system emboldened him to consider if his values were correct ones.
- Carolyn is beside herself, heart-aflutter, when she learns that The King shares the same attitudes on appearances and adoration. She learns that despite the fact that he is, in fact, also struggling to keep his life held together, it is more important to him to be celebrated for what he has been than accepted for the faulted person that he is. Regardless of how much shaming and bickering Carolyn does, Lester simply does not see things this way and it becomes something of an escape to learn she's not alone in this regard.
- Twice in the movie, we hear Jane say that she wishes she had a role model, rejecting and mocking her father, but all throughout the movie learning from Ricky. Ironically, Lester is trying to do just the same thing. More ironic yet, by the end of the movie both Lester and Ricky profess the same overwhelming sensation about life itself-- they're not so different.

Characters really only ever feel compelled to move from their comfort zone when they're unhappy. They develop an approximation of someone's Black Box Turbulence and try their hand at adapting themselves to be more like, or unlike them-- Jane despises her dad, intentionally growing away from him and rolling her eyes every time Ricky and Angela stand up for him. Carolyn perceives The King to be successful and satisfied which reaffirms the way that she lives her life. Lester tries to become more aloof physically attractive to impress Angela-- only when he finally has her does he realize that his arrival to her point in space didn't bring him the happiness he was after. From a character study perspective, this conscious movement through Turbulence Space relative to other actors is absolutely critical.

Also worth considering is the importance of distance that a character navigates over time:

- A big driver in Lester's behavior is reflection on the person that he used to be, flipping burgers, partying, and getting laid. Upon reflection, he finds that whatever concessions he's made with himself has put him into a state of higher Turbulence, and he finds peace in regressing back to the way that he was.
- The amount of emotional whipsawing that Ricky's father does is exhausting to watch. Even in an individual scene, he'll go from beating the hell out of his son, to looking at him with pride. He begins the movie condemning his gay neighbors for their way of life, kicking Ricky out of his home when he thinks that his son is gay, shows up at his neighbors house in the middle of the night to kiss him, and then when he gets rejected, returns to murder him. Goddamn.
- Lastly, though the characters have all moved considerably through Turbulence Space over the course of their lives and the story, their perceptions of others hasn't. Lester in particular struggles to reconcile between the people that he lives with and who they really are. When we see Lester and Carolyn's first fight at dinner, Jane storms off into the kitchen. Lester follows and begins with "What happened? We used to be pals." Later in the movie, Carolyn returns home and Lester tries his damnedest to coax out his real wife, reminding of the wild things that she used to do before her life revolved around her work and the opinions of others.

### Think about it


All models and brain dumping aside, I want to summarize with two of my biggest lasting impressions from American Beauty:

The first being that our best guess for where someone lies is Turbulence Space is just that, a guess. Lately, I've been trying to work on developing better GitHub skills and in doing so was referred to an awesome site called [think-like-a-git.net](http://think-like-a-git.net/). Perhaps it's because I stumbled across it this morning and the thought was still alive in my head, latent, but the author had a really great learning moment that I think is [worth sharing.](http://think-like-a-git.net/sections/git-makes-more-sense-when-you-understand-x/example-1-kent-beck.html)

<center>{% img {static}/images/beauty/kent.png %}</center>

We really don't know. But on the off chance that we nail that guess, we often have a comically incorrect view of how together someone's got everything-- especially if they're the type of person who values their perception. As I've more than belabored at this point, that Black Box Turbulence function is no joke.

The second is a quote that Lester said that I really loved:

**"It's a great thing when you realize that you still have the ability to surprise yourself. Makes you wonder what else you can do that you've forgotten about."**

I think at its heart, American Beauty is a love letter to wellness and mindfulness. It's about a man staring his unhappiness directly in the face and his journey to learn how to be more at peace with everything from the world around him. Characters are ushered out of their comfort zone when their Black Box Turbulence hits them across the head like a bucket of cold water. Some people ignore this wake up call and double down on their unhappiness, others poke around Turbulence Space until they find a place that suits them, ultimately finding themselves being on the wrong end of an Austin Powers-level "seeing the wrong thing through the window" gag and being gunned down by a Neo-Nazi. But hey, that's life. If I had a nickel.
