Title: I Had the Data -- Pt II
Slug: i-had-the-data-ii
Tags: musing, politics


<!-- PELICAN_BEGIN_SUMMARY -->

My last post was essentially a thousand-foot view of our DNC tech and how it all fit together. But by the time I felt like I'd done a decent job giving the background, I realized that writing about *how we actually used it* would be at least another standalone post. And while we're on the subject, this is probably a good a place as any to actually explain the job I'd signed up to do.


## Our Data (That Only We Had)

### Entity Resolution

I knew we had our work cut out for us by my second day on the job. I'd just gotten off a "here's some of the reporting basics" call with the New Hampshire Data Director, Andy, and was finally getting into the lunch I'd brought. Then my phone lights up and I've got a text from a friend from home.

<br></br>
<center>{% img {static}/images/yang_gang/2_data/idr.png %}</center>
<br></br>

In case it's not obvious reading it, somewhere along the way *his* phone number was affixed to *his mother's* voter file record. In this particular instance, we must've done a search on the voter file to find people like his mother, who's ostensibly an active, voting Democrat. We constantly did this sort of list creation to coordinate with our hundreds of text banking volunteers. Essentially, we'd narrow down a population of interest from the voter file and our volunteers would collect basic survey responses, used to give us a rough understanding of where our supporters are. Text banking can be outrageously effective from a "campaign benefit per dollar spent" perspective, if you're chasing down the right leads. Unfortunately, like my friend points out, right leads is predicated on right data and... swing and a miss.

At the time, I didn't know enough about our tech stack to troubleshoot how this might have happened. And over the coming months, I'd come to learn that the data we were working with was *particularly* messy.

<!-- PELICAN_END_SUMMARY -->

Consider a few mostly-realistic scenarios:

* Tyler John Doe has gone by his middle name, John, for years. In fact, when he comes to our late-November rally he signs in as "John Doe" and gives us his phone number and email. Little do we know, John gets his middle name from his father, John Senior. Later, when we log his attendance to VAN, we look up and see that there's a John Doe that lives in Iowa. The volunteer entering data doesn't think twice that John Doe is 60 years old-- they're only going off a row in a sign-in sheet. John "Danger" Doe Sr now has a new phone number and a fancy new gmail affixed to his contact info.

* In 2018, Smitty Werbenjagermanjensen registered to vote in the midterm at 1234 Main St in Des Moines. This is the info on file as far as the Vote File is concerned. Two years later, a Smitty Werbenjagermanjensen visits yang2020.com, donates, and gives us his contact info, showing an address at #1 Example Rd. It's a particularly unique name, but when we migrate this information from our source system and into VAN, should we overwrite the address we have on file for this name or is it a new person entirely? Duplicate record, it is.

* Troy and Abed are roommates and great friends. Abed, far more politically active than Troy, finally drags him to an event. Abed signs in and passes the clipboard to his friend. "Eh, this is more of *your* thing" and he copies Abed's contact info. Now two different names have the same address, phone, and email (shoehorned_community_reference@gmail.com). Troy winds up having a great time and would volunteer again. A week later an organizer follows up, calling the number on file. "Hi, is this Abed?" "Nope, you've got Troy." "Oh! Sorry for the mix up. Have a good one." And marks Troy "wrong contact info," filtering him out of all future list pulls.

My friend's text called for us to do some "Entity Resolution," which is essentially the practice of programmatically resolving the kind of scenarios you just read. Someone who knows the best way to *accurately* marry together multiple, separate data points, using varying levels of information is worth their weight in gold. It's a skill I sorely wish I'd read up on in my previous roles. 

### Hi Tech

Campaign data is rife with human error and it can get out of hand, fast, with each additional avenue of data collection.

Think of all the ways you might use technology to run a campaign. There's direct voter contact-- via both phones and text, merch sales, donations, newsletters, Facebook, event registrations, email surveys... Each of these areas had at least one unique tool that we used to handle the data. Now consider further that every tool couldn't operate without being fed external data, while generating its own data in turn.

The biggest favor we did ourselves was truing up all of the ways that our different source systems talked with one another. We drew diagrams like this a lot.

<br></br>
<center>{% img {static}/images/yang_gang/2_data/cosmos.jpg %}</center>
<br></br>

But the Entity Resolution problem outlined above became exponentially-harder as we increased the number of source systems to match records against.

---

To a stakeholder, a question like "How do we email every supporter in Iowa to ask if they want to be a Precinct Captain?" *feels* pretty trivial. But sitting down to make it happen, hands-on-keyboard, it quickly became anything but.

For starters, we collect and therefore house supporter emails in half a dozen different systems. Which means we have to comb through each of them to find all the records with Iowa addresses (and haven't opted out of emails). Then we stack each source's payload together and deduplicate as best we can. Ultimately, our stakeholder wants to send this particular email using ActionKit and of the, say, ten thousand emails in our stack, only seven thousand of them have a record in ActionKit. So we cook up a clever way to create new ActionKit records using data linked from the various other systems.

Fast-forward few days. We sent the email but we're not seeing the increase in our Precinct Captain numbers we thought we would. "Let me show you in VAN... See? I go into MyCampaign and pull the 'Precinct Captain' survey responses. They're basically what they've been all week."

...well, email respones go to ActionKit. Did we push the responses back to VAN? Nope. Okay, doing that now.

Wait, shit. 2,800 of these ActionKit records don't exist in VAN.

You get the idea.

--- 

And so, a word of caution to anyone intending to work on a campaign's data team: All of these tools come with varying degrees of "manual upload" interfaces. If the end-users have access to use them, they're going to use them until you automate it away. The impulse is a perfectly rational one-- "Let me export this list from VAN, upload it into our DVC platform. Tomorrow, I'll export the results and upload them into VAN." And this will work without a hitch *at least as often* as it will fail silently. Then one day, they'll come to you asking why everything is broken. Simultaneously, you'll learn that this problem even exists.

On this matter, my advice is to:

1. Get a lay of the land. Even if you don't have a hand in the data flow, you should know *basically* how everything fits together.
2. If you can't be a helper, don't be an obstacle. There's a real empowerment in being able to unstick yourself. Don't gatekeep someone's ability to do that.
3. Pick your battles. You'll never have time to automate everything.
4. Identify power-users and learn how they work and think. Should you find yourself ready to automate, you'll want to replicate your experts. And they'll be happy to help because you're about to save them time and ideally, you're not being a total knob about it.

### Lo Tech

Another word to the hypothetical data person reading: If you're like me, you'll spend most of your time living in a constant state of "but there's so much more to automate!" dread. But what if, occasionally, you didn't?

This might read like a tangent after spending so much time sounding off on all of technical gotchas. And that's only because it is. Hear me out.

Urgent or no, I'd always recommend that you manually build a report once or twice before trying to automating it. You miss out on a wealth of context and intuition-building, otherwise. In that same fashion, you should make time to root around in the data. You'll thank me later.

Go into MyCampaign and literally watch the timeline of someone getting involved-- from attending their first event, to increasing frequency of volunteer shifts, to eventual Precinct Captain.

Bad data is seldom useful, but it can often be entertaining. Look for the best fake names people have given us. And by extension, names that have gotten past an organizer entering in data. Shout out to whoever signed in with the [Colbert deepcut](https://www.youtube.com/watch?v=QuWGI1uQy3w), "Suq Madiq."

Watch someone literally go from uninterested to Yang Gang over the course of a rally.

<br></br>
<center>{% img {static}/images/yang_gang/2_data/event_data.PNG %}</center>
<br></br>

Better yet, hop onto YouTube, Zach and Matt have a stream of the event, I'm sure of it. Gather your own anecdotal data. Did he *always* get an applause break at this point in his stump speech? Or is this what it looks like when people start warming up to him?

Volunteer to do manual data entry when the mailers come in. You'll remember it forever.

<br></br>
<center>{% img {static}/images/yang_gang/2_data/issue_mailer.jpg %}</center>
<br></br>

It was a punishing job. It was a difficult job. It was a wonderful job.

## Data Director

But what *was* my job?

My title was Iowa Data Director but I did everything under the sun in the three months I was on staff.

In hindsight, I should have probably saved a copy of the job posting they sent me after I said I'd be open to something beyond Data Analyst/Scientist. I'm checking the campaign site now and for the life of me can't imagine why I'm not seeing it, lol

### A Comparison

I was curious to see how typical my experience was. Specifically, how it measured up against listings on other campaigns for similar positions. I grabbed some screenshots before the positions were filled or vacated so we can look at a few.

**Strong caveat, though**: I don't mean to confuse absence of positions to mean that they don't exist. Entirely possible my counterparts were hired long ago and they're backfilling other needs. I've done literally zero due dilligence watching these listings and how they've changed, if at all, over the last several months.

**Even stronger caveat**: I drafted this entire section a week before Super Tuesday and a lot has happened since.

**Even stronger, yet:** Three years have gone by in the three weeks since I wrote that last sentence, mid-March. Woof.

#### Amy - Regional Data Manager

<br></br>
<center>{% img {static}/images/yang_gang/2_data/amy.PNG %}</center>
<br></br>

1. On the whole, this looks to be an Administrator role, facilitating the use of tools, but not doing much with the data
2. That, plus the "and/or" between Excel and SQL, which aren't even remotely similar, leads me to believe they're probably not a terribly technical campaign
3. "Targeted universes" simply means saved searches in VAN to narrow down to specific populations for Voter Contact (e.g. Democrats who have voted, who fit *this* demo and live in *this* area). We did a ton of this.

As stated above, the fact that I'm not seeing much in the way of analysis or data warehousing leads me to belive that this is probably an overflow role, designed to free up time for the data team, by staying on top of the *crucial* training and standardization of tools.

#### Joe - State Deputy Data Director
<br></br>
<center>{% img {static}/images/yang_gang/2_data/joe.PNG %}</center>
<br></br>

1. The ticketing system suggests the role is also as a liason to a greater data team
2. This listing also includes reporting responsibilities
3. It also lists Tableau in the skillset, by name

Very similar to Amy's listing, but with a wider breadth of responsibilities.

#### Warren - Data and Analytics Team

<br></br>
<center>{% img {static}/images/yang_gang/2_data/warren.PNG %}</center>
<br></br>

This listing basically coalesces all of the positions into one application. They namedrop scikit-learn which earns a point or two in my book. Moreover, "experience with website analytics platforms" tells me that they're doing *at least* some naive web-optimization on their site, which is where you'd hire a good swath of data people from industry.

#### Mike - State Data Director

<br></br>
<center>{% img {static}/images/yang_gang/2_data/mike.PNG %}</center>
<br></br>

Bloomberg's listing was about as broad as Warren's catch-all, but with a job title affixed to it. It was also much more sterile, lol

Couldn't find similar listings on any of the other campaigns.

### Skills

Broadly-speaking, I'd say these are all in about the same ballpark of my experience.

In rough order of utility, I'd say:

* SQL/VAN. From jump, my biggest job was learning the ins and outs of our VAN operation and translating it into the underlying SQL code in Civis. Then, quickly being the resident "how does this work in VAN?" guy for the data team.
* Soft-skills. The most important aspect of the job is to be shoulder-to-shoulder with the State leadership, translating their goals and needs into tools you can build to give them actionable insight.
* Tableau. I'd used it a good deal years ago, but it was my bread and butter on this job. Probably stood up ten or so dashboards that got daily use-- everything from "what is our volunteer retention looking like?" to "where are the other candidates playing?"
* Report generation. With the SQL logic worked out, I could automate the creation of dashboards and workbooks. I hadn't meaningfully used Excel in years and it came careening back into my life by way of Google Sheets. I spent at least a quarter of my time keeping up with all of the edits, permissions, unintentional breaks, permissions again, etc.
* I certainly did my fair share of VAN administrivia. Cleaning/purging data, universe creation, training, answering a million Slack notifications re: "why is VAN the way that it is?"
* Pure Python. Being stuck on a one-off data problem and being able to hop in and keep the project moving with some timely regex saved me more times than I'd care to admit.
* I didn't do nearly as much Pandas as I thought I would. Probably only had cause to use it a few times a week. Mind you, SQL and well-made dashboards made for a pretty reasonable substitute.
* Shapefiles. They're perplexing until they're not. Even learned enough QGIS to make alterations as needed. Then you can drag and drop them into Tableau, and as long as you've got a `.csv` that bridges `precinct_id` to the individual shape IDs, you're golden.

More important than any of that, though, is to find and foster your community.

### Community (2009-2015, ???)

This job was like being thrown in the deep end of the fire. I showed up competent as hell and confident in my skillset, but after a week or so feeling like I was spinning my wheels, that evaporated. I couldn't keep building the manual reports forever. At the same time, I didn't know the data, have the right context, nor did I *really* know what needed doing. Moreover, I was *certain* that I was the only person feeling this clueless.

I'd gotten my hands on the DNC's VAN documentation but wasn't making much sense of it. My New Hampshire counterpart, Andy, had a few weeks of experience on me, and seemed to be humming along just fine. As did Kristen, **someone whose title was literally Data Wizard**. I got to the point where I knew I should ask for help, but didn't want to interrupt the two of them knocking stuff out to ask "hey, yeah, hi.... what is... *any* of this?" 

And it turns out Andy was doing the same for Kris and I, and she was as well. A real comedy of errors, yeah?

We spent the next couple days poring over everything, swapping code snippets, and firing a million emails to `tech-community@dnc.org`. It was a Cambrian Explosion of getting our shit together and my self-confidence crept back in as quickly as it had left me. It was the first time I recall feeling good about the day I had and optimistic about the day I was going to have.

They were my first friends on the campaign and two of the solidest people I'd meet those months. And that's not for lack of competition.

<br></br>
<center>{% img {static}/images/yang_gang/2_data/a_and_k.png %}</center>
<br></br>

Looking back on Iowa through the lens of "skill development" has been an interesting exercise. I got really good at Tableau. My `keras` got rusty. I picked up a SQL trick here or there. I got a lot of campaign-tooling exposure I might never use again. I know how to handle weird shapefile peculiarities when things look like this

<br></br>
<center>{% img {static}/images/yang_gang/2_data/gerrymander.png %}</center>
<br></br>

More than any of that, though, I'm coming to appreciate just how much I've grown, working with people.

But more on that next time.

Cheers,

-Nick




-------------------

[Index Page](https://napsterinblue.github.io/blog/2020/03/29/about-that-time/)

[Previous Post](https://napsterinblue.github.io/blog/2020/04/03/i-had-the-data-i/)