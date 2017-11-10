# Using PigPen.py
Document needs work.

## Menu:
A messy work in progress:

```
| PigPen | pnut u:@bazbt3 |
menu=menu exit=exit
p  post     rp repost   gm mentions
r reply     gp getpost  gt getthread
msg message gm getmsgs  gs getsubs
gc getchanl sub subscribechannel
b bookmark  gb bookmrks gh hashtag
f follow    gu getuser  gi interacts
gt your tl  gg global
Choice?
```

## Status indicators:
User and post status indicators:

* User id,
* `+f` = followed?
* `+F` = follower?
* `*` = bookmarked?
* `rp` = reposted?
* `id:` = post id,
* `rep:` = replying to post,
* `thd` = in thread.

## At this stage in lieu of further explanation here's a simple (large) dump from the running app:

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
---------------------------------
@bazbt3: [u:175+f+F]
2017-11-09 19:42:34+00:00 []
@skematica Power!!! Actually, the idea of the near-infinite subwoofer interests me; I'm wondering how to make one. Probably not cereal boxes.
// @bazbt3 @schmidt_fu
 id:222017 rep:221979 thd:221882
---------------------------------
@bazbt3: [u:175+f+F]
2017-11-09 19:54:57+00:00 []
@schmidt_fu "Infinite speakers around you goes without saying"; that's easy for *you* to say. :)
// @bazbt3
 id:222026 rep:222004 thd:221882
---------------------------------
@bazbt3: [u:175+f+F]
2017-11-09 19:57:12+00:00 []
@bazbt3 It shouldnt be possible Baz.
 id:222028 rep:222027 thd:222027
---------------------------------
@bazbt3: [u:175+f+F]
2017-11-09 19:58:29+00:00 []
@bazbt3 But it does it anyway. :/
// @bazbt3
 id:222029 rep:222028 thd:222027
---------------------------------
@bazbt3: [u:175+f+F]
2017-11-09 20:00:59+00:00 []
@bazbt3 It's still happening.
 id:222033 rep:222027 thd:222027
---------------------------------
@bazbt3: [u:175+f+F]
2017-11-09 20:01:48+00:00 []
@bazbt3 One more try and then I'll remove it.
// @bazbt3
 id:222035 rep:222033 thd:222027
---------------------------------
@bazbt3: [u:175+f+F]
2017-11-09 20:10:24+00:00 []
@bazbt3 I removed it.
 id:222042 rep:222033 thd:222027
---------------------------------
@skematica: [u:411+f+F]
2017-11-09 20:20:12+00:00 []
@bazbt3 probably not cans on a string either ☺️ @schmidt_fu
 id:222051 rep:222017 thd:221882
---------------------------------
@skematica: [u:411+f+F]
2017-11-09 20:20:54+00:00 []
@bazbt3 different kinds of pie 🥧 (mine will be sweet potato or pumpkin) 
 id:222053 rep:222045 thd:222045
---------------------------------
@schmidt_fu: [u:106+f+F]
2017-11-09 20:24:28+00:00 []
@bazbt3 Ok, I'll settle for #GreenMonday because we have 25,000 visitors in the city of #Bonn for the freakin' climate conference!

#COP23
 id:222055 rep:222045 thd:222045
---------------------------------
@schmidt_fu: [u:106+f+F]
2017-11-09 20:25:34+00:00 [rp]
@bazbt3 Always be yourself! Except when you can be Batman: Then, be Batman!
 id:222057 rep:222028 thd:222027
---------------------------------
@ukhaiku: [u:251+f+F]
2017-11-09 20:42:25+00:00 []
@bazbt3 She’s 18months old now. I don’t know where the time has gone!
 id:222087 rep:221825 thd:219056
---------------------------------
@Streakmachine: [u:97+f+F]
2017-11-09 21:00:06+00:00 []
@schmidt_fu Words to live by! @bazbt3
 id:222108 rep:222057 thd:222027
---------------------------------
@skematica: [u:411+f+F]
2017-11-09 22:56:32+00:00 []
@bazbt3 yes you may! Be my guest ☺️
 id:222173 rep:222119 thd:222045
---------------------------------
@skematica: [u:411+f+F]
2017-11-09 22:56:45+00:00 []
@bazbt3 will dooooo 
 id:222174 rep:222064 thd:222045
---------------------------------
@skematica: [u:411+f+F]
2017-11-09 23:02:28+00:00 []
@bazbt3 sounds good 👌🏼
 id:222182 rep:222180 thd:222045
---------------------------------
@Streakmachine: [u:97+f+F]
2017-11-10 09:26:18+00:00 []
@bazbt3 Do it! @schmidt_fu
 id:222545 rep:222155 thd:222027
---------------------------------

Choice? r
Reply to postnum? 222545
---------------
Replying to @Streakmachine:
@bazbt3 Do it! @schmidt_fu
---------------
Write now (\n): Later this afternoon, it's an odd day today.
ok
Choice? 
```

## Next steps:
Go to the [Technical](/docs/30-technical.md) primer to see what's going on behind the scenes.
