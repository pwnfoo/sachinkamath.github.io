Tags: fedora,gsoc,python
Title: fedstats - Final touches and road ahead
Date: 2016-07-30 02:26:00
Slug: fedstats-final-touches-and-road-ahead
Category: gsoc


>GSoC Deadline is coming!

This week was meant for me to add the final touches to the tool and getting statistics for Flock ready by tweaking it.


#####Final Touches


The only thing remaining was categorization of output files. This had to be done because the files generated earlier where cluttering the main folder if too many users were pulled for. A very elegant solution was to categorize them into folders. by usernames - and then a `.gitignore` entry for all the outputs. Although I had `.gitignore` entries earlier, I organized files only this week.

This is how it basically works :

If the tool is called with the `--group` argument, the output is stored in `<group>/<username>/<output_filename>` and if the tool is called using the `--user` argument, then the output is to `<username>/<output_filename>`. Also, to avoid confusion - and overwriting of files - the default filename of every file is now `<username>_main.<extension>`. If a duplicate entry is found, a numeric number is automatically appended to the end.

I also started  prettifying the code and scrubbing it. There were performance issues while grabbing group members but now, the JSON can be locally cached by using `--mode json` argument.

As of now, the develop branch stands at around 48 commits.

------------------
####Road Ahead

The tool is written in the format of a script and this needs to be addressed. I have started working on packaging this tool and am currently trying to split up the script into modules to get it ready for packaging. Although it is not on my GSoC timeline, I am anyway going ahead with it.

Post-GSoC Goals :

* More powerful stats

      *Comparison graphs, multi-threading, caching and more..*

* Package the tool

       *The tool needs to get ready for PyPI and needs to be modularized.*

* Implement missing features in statscache

    *Statscache does not have the graph features (yet). Also, it'll be great to combine it with FAS features for more powerful analytics of data like `Count by group` and so forth. There was a discussion on whether the tool should be migrated to statscache or not but considering the target audience, initial plan and the timeline of GSoC, it was scheduled for after GSoC.*

* Continue work with Onboarding

    *Onboarding is a really long process and I'm looking forward to bettering the Onboarding and Join Process of Fedora*
