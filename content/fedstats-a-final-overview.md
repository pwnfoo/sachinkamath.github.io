Tags: fedora,gsoc,code,python
Title: fedstats - A final overview
Date: 2016-06-21 06:01:45
Slug: fedstats-a-final-overview
Category: gsoc


Mid term evaluations of GSoC starts today. It's been a month since it all started and I'd like to blog (brag) about what I've done so far.

To start with, here are the list of things I was assigned to work on till the mid-term and the current status of it :

 <OL>
<LI> **Statistics Tool**
<UL>
<LI> Automate Event Report Visualization
   *<strong>STATUS :</strong> Check. The tool was used to gen rate user statistics for PyCon US and can be used for any future events.* [[Link]](https://docs.google.com/spreadsheets/d/11vOxzGmZKagfHYlkW4dXY4EovRcUXVxOJ5OsEId0DBE/edit#gid=0)

<LI> Support for multiple formats of Output
 *<strong>STATUS :</strong> Check. The tool is feature-rich with support for SVG, PNG, Text, Markdown, CSV and Gource.*

<LI> Pull data of individual users / multiple users for reporting.
 *<strong>STATUS :</strong> Check. The tool uses datagrepper to generate statistics. If it's on the datagrepper, it should be covered in the stats. Since the tool is based on arguments, stats can easily be generated for multiple users*

<LI> Document code to help future contributors.
 *<strong>STATUS :</strong> Check. The tool has a README which explains the features and the working on the tool in a concise and clear way.*  [[Link to README]](https://pagure.io/gsoc-stats/blob/master/f/README.md)
</UL>
<LI>**Onboarding Series**
<UL>
<LI>Identify OnBoarding badges
*<strong>STATUS :</strong> Check. The CommOps onboaring badge is now a ticket in the Design Trac.*

<LI>Identify steps to make onboarding better
*<strong>STATUS :</strong> Check. The discussion is scattered across all the CommOps meeting that we have had in this month.*</UL>
</OL>

<hr>

#####Stats-Tool : Overview
<br>

**Features :**

* Gather data from datagrepper for analyzing and visualizing data.

* Support for SVG, PNG, CSV, Markdown, Text and gource style outputs. *(Working on PDF and HTML - HTML is currently halted due to a bug in the `python-grip` module. Waiting for the developer's response on it)*

* Generate category-wise reports (pie / donuts)


**This week's work:**

* Added support for gource style outputs *(Inspiration - [fedmsg2gource](https://github.com/ralphbean/fedmsg2gource))*

* Text output mode now branches out to two. The default text mode only prints the statistics onto a text while and when combined with `--log`, it dumps the category-wise activities into the text file.

* Extended the scope of the tool by adding `--start` and `--end` arguments which take in dates in the format **MM/DD/YYY**. Useful for generating event reports.

* `--user=ALL` argument added. This is useful pulling ALL the messages from datagrepper. To be combined with either `--delta` which defaults to delta of one week or `--start` and `--end` arguments.

* Added more options to interactive mode and set defaults.

* Code cleanup and minor enhancements.

**EDIT :** I have generated statistics of all the Google Summer of Code Interns for the mid term. If you are interested, take a look [here](https://goo.gl/Z3wRxj) and [here](https://github.com/sachinkamath/fedstats-data/blob/master/interns-mid-term/).


**Repository Statistics :**

Total Issues : 13
Total Fixed : 11
Open Issues : 2  *(External Bugs)*
