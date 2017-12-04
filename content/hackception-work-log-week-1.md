Tags:
Title: HackceptionCTF  Work Log - Week 1
Cover: http://www.tripwire.com/state-of-security/wp-content/uploads/cache//featured4/2224787848.png
Summary: Event Co-Ordinators' worklog of Hackception CTF and an introduction to Capture The Flag, organized by Sachin S Kamath and Nishaanth  Guna for Anokha 2016.
Date: 2016-01-23 05:33:22
Slug: hackception-work-log-week-1
Category: security


Anokha is coming! Yeayy! With less than a month to go for Anokha, work needs to be done on Hackception CTF to get it up and running on the big day. This is the second edition of the CTF, and is going to be bigger, better and merrier this time as a lot of planning has been done on the event. First things first, you can find the event page [here](https://anokha.amrita.edu/event/hackceptiononsite-ctf-event/14). What's more? It's free.

This is what the previous years' contestants had to say:

[Blog Post of Team Unclassified Errors](http://unclassifiederrors.blogspot.in/2015/03/hackception-experience-at-amrita.html)

[Shyam's Blog Post](https://hackception.wordpress.com/2015/03/05/anokha-2k15-hackception-event/)

[Sunil's Blog Post](http://bsdchoudhary.blogspot.in/)

And the prize winning blog post : ~~[Abhiram's Blog,err. Code](https://github.com/abiram11/The-Blog/blob/master/Day1.cpp)~~ Looks like he took it down.



'Nuff said. Less talks and more hacks this time.

Wondering what a CTF is? Well, Capture-The-Flag events are usually held to test the wit , skills and intelligence of a programmer or/and a hacker. CTF's are broadly categorized into two. Jeopardy and Attack 'n' Defense. Jeopardy is more like an online treasure hunt game where you are given a few puzzles/questions along with a clue for you to solve it. Once you solve it correctly, you usually receive a flag which can be entered into a flag submission portal which will grade you on basis of the correctness of the flag you have entered. Flags are usually long strings of plain-text or a MD5 encrypted hash. Of course, it is not going to be as easy as a treasure hunt. But yeah, it ain't rocket science too ;)


Attack 'n' Defense is the real deal. You might be good with jeopardy but the real test of the skills is done in the Attack 'n' Defense round. It's *Survival of the Fittest, no mercy.* Make Mistakes and watch your opponent tear your computer apart, savaging all the resources you have. You have to defend yourself from incoming attacks as well as attack the other opponents in a typical Attack n Defense CTF within a limited period of time. The game mechanism is fairly complex too. A gameserver, or the "Big Brother", constantly pushes random MD5 hashes into the vulnerable services of every team every *x* minutes. A team has to break into any opponent's system and exploit a vulnerability in the hosted service to extract the flag from the user. Every successful submission of a stolen flag will give the attackers' team points and will reduce defense points of the defending team. Told you, IT'S WARRR! The Battle of 0's and 1's, and occasionally idiots.

That being said, I expect to do the following things this week :

* ~~Figure out the Platform to use. Hackademic is unusable now. Bad Bad Code~~.
Pico it is. Waiting for permissions from the authors.

* ~~Setup Apache alongside nginx to support pico and MongoDB. I know they don't go well together, but yeah. Let me give it a shot~~. Done. My seniors are awesome guides :D

* ~~Write Web, Linux and Networking challenges. Easy ones. Will extend for a couple of weeks~~. Decided to make the practice questions this week.

* ~~Make a Slack user group, an IRC for delivering clues and somehow link it up with Slack~~. Done. Done. Slack is awesome. IRC is well umm, just nostalgic. Gives me a 90's hacker feel :')

* Configure the above IRC Bot to automatically give out clues at random times from a predefined list of clues.

* ~~Tweak  the event information, rules in the Anokha Main page.~~ Event Managers taking care of it.

* Tweak pico to my heart's content.

Yes, the work is hectic and tweaking source code of an existing application is a nightmare for most programmers. Nevertheless, it's fun and always a learning experience. After all, it's for one of the biggest tech fest of South India ;)
