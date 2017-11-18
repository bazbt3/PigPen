# What is 'PigPen'?
A Python application to allow interactions with the [pnut.io](https://pnut.io) social network.  My work here covers the absolute basics.

This document covers v0.3.0 onwards.

## A recent 'screenshot':

```
| PigPen | pnut u:@bazbt3
gg global timeline  gt your timeline
p  post     rp repost   gm mentions
r reply     gth getthrd gp getpost
b bookmark  gb bookmrks gh 'hashtag'
f follow    gu getuser  gi interacts
msg message gms getmsgs gs getsubs
gc getchanl sub subscribechannel
| help=menu exit=exit
Choice? gp
Get postnum? 213140
--------------
@dasdom: [u:19+f+F]
2017-10-28 19:41:31+00:00 []
@bazbt3 \o/
 id:213140 rep:213130 thd:213027
---------------
Choice? gt
---------------
@jws: [u:7+f+F]
2017-11-15 20:03:13+00:00 []
@schmidt_fu Probably the set you don’t have to follow into the bathroom.
 id:226300 rep:226243 thd:226243
 ------------------------------- 
@adiabatic: [u:172+f]
2017-11-15 20:06:46+00:00 []
@EchoDunk I made a paper wallet. There’s nothing in it yet. 
 id:226302 rep:226114 thd:226114
 ------------------------------- gth
---------------
@EchoDunk: [u:225]
2017-11-15 15:05:54+00:00 []
Speaking of #Bitcoin, whats in your wallet pnuts? Satoshi, whole coins? Inquiring minds want to know. 
 id:226114 thd:226114
 ------------------------------- 
@adiabatic: [u:172+f]
2017-11-15 20:06:46+00:00 []
@EchoDunk I made a paper wallet. There’s nothing in it yet. 
 id:226302 rep:226114 thd:226114
 ------------------------------- help
  Inline interactions menu:
  [enter]=next r=reply rp=repost
  b=bookmark gth=get thread
  x=exit
 ------------------------------- 
-back to main menu-

-back to list-
-back to main menu-

Choice? gu
Get data, usernum? 1

33MHz - human
Robert
en_US
America/Chicago
@pnut developerd
#🐝 keeper

posts: 11441
followers: 336
following: 181
bookmarks: 357

Choice? exit
 
You chose 'exit': Goodbye!
```

As you can see, there are layout bugs aplenty. And ordinary bugs too.

## What I needed to make this work
* A [pnut.io](https://pnut.io) account; no [developer account](https://pnut.io/dev) is required for single-user apps,
* Python, via the iOS [Pythonista app](http://omz-software.com/pythonista/). Note: I'm converting the application from Python 2.7 to 3.5 (see the documentation.)
* [`StaSh`](https://gist.github.com/CodyKochmann/4d6b40e77ba862e634185a038d2c3f13), a bash-like shell for Pythonista, to give `pip`, which allows installation of… 
* @33MHz & @thrrgilag's [`PNUTpy`](https://github.com/pnut-api/PNUTpy) library,
* Access to the good people of pnut.io, for when comprehension failed,
* Half a brain.

### Repo structure:
If you want to know more, the most important things to look at here are:

* The **[Documentation.](/docs/00-index.md)**
* The [CHANGELOG.](CHANGELOG.md)
* The **PigPen.py** app, obviously.  The code comments will likely always be more useful than the documentation,
* This README file.

## Why did I do this?
Good question.

## Why 'PigPen'?
App names are chosen throughout the pnut.io developer community to reflect the pnut (peanut) name. After a *lot* of thought I decided to choose PigPen from the Peanuts show character Pig-Pen; he's a scruffy boy without a name.

Incidentally, it took longer choosing the app name than it did to get to the first release to GitHub!
