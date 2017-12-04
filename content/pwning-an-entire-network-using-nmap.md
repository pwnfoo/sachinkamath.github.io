Tags: college,security,hacking
Title: [Repost] Pwning an entire network using nmap
Date: 2014-12-28 18:03:00
Slug: pwning-an-entire-network-using-nmap
Cover: https://nmap.org/movies/matrix/Nmap_Matrix_Screen_Huge.jpg
Category: security


Originally posted on [HackerSpace](https://bufferoutofbounds.wordpress.com/2014/12/29/pwning-an-entire-network-using-nmap/).


When every friend of mine was busy studying for the finals,only thing I could do was to think in what subjects I would flunk and how pathetically I would screw my GPA. Though I tried my best,only thing I was able to do was worry,worry and worry.
Thinking of taking a break(from not studying and using FB),I thought it would be a better idea to use Whatsapp for a while.
I switched on my Internet. Other than the boring texts from the groups,I didn’t get anything(as usual xP). After some time,beep beep and I get a text from Sachin who is my junior(most of the time hyperactive) Then was suggesting me if we could try to get access to the cameras around our college infrastructure.

The idea seemed nice. And since I was doing almost nothing,I thought it would be better to do something interesting.

So,what have we got?
Nothing except the IP of FTP address which we use very often in our labs to download books and questions.
It was of the range 172.17.171.*
Thought we would do a sweep of 172.17.171.0-255 range.
Being so stupid,I tried to write a script which scans all the IP’s within that range. Though I could make it work,I wasn’t able to make it scan fast enough.
But,we got 7 IP’s which were up in that range. So,we took one IP and tried opening.

Bazinga! It was a surveillance camera. Obviously it was password protected.
But sad. They forgot to change the default password of the camera. So we did Google for the specific camera’s default user name and password.
We’re in! We never thought it would happen. That camera was of that of my college’s library.

We started thinking about getting access to all the cameras(Just for fun,though xP).
It was becoming late and I haven’t studied for my exam yet.
So Sachin said that he would volunteer for the job of entire ping sweep of all 65535 IP’s in that range. This time we thought we would take help from Nmap which is blazingly fast.
It took just minutes to scan the entire network and we got 1212 IP’s which were live.

Again! The next problem.How can we know if that specific IP corresponds to a camera or not?
I did a curl of the webpage and checked using grep if that site’s source code contained the word ‘XYZBrand Camera’. Bingo! We got all the cameras in our network. But certain of the passwords didn’t match with the default ones. So we brute forced everything.
We got into all the cameras of our infrastructure.

But,wait! What about the rest of the IP’s? We tried different search terms like ‘Router’,’Switch’,’Firewall’. And at last,we got all the IP’s of Cameras + Routers + Switches + Firewall and some blackbox shit which we couldn’t understand what it is.
So we thought of trying the default password for each service. If not,we brute forced and got access.

**Mission accomplished!**

(I get it. I screwed up my exams and even flunked in one subject which I thought I would definitely pass. Karma -_- I am planning to study for that once this post is done.)

Lessons learned :


* Nmap is always the best.
* Study for your final exams.
* Never forget the basics of penetration testing.
* Never report this to college officials.
Chances are high that they wouldn’t give a damn or embarrass for pointing out vulnerabilities in their server.

(The characters mentioned in this story are real and are having a tough time in college to study for the exams and never get grades up to their parent’s expectation)
