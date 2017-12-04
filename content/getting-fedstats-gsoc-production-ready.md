Tags: fedora,gsoc,code,python
Title: Getting fedstats-gsoc production ready
Cover: images/Screenshot-from-2016-05-28-12-26-25.png
Date: 2016-05-28 06:57:09
Slug: getting-fedstats-gsoc-production-ready
Category: gsoc


I have been working on a tool that generates the statistics of Fedora interns. When writing code and running it, I came across various errors. I thought blogging about it and keeping track of it will be a good idea for anyone who will be using it in the future. So here goes :

Q. What is this anyway ?

**A :** It is a CLI tool/script written in python that pulls data from [datagrepper](https://apps.fedoraproject.org/datagrepper/) and generates graphs/output as per the users' requirement.

Q. What are it's features?

**A:** Take a look at the project on [Github](https://github.com/sachinkamath/fedora-gsoc-stats/) or [Pagure](https://pagure.io/gsoc-stats).

Q. The program throws errors while running. What should I do?
**A:** This program was tested on Fedora 23 and ran without any errors/warnings. However, each person has a different machine and errors might have crept in. To begin with, make sure your default Python compiler is 2.7 and not 3.0. This tool is not Python 3.* compatible (yet!). Also make sure your environment variables were set correctly. `python --version` should say `Python 2.7.*`. If you face an issue, please open an issue in the [Issue Tracker](https://pagure.io/gsoc-stats/issues) of Pagure.

Q. Why are the  SVG's generated blank /  completely dark.
**A:** You are using your default image viewer which probably doesn't support viewing of clickable SVG's. Try opening the SVG in a web browser and check if the problem persists. File an issue if you can't get it to work.

Q. The PNG image is black / blank.
**A:** This is an issue with the installed packages. To overcome this issue, run `pip install tinycss cssselect cairosvg`. Try running the tool again and check if the problem persists. If at any point of time the gcc compiler fails with an error message of `ffi.h` not found, do `sudo dnf install libffi-devel` to solve the issue.

Q. The text generated is blank.
**A:** You do not have fedora-meta installed. The tool does check for this in the startup and warns you. If you had not noted it, you need to do `rpm -q python2-fedmsg-meta-fedora-infrastructure` to check if fedmsg-meta is installed. If it says the package is not installed, you need to do `sudo dnf install python2-fedmsg-meta-fedora-infrastructure` to install the package. Run the tool again to check if the problem persists. *(Shoutout to [pingou](https://fedoraproject.org/wiki/User:Pingou) and [Ralph](https://fedoraproject.org/wiki/User:Ralph) for helping me identify the issue)*


I'll try to add in more as I develop code further. Let me know what you think of the tool in the comments below.

Suggestions/criticism welcome :)
