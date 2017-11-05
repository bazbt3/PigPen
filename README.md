# What is 'PigPen'?
A Python 2 application to interact with the [pnut.io](https://pnut.io) social network.  My work here covers the absolute basics.

This document covers v0.01.21 onwards.

## A recent screenshot

```
PigPen | menu=menu exit=exit
 p post        m mentions(user)
 r reply       g get post
 rp repost     gt get thread
 f follow      gh get hashtag
 b bookmark    gb get bookmarks
 u unified tl  gg get global tl
 msg message   gm get msgs
 s subscribed  gc get channel
Choice? g
postnum: 213140
@dasdom:
2017-10-28 19:41:31+00:00
@bazbt3 \o/
---------------
Choice? m
user_id ([return]=me): 
---------------
@schmidt_fu: [u:106+f+F]
2017-10-31 12:01:23+00:00 []
@33MHz @bazbt3 Posting to channels would be a nice addition to #rtpaasfp anyway. Apart from that, the current posting rate doesn't seem alarming to me, <30 posts/hour on the most days, even with the last 100 users added.
 id:214999 rep:214637 thd:214632
…
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
