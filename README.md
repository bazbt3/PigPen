# What is 'PigPen'?
A Python 2 application to interact with the [pnut.io](https://pnut.io) social network.  My work here covers the absolute basics.

This document covers v0.01.31 onwards.

## A recent screenshot

```
| PigPen | pnut u:@bazbt3 |
menu=menu exit=exit
p  post     rp repost   gm mentions
r reply     gp getpost  gt getthread
msg message gms getmsgs gs getsubs
gc getchanl sub subscribechannel
b bookmark  gb bookmrks gh hashtag
f follow    gu getuser  gi interacts
gt your tl  gg global
Choice? gp
Get postnum? 213140
--------------
@dasdom: [u:19+f+F]
2017-10-28 19:41:31+00:00 []
@bazbt3 \o/
 id:213140 rep:213130 thd:213027
---------------
Choice? gm
User mentions, userid? [return]=me: 
---------------
@bazbt3: [u:175+f+F]
2017-11-09 18:49:16+00:00 []
@schmidt_fu It can actually do ∞.2, but managing the power requirements is beyond my abilities.
// @bazbt3
 id:221970 rep:221906 thd:221882
---------------------------------
@skematica: [u:411+f+F]
2017-11-09 18:55:56+00:00 []
@bazbt3 😂 21.1 gigawatts! @schmidt_fu
 id:221979 rep:221970 thd:221882
---------------------------------
@schmidt_fu: [u:106+f+F]
2017-11-09 19:26:28+00:00 []
@bazbt3 Infinite speakers around you goes without saying, but you put *2* in front??? That's nothing for the faint of heart!! ;-)
 id:222004 rep:221970 thd:221882

...

@Streakmachine: [u:97+f+F]
2017-11-10 09:26:18+00:00 []
@bazbt3 Do it! @schmidt_fu
 id:222545 rep:222155 thd:222027
---------------------------------

Choice? 
```

## What I needed to make this work
* A [pnut.io](https://pnut.io) account; no [developer account](https://pnut.io/dev) is required for single-user apps,
* Python 2, via the iOS [Pythonista app](http://omz-software.com/pythonista/)
* [`StaSh`](https://gist.github.com/CodyKochmann/4d6b40e77ba862e634185a038d2c3f13), a bash-like shell for Pythonista, to give `pip`, which allows installation of… 
* @thrrgilag's [`PNUTpy` library](https://github.com/pnut-api/PNUTpy),
* Access to the good people of pnut.io, for when comprehension failed,
* Half a brain.

### Repo structure:
If you want to know more, the most important things to look at here are:

* The **[Documentation.](/docs/00-index.md)**  A work in progress,
* The [CHANGELOG,](CHANGELOG.md)
* The **PigPen.py** app, obviously.  The code comments will likely always be more useful than the documentation,
* This README file.

## Why did I do this?
Good question.

## Why 'PigPen'?
App names are chosen throughout the pnut.io developer community to reflect the pnut (peanut) name. After a *lot* of thought I decided to choose PigPen from the Peanuts show character Pig-Pen; he's a scruffy boy without a name.

Incidentally, it took longer choosing the app name than it did to get to the first release to GitHub!
