---
layout: page
title: '2. Using PigPen.py'
permalink: /Usage/
---

# Using PigPen.py
Document needs work.

## Menu:
A messy work in progress:

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
Choice?
```

## Status indicators:
User and post status indicators:

* `u:number` = pnut user id,
* `+f` = followed?
* `+F` = follower?
* `*` = bookmarked?
* `rp` = reposted?
* `[u]` = message unread indicator,
* `id:` = post id,
* `rep:` = replying to post,
* `thd` = in thread,
* `pnut u:` = app user
* `c:` = channel creator.

## At this stage in lieu of further explanation here's a simple (large) dump from the running app:

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
 ------------------------------- x
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

## Next steps:
Go to the [Technical](30-technical.md) primer to see what's going on behind the scenes.
