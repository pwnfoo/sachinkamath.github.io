Tags: security,guide,tech
Title: Directory Listing - Dangerous?
Date: 2016-01-15 18:05:54
Slug: directory-listing-dangerous
Category: security
Summary: Post on Dangers of Directory listing, explained in a lucid and simple ma$
Cover: http://www.acunetix.com/wp-content/uploads/2012/11/backup-dir3.png



While browsing web pages, most of us expect to see only the pages offered by the website. For instance, if you are reading this blog, you will only be expected to see my landing page, posts, tags and the author information. I'll really not want to you take a look at my admin panel or the other administrative facilities of this blog. This not only keeps my blog neat and to-the-point but also reduces the risk of attacks.

So, let's assume that you are a hacker and want to gather information about my website. As the first step, you'll naturally have to find how my files are arranged/segregated. But how do you do it?

Yes.Browsers! A powerful application which gets more powerful every other day. If you didn't know,every browser lets you view the source of any website by right-clicking and selecting `Inspect Element`. Let's do it. Go to any website, say *Google*. Now there's a nice colourful logo and it is an image. Images have to be stored somewhere to be able render it in a web-page. Let's find out where Google is storing it's doodle. If everything goes right, you'll see the location of the image in the CSS rules in the right-bottom corner. Something like this:
![](images/cssrule.png)

Awesome. Google stores their data in `http://google.com/images/branding/googlelogo/lx/`. Hmm, but that page is giving me a 404 error when visited.Let's try visiting the image URL **as such**.

`https://www.google.co.in/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png`

It works! What does that mean? Google managed to restrict your access to the folder that the image is in, but gave you access to the particular image. Google doesn't want you to see the entire contents of the folder because it might contain a lot of stuff that is not relevant for you. We just saw a classical example of Directory Listing being disabled.

Let's look at another website. This time, a less secure one. I have setup an example on my website to demonstrate Directory listing. Go ahead and visit :
`http://www.sachinwrites.xyz/sandbox/`

You will encounter this page :
![](images/Screenshot-from-2016-01-15-22-56-00.png)

As I mentioned earlier, every image has to be stored somewhere in some form or the other. Go ahead and do an `Inspect Element` on the Image. You will see that the image is stored in `/storage/sysadmin.jpg`. Go-to `https://sachinwrites.xyz/sandbox/storage/sysadmin.jpg` and you'll have the full-image in front of you. Let us try to look into the folder of the image. Remove the image name from the URL and see what you get.

![](images/Screenshot-from-2016-01-15-23-01-03.png)

You are able to see the contents of the entire folder as the developer forgot to block Directory Indexes. Have fun exploring the new-found folder ;)

**How exactly is this undesirable?**

As you might have noticed, it reveals everything present in the folder. It might include sensitive documents, login credentials, php backup files, zip files and more. This can be dangerous from the security point of view.

**How to prevent Directory Listing?**

There are a lot of ways to do it. The easiest and the most undesirable way of doing it is to put a blank `index.html` page in every folder of your website. This way, directories won't be listed.

The better way of doing it is by using a `.htaccess` file on an Apache server. You don't need an `.htaccess` for nginx server. As nginx wiki says :
 > If you need .htaccess [with Nginx], you're probably doing it wrong.

Coming back, to prevent directory listing on an entire webserver, just write `Options -Indexes` in the `.htaccess` file and you're good to go.
The same can also be done in the apache configuration files. Also, for `.htaccess` to work properly, you need to set allow overrides in the Apache configuration files. I'll leave that part for you to figure out.

There were numerous instances of a website getting pwned just because of the fact that the developer was either too lazy or stupid to block it. Directory Listing is always the first step for gathering information about a website, according to me. To conclude with, here's a bonus meme :

![](images/bill.jpg)

Hope you liked the post. Comment your thoughts below and I'd be more than happy to hear from you. Cheers.
