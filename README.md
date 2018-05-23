# MoviesMetricsMusings
So the blog itself is looking at [another repo](https://github.com/NapsterInBlue/napsterinblue.github.io), and rendering it directly. This repository contains all of the course code to populate *that repository*.

In hindsight, I don't think this is different enough from [the blog that I used to structure it off of](https://github.com/jakevdp/jakevdp.github.io-source#building-the-blog) to merit copying over forking.

That said, I do want to point out some key differences between what he did and what I did in case you're looking to use either repo as a jumping-off-point:
* I've never published a book, so my About page is pretty different.
* I've got another navbar link titled `My Notes` cheated to go to a totally-separate project containing [my note-hosting platform.](https://github.com/NapsterInBlue/notes)
* I have my own fork of the `toc` pelican plugin to allow table of contents parsing from notebooks
* Jake tends to just put all of his work into the `content/downloads/notebooks` folder. I've had success instead working in an independent repository, then pulling it in as a submodule when I'm ready to publish.

Last note, if you're going to use this, **make sure you understand submodules back and forth**. This project was the first time I've dealt with them, and they accounted for probably 70% of my struggle to get going in all of this.

Cheers,

-Nick
