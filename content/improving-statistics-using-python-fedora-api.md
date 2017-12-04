Tags: fedora,gsoc,python
Title: Improving  statistics using python-fedora API
Date: 2016-07-24 12:09:00
Slug: improving-statistics-using-python-fedora-api
Cover: https://communityblog.fedoraproject.org/wp-content/uploads/2016/03/gsoc-announce-1.png
Category: gsoc

I was working on adding the group scraping feature this week. This is one thing that was proposed in a recent meeting of Commops, originally for CommOps retrospective wiki.

I was initially thinking of using statscache for this, but came across a few things that stopped me from doing so. Firstly, statscache is not deployed anywhere, which basically meant that I'll have to pull the historic fedmsg data using `fedmsg-hub` for the first run, and anyone who wanted to use the tool will also have to do the same. This tool is to be used by anyone as is, and not everyone will have the resources/bandwidth to download all the `fedmsg` messages. Also, statscache lacks the feature of grouping users. I could only find a `by_user` count of messages. It made more sense to run the tool on FedoraInfracloud and grab data from it.

Now that I could not use statscache, I initially tried scraping using Selenium and requests. After receiving some quality time on it, i realized that I was getting bad responses from the server. *(Sigh, CSRF Token Issues)*. After some research and IRC discussions, I came across `python-fedora` [API](https://pythonhosted.org/python-fedora/api.html). It is an amazing API that does almost anything. Using it, one can log into FAS and perform a lot of actions like editing profile, getting user info,etc.

In fedora-python, the [FAS Modules](http://www.pythonhosted.org/python-fedora/existing.html#fas) can handle logins, session caching and user handling. I wrote a function that'd pull all the users from a specific group, which looks something like this :

<script src="https://gist.github.com/sachinkamath/7f5a458a8793aaecc6fd472f40fa999d.js"></script>

And guess what, it worked like a charm. Okay - now for the login part - I had two choices; either prompt the password / get it from a config file. I chose the latter because it'd make automation easier. I ended up using `ConfigParser` to pull data from a cfg file.

During this, I noticed a very interesting thing - The next time I ran the script, I modified my password a bit *(the hacker in me prompted me to :p)* and surprisingly - it worked. Session caching is amazing- isn't it. Shoutout to `#fedora-admin` for helping me understand that :)

And finally, I integrated it in the main script and added the argparse argument of `--group / -g` to specify a group for which the data has to be generated. Of course, this should not be paired up with `--user`, or it will throw an error. Also, all the internal errors like, bad group name and incorrect credentials is handled by python-fedora itself! Hurray. The script looks much better now! :)

![](images/Screenshot-from-2016-07-30-20-30-01.png)

<center> *Fig : Data being pulled for the CommOps group* </center>

And right now, the develop branch has about 45 commits.

![Current repo commit count](images/Screenshot-from-2016-07-30-20-41-26.png)
</br>
I am looking forward to working with Onboarding Series badges and yml files next week and cleaning up and organizing the script files. By next week, the tool should be *pycodestyle* ready :)
