Title: People Over Politicians
Slug: people-over-politicians
Tags: musing, politics


<!-- PELICAN_BEGIN_SUMMARY -->

As soon as a week after I'd started working on the campaign, I was already getting every manner of "so what's it like?" questions from friends I'd worked with at my industry job. Six months after I'd separated, I was so far removed from the work I'd done, yet so thoroughly tossed into the deep end of this new life, that comparing and contrasting was a wall of braindump text.

Obviously the problem space was different. I've spent my last couple posts outlining the tech stack I was unfamiliar with and the learning curve therein. Geographically, Iowa was much flatter (and had markedly less traffic) than what I was used to in Michigan. The food was alright. I barely experienced the nightlife in Iowa. Financially... it's now obvious to me why there aren't more tech-to-politics transplants.

Without a doubt though, I think the starkest change was in the people.

### A Lifestyle

I never quite adjusted to how much of a *lifestyle* this was for a good chunk of my friends on the campaign. Mind you, I was the odd-man out-- I can count the number of candidates I've voted for (much less have been employed by) on one hand, but the amount of people introduced to me as having "worked on *So and So*'s Senate race!" blurred together. The introduction was usually followed by a beat of silence as I combed my mental roladex, came up blank, and made some offhand quip about how I was class president once. Honestly, I was only half-certain that there weren't baseball cards of all these campaign teams in circulation.

<br></br>
<center>{% img {static}/images/yang_gang/3_people/baseball.jpg %}</center>
<center>["Eh, close enough"](https://www.youtube.com/watch?v=LEiG7NzN6fM)</center>
<br></br>

<!-- PELICAN_END_SUMMARY -->

All told, I'm confident that there were alumni of at least a dozen other campaigns that would come swarming every time pizza would show up at the office. Thinking about it some more, I seem to recall a lot of folks from Bernie and Hillary's 2016 teams as well as a handful from Beto for Senate. I think Andrew said it best when he was panneling for the Nevada Caucus on CNN: "Politics is incestuous enough such that everyone on every team knows someone else on someone else's team." I heard this sort of thing often: "My roommate works for Amy." "I'm grabbing lunch with friends on Warren." "Mike Bloomberg stopped and frisked me."

But all of this is only top of mind now that I'm so far removed. In those months, it got real familial real fast as we gained a shared understanding of the relationship between hours worked and laundry washed. Every new hire was warned, prophetically, that "everyone is going to be mad at everyone. All the time." Time dilation got weird, too-- someone would spend a couple days buttoning up personal matters it'd feel like you hadn't seen them in weeks. Damn if that level of shared toil didn't erode away all of the memories from "the before time."

And it didn't occur to me then, that this was-- by definition-- the next thing everyone was doing. Regardless of how this all panned out, it will uniformly be something that we all *had done* when we meet new teams at new gigs. In the meantime, let's get this nerd elected, yeah?


### A Different Breed of Stakeholder

The biggest throughline I found in working with the Iowa staff was how incredibly resourceful everyone was. I think "scrappy" is a bit overused, but I'm struggling to come up with a better descriptor. By the time I'd showed up in early November, there were a myriad of Google Sheets stitched together by people, from all levels of the organization, who had access to pull their own data from VAN and had figured out how to build the reports they needed.

To that end, I was thrilled to realize just how helpful I could be, greasing the wheels here and there with a bit of code. Something like a "How do I make a leaderboard of organizer recruitment rate with college students?" could have been a daily task, accomplished with a saved search in VAN, using their UI to do some data exports, then some pivot table magic™. Or if they agree "email ending in `.edu`" was sufficiently "college" then it'd take me like 10 minutes to give them a Google sheet that would auto-refresh every day.

    select
        organizer,
        sum(case when ch.contact_result = 'shift'
             then 1 else 0 end) as shifts,
        count(*) as attempts,
        shifts / attempts as success_rate

        from            supporters s
            left join   contact_history ch 
                on      ch.people_id = s.id

        where           RIGHT(s.email, 3) = 'edu'
            and         ch.contact_type = 'phone'

        group by        ch.organizer
        order by        success_rate desc


A mentor of mine, who I thought about often those days, had always encouraged me to help people achieve their highest and best use. I was thrilled to be able to save people from spreadsheet hell and get back to doing what I sincerely thought was the hard work. And they absolutely did. But to my sincere delight, *so many of them were interested in getting even better with data.* It was a group of hungry fishermen saying "teach me to fish" and I admired the hell out of that.

It wasn't long before I was feeling less like the token "data guy" and could literally see the people around me leveling up. We'd developed a shared vocabulary of nuanced metric definitions that we were all paying attention to. I saw folks leverage source-of-truth datasets I'd developed to make their own goals dashboards. Early December, I made a Slack channel to centralize the torrent daily VAN questions I'd get (lovingly named `Rage Against the Machine`) and near the end I barely had to monitor it-- everyone was so on top of helping one another grow.

Hell, people were even catching bugs that had passed silently in the production dashboards we were all looking at.

<br></br>
<center>{% img {static}/images/yang_gang/3_people/keith.png %}</center>
<br></br>

Those months were marked with dizzying highs and gut-punching lows. When I'd write home I often joked that this was probably a bad job for someone "actively working on their workaholism." Give me the right data problem and I'll be thinking about it, whether I want to or not, until it's done. Layer in how important and time-sensitive the work is and yeah, go figure I'm running myself ragged trying to make it all come together. All personal drive notwithstanding, I wouldn't have been able to keep up with it were it not for the tenacious, brilliant friends I had around me.

By now you might agree that I'm having real trouble being succinct in these posts. Nevertheless, I can't quite describe the feeling of camaraderie I felt after a long day of putting out fires, shutting the door and talking through how we'd get through the next one together. It was a partnership.

<br></br>
<center>{% img {static}/images/yang_gang/3_people/sinatra.jpg %}</center>
<center>Just whiteboarding, eating day-old pizza, listening to Sinatra, and taking creepshots of the guys.</center>
<br></br>

### Downstream

And what can I even say about my friends in Field?

For starters: Hardest-working group of people I've ever had the pleasure of knowing. Full stop. Now I'm hardly trying to discount the scores of fantastic people I've worked with and for over the years. It's just different. So many of these folks had, like me, picked up their lives to champion a once-in-a-generation candidate and that passion was obvious in everything they did.

It was such a gift to see them doing their thing. Every Slack post sharing pictures of the small army of volunteers that had rolled into their office. Hearing the pride in their voices as they reported the day's numbers (when I'd eavesdrop on their nightly calls). Seeing the relationships and *community* they were fostering together... It's probably a criminal understatement to say that I miss the friends I worked with.

It was egoless. Not "Look what I did" but "look what *we're doing*."

<br></br>
<center>{% img {static}/images/yang_gang/3_people/pride.JPG %}</center>
<br></br>

Regrettably, I didn't get to meet everyone that came work in Iowa. We about doubled our Field team over the course of a month between December and January and by those pesky laws of time and space, we couldn't all be together all the time. But sincerely-- my best days on the campaign were days I could share good news. It's been the highest honor I've known, getting to call them friends and do all I could to set them up for success.

## The Yang Gang

Of course, I would be remiss if I didn't then talk about the sea of people who cared just as much, pro bono. I heard again and again "other campaigns would *kill* for this supporter base." And that was for absolute certain.

The campaign's been suspended for awhile now, but my Twitter feed is still awash in Blue Hat emojis. It feels like #humanityfirst is being shepherded from slogan to movement. Heidi, Paget, Genie, Matt and Zach, TrapSmoove, Scott Santens, Sorority of Yang, and many, many others created an engaging, *welcoming* community. In truth, it was what initially drew me to Andrew and so by extension, why I ever took the leap of faith to pack up and head to Iowa. So if any of you are reading this, I want to say thank you.

We worked hard. I probably checked the subreddit in excess of 20, 30 times a day and would *consistently* see people calling for folks to phone and text bank. The amount of live streams and Twitter clips of people making impromptu call centers out of their living rooms were a delight. I wish I could have shared then and I wish I still had the data to show now-- that shit **mattered**. Every day, I'd update a composite map of all voter contact. A dot for every call, every door knocked, every text, all color-coded by contact type. By the end of December, it looked like someone had spilled a bag of confetti over the state of Iowa. It got to the point where I had to timebox the data by day or plot each contact with 70% transparency to tease a more nuanced narrative than "we're doing **so** much with what we've got."

Hard work aside, we had an incredibly *talented* group. I followed a dozen or so production-quality YouTube channels. We had onboarding sites and countless content creators making FAQ pages, with timestamped videos where people could see, precicely, where Andrew's been on the record about a particular issue. I kept the site where you could see the impact of $1,000/mo in your community bookmarked and shared it liberally. We had an *exceptional* community-organization tool in YangNearMe.

<br></br>
<center>{% img {static}/images/yang_gang/3_people/yang_near_me.PNG %}</center>
<br></br>

And the creative content. It was weird, thoughtful, and hilarious. Most importantly though, it was fantastically-curated.

<br></br>
<center>{% img {static}/images/yang_gang/3_people/yang_prints.PNG %}</center>
<center>I mean look at the size of that scroll bar. And that tardigrade.</center>
<br></br>

And when people started flocking to Iowa, they'd marry this with an affinity for baking to make the best cookies I've ever had a guilty conscience eating.

<br></br>
<center>{% img {static}/images/yang_gang/3_people/cookies.jpg %}</center>
<br></br>

But damn if I didn't stare at a blinking cursor for the better part of twenty minutes before continuing here. Because for as much good as there was, it was a lot to navigate.

### A Tension

In hindsight... duh, the anti-establishment candidate *would* have supporters without a lot of trust for the process.

My phone was a graveyard of unopened texts from unknown numbers. Same goes for the email inbox I quickly learned to only check once or twice a day. All from resourceful, passionate, people urging me to "just give them the data," or to look over their strategy proposals-- the campaign existed in a perpetual state of "doing it all wrong."

* We should be in more areas, we're too saturated.
* We should consolidate, we won't be viable.
* We should tell people their goals need to be higher, they're slacking.
* We should dial down the goals across the board, they're overwhelmed.
* Bernie won here in 2016 so we should go here (?)

But it wasn't all abject, opinionated chaos. Of course it wasn't. Now that I've got a lot more free time on my hands, I'm finally trolling through the sea of Google Docs I was CC'ed on and seeing what was essentially an organization of volunteer leaders parallel to the campaign.

And they *really* felt like they should have access to the data.

<br></br>
<center>{% img {static}/images/yang_gang/3_people/tension.PNG %}</center>
<br></br>

Just not enough to come be a part of the solution.

<br></br>
<center>{% img {static}/images/yang_gang/3_people/tech_help.png %}</center>
<br></br>

And that sucks. Because all of my defensiveness aside, *I don't disagree* with much of the criticism leveled against the campaign. Moreover, I think the community brought *at least* as many good ideas to the table as bad ones. Ultimately though, we never had the staff or the infrastructure to sort out which from which, nor the capacity to take on more work than we were already doing. And so, the campaign stayed laser-focused, blinders on and executing where it had autonomy: the campaign.

### A Real Miss

I've spent the past weeks whipsawing between "I should have done this or that differently" and "I should have done more." And of all the "mores" I could have done more of, unambiguously, this could have been the "more-est." Fuck. **We** could have done more of. It's crazy how this still feels like it's my fault, weeks later.

In any case, the next time we take a crack at this, this should be someone's full-time job. Specifically this person should:

1. Chiefly, be someone who understands the limits of what we're **legally** allowed to have volunteers help with. Nobody was trying to wind up in court because we kicked a `.csv` to someone with more experience in Network Science than us.
2. Have experience orchestrating technical projects in a context that looks similar to Open Source. We had a lot of talent reaching out, asking if they could hack on a quick-hit over the errant weekend-- I personally had a number of friends and former co-workers interested in pitching in. Hell, I was in the same boat before I took the plunge.
3. Have experience creating *just enough* transparency to keep everyone happy. It was a chief area for improvement felt in Field and Yang Gang alike.

<br></br>
<center>{% img {static}/images/yang_gang/3_people/transparency.PNG %}</center>
<br></br>

On the other hand, nobody campaigns in a vacuum. Primaries are a messy afair where of all of the campaigns are trying to elbow for rank over one another. For instance, the precincts that we won outright were a result of data'ing our way into where we thought the other candidates were playing and putting focus where there was virtually free real-estate. And so regardless of intent, that means that information shared is indeed, information shared.

On the other, *other* hand, it was an objectively *good thing* to champion how low our average donation was. Or to publicly host progress bars to our fundraising goals (80% of my donations were between 11p and 12a on the last night of a goal push). And while it's clear they recognized this issue wasn't cut-and-dry

<br></br>
<center>{% img {static}/images/yang_gang/3_people/understanding.PNG %}</center>
<br></br>

I'm certain that there's more we could have done to keep fanning the enthusiasm.

And by extension, farm out quality work. They'd done a great job documenting their various initiatives, complete with retros, KPIs, and a good deal of reverse-engineering our org chart so they knew who to try and reach out to about them.

<br></br>
<center>{% img {static}/images/yang_gang/3_people/projects.PNG %}</center>
<br></br>

And once you get over the eeriness of how close their approximations are to reality, there were some bang-up proposals we would have been well-served to coordinate with.

<br></br>
<center>{% img {static}/images/yang_gang/3_people/precinct_ex.PNG %}</center>
<br></br>

When we regroup in 2024, we *have* to do a better job of this.

## Delegate. The Verb, not the Electorate Proxy.

I think it took all of three days being back in Michigan for me to stubbornly break my laptop out and try and pick up where I'd left off in October, improving my Python chops. I was getting frustrated as hell, consulting docs and old notes on things I'd had down pat not six months prior. Self-improvement is the thing I like most about myself and I felt like I'd objectively regressed. Had a real "I went to Iowa and all I got was this lousy cynicism" attitude about it, I'll admit. 

But as I stuck with it, it started falling back under my fingers-- of course it did-- moreover, when I wasn't coding, I was writing and reflecting. After a couple of weeks of this, I've come to realize that I lived through one hell of a crash course in team-building. More accurately, **recognizing how important it is to ask for help.**

Personally-speaking, that's the big, neon, `LESSON LEARNED` sign I'd hang above this whole blog series. It's miserably ironic to me to have spent so much time thinking about organizational failures due to lack of process ([I'm sympathetic if coworkers prefer the term 'obsessed'](https://napsterinblue.github.io/blog/2017/08/18/thoughts-about-tech-debt/)). Doubly ironic, that I was echoing our *macro* communication problem with the Yang Gang on the *micro* scale of the Data Team.

### Communication Breakdown

I was the only person working Data in Iowa for a long while.

The rest of the team worked together in New York, save for Andy and Kristen in New Hampshire and Colorado, respectively. It took me a couple weeks to learn that nobody but Andy and I were daily VAN users-- most all of the work done at HQ was done leveraging datasets I'd never really touch (e.g. financial, marketing cohort-type stuff).

For that first stretch, I considered myself solidly more an extension of Iowa Field than a member of that team. The Data Team had daily standups, booked for 30 minutes and seldom longer than 5-10. They were always talking in shorthand about projects I had no context on and likewise, my updates were always about some nuanced Iowa Field thing that nobody had context to weigh in on. Speaking two different languages, it seemed.

As my nights got later and later, I stopped prioritizing making the 9 AM-- 8 AM my time-- call.

I also didn't use the same Asana taskboard they did. The same "10 minute quick hits" I was so excited to be able to help my Field friends with, wound up being Death by A Thousand Cuts as I was catching maybe a dozen or so of them a day. I'm awful at telling people no and it didn't make much sense to spend half the time *task bookkeeping* that it would take me to just *do the task*. Moreover, I was hardly about to have my friends submit a ticket to the team in NY so they could then reach out to me for context I didn't have time to give, before they put it on the board and assigned me the ten minute fix anyways. So more accurately, I should say that I didn't use *any* Asana board.

And I burnt out hard. The few times I *did* talk to the people in NY, there was always concern and a confusion about why I wasn't asking for help. And appropriately, it'd take me a good while to respond to these emails because I was in a constant state of "absolutely slammed." But thanks to a steady diet of Red Bull and exisential dread, I was more or less managing, so I didn't make a fuss.

Then the other shoe fell. Sometime around the back half of December, I think, both the CTO and the Reporting Director who hired me had moved to a totally different positions and we were even more short-handed.

### Righting the Ship

As we scattered for the holiday, everyone at varying states of working remote. Christmas and Christmas Eve were mandatory "have someone hide your computer" days. I slept so damn much that week-- the break was a well-needed reset button. I saw some friends and family, watched a couple seasons of Community, and slept some more. I was pretty thrilled when I started feeling like a person again. But what was more invigorating was learning that the cavalry was coming.

Our Analytics Director, Robin, had stepped up to subsume the whole data team. And well-deserved, he's legitimately one of the brightest and hardest-working people I've had the pleasure hacking with. He and a couple others would be filtering into Iowa the first couple weeks of January. His deputy, Louisa, was going to hang back and start aligning HQ work to support the campaign's increasing focus in Iowa-- she'd later join us as well.

<br></br>
<center>{% img {static}/images/yang_gang/3_people/fanfare.JPG %}</center>
<center>He arrived with much fanfare.</center>
<br></br>

And man, it wasn't long at all before that drowning feeling began to subside. The two that came with Robin, Troy and Amelie, hit the ground running with a tenacity and ownership that exceeded every single hope and expectation I'd had. It was the first time in my career I'd ever surrendered a vague idea of "these projects I wish I had time to do" and had them materialize, better than I would have done, within days. I hope my subconscious cements the gratitude and relief that I felt delegating to such capable folks. It taught me so much.

Within a week, we were banging out all kinds of data standardization and documentation, fixing a huge backlog of sticky notes I'd filed under "Gross VAN Stuff" and were now starting to generate insights and reports that Iowa didn't even know they wanted or needed. We ate a ludicrous amount of Thai food.

It only got better as Robin and Louisa developed the effective "source the Iowa work to HQ" pipeline that I'd needed but neglected forging. Then Louisa and Kristen came to 950 Office Park in West Des Moines and we spent the next few weeks cooking with gas. If I were kinder to myself, I'd spend more time celebrating how much I achieved in those first couple months, doing my best. But looking back, all I can see is a supreme lesson in "you can't do everything by yourself."

I'd never experienced that level of focus before. We woke up, knocked shit out all day, then went to bed. Rinse, repeat. All of us did-- across the hall, we'd have an All-Iowa standup every morning and evening. Robin and I would go and speak our piece, as did teams from political, web, advance, scheduling, field, operations, and a host of temporary teams spun up to deftly handle the various speedbumps that would bubble up (how do we house and get cars for several dozen staffers coming in two weeks? Katie Dolan is how.). Fast forward a day that would fly by, and by the time we'd regroup, damn-near everything was done. I said it often, and on deaf ears, that if they ever bore of campaigns, we had some world-class technical Project Managers in our midst.

Even now, as the dust has settled on everything, I'll say with confidence that we'd built an incredibly sophisticated approach to the Iowa Caucus. My optimism was less and less reluctant by the day and I sincerely thought we were cruising for a top five, perhaps top four, finish. Of course, we all know how that panned out.

But more on that next time.

Cheers,

-Nick




-------------------

[Index Page](https://napsterinblue.github.io/blog/2020/03/29/about-that-time/)

[Previous Post](https://napsterinblue.github.io/blog/2020/04/08/i-had-the-data-ii/)