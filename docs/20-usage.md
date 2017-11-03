# Using PigPen.py

## At this stage in lieu of explanation here's a simple (large) dump from the running app:

```
PigPen menu:
 p post         m mentions(user)
 r reply        g get post
 rp repost      gt get thread
 f follow
 b bookmark     h hashtag
 msg message    gm get msgs
 s subscribed   gc get channel
menu show menu ------- Exit quit

Choice? m
user_id: 175
---------------
@dasdom:  p:213140 t:213027
2017-10-28 19:41:31+00:00
@bazbt3 \o/
---------------
@33MHz:  p:213150 t:213108
2017-10-28 19:55:44+00:00
@bazbt3 huh. May need to run it through 2to3. Been a while since I looked at it, though.
---------------
@33MHz:  p:213155 t:213108
2017-10-28 20:00:43+00:00
@bazbt3 yeah.
---------------
@thrrgilag:  p:213169 t:213108
2017-10-28 20:26:29+00:00
@bazbt3  @33MHz You create a post with the reply_to parameter referencing the post you are replying to.
---------------
@unixb0y:  p:213211 t:212906
2017-10-28 21:17:39+00:00
@bazbt3 Haha :D 👍 Good name is important 😉 @thrrgilag @33MHz 
---------------
@jws:  p:213219 t:213108
2017-10-28 21:37:37+00:00
@33MHz Or use six to target both. I think there are still distros shipping 2.x as standard. @bazbt3
---------------
@muncman:  p:213253 t:213027
2017-10-28 23:21:28+00:00
@dasdom Thank you! :D @bazbt3
---------------
@hutattedonmyarm:  p:213491 t:213481
2017-10-29 11:09:04+00:00
@bazbt3 Oh nice! I'm currently trying to document PNUTpy whenever I find the time for it. This [files.pnut.io] is how far I've come. (Spoiler: not very far)
---------------
@hutattedonmyarm:  p:213504 t:213481
2017-10-29 11:46:43+00:00
@bazbt3 I'm also a Python noob, so I'll need some time. Yes, I have! My plan was to create a fork when the first section is complete, and submit PRs. Thinking about it, I could do that now, as the 'files' part is mostly done!
---------------
@doctorlinguist:  p:213834 t:213732
2017-10-29 21:00:07+00:00
@bazbt3 there you go :)
---------------
@jws:  p:213908 t:213886
2017-10-29 23:43:52+00:00
@bazbt3 More of an Elm Street kind of guy?
---------------
@33MHz:  p:214637 t:214632
2017-10-31 01:01:13+00:00
@bazbt3 RSS posting like this makes me wonder if people wouldn't be better served posting these to channels in some cases. Channels being nice for purpose-driven posting.
---------------
@schmidt_fu:  p:214999 t:214632
2017-10-31 12:01:23+00:00
@33MHz @bazbt3 Posting to channels would be a nice addition to #rtpaasfp anyway. Apart from that, the current posting rate doesn't seem alarming to me, <30 posts/hour on the most days, even with the last 100 users added.
---------------
@blumenkraft:  p:215000 t:214632
2017-10-31 12:03:08+00:00
@schmidt_fu posing to channels for RtPaaS (fP) is already on the issues list. :) @33MHz @bazbt3 
---------------
@schmidt_fu:  p:215001 t:214632
2017-10-31 12:03:50+00:00
@blumenkraft Very cool! @bazbt3 @33MHz 
---------------
@bazbt3:  p:216136 t:216133
2017-11-01 22:01:45+00:00
Heh! Getting there @bazbt3. :)
---------------
@33MHz:  p:216137 t:216133
2017-11-01 22:02:20+00:00
@bazbt3 sweet :D
---------------
@jws:  p:216149 t:216133
2017-11-01 22:24:51+00:00
@bazbt3 Pnut qua parser IF ;) @33MHz
---------------
@jws:  p:216603 t:216429
2017-11-02 12:29:42+00:00
@bazbt3 Suggest you check out:

KeepAChangeLog.com to polish your changelog format.

Multiline strings with “”” delimiters to simplify some of your text displays.

f-strings to simplify interpolation.
---------------
@jws:  p:216621 t:216429
2017-11-02 12:40:10+00:00
@bazbt3 Mostly that grouping by Added, Removed, Changed, Fixed, etc sections makes it a lot easier to get the gist of a version’s changes.
---------------

Choice? gm
channelnum: 779
---------------
@bazbt3:  p:31271 t:31271
2017-09-30 14:00:20+00:00
No. ;)
---------------
@blumenkraft:  p:31272 t:31272
2017-09-30 14:14:57+00:00
ok!
---------------
@blumenkraft:  p:31273 t:31273
2017-09-30 14:15:14+00:00
let me think.
---------------
@bazbt3:  p:31283 t:31283
2017-09-30 16:06:20+00:00
Been busy, sorry. Wondering what to suggest myself. Hard
---------------
@blumenkraft:  p:31424 t:31424
2017-10-01 15:07:09+00:00
ok, for real. i propose bitcoin monday as a thememonday (what the fuck else,eh?)
---------------
@unixb0y:  p:31720 t:31720
2017-10-02 22:17:51+00:00
Hi guys 😊 
---------------
@unixb0y:  p:31721 t:31721
2017-10-02 22:17:55+00:00
Whattuppppppppp
---------------
@unixb0y:  p:31722 t:31722
2017-10-02 22:18:05+00:00
9th of October is great 😊 
---------------
@unixb0y:  p:31723 t:31723
2017-10-02 22:18:25+00:00
Let's make it always on the 2nd monday like back in the day :)
---------------
@unixb0y:  p:31724 t:31724
2017-10-02 22:19:15+00:00
My suggestion would be to use an image of your favourite sports (whether you do it yourself or not) 😊 
---------------
@33MHz:  p:32053 t:32053
2017-10-03 03:37:59+00:00
#themeMonday suggestion: broke technology
---------------
@hutattedonmyarm:  p:32128 t:32128
2017-10-03 09:14:38+00:00
Suggestion: Books (or maybe ‚Media‘ as it’s more general)
---------------
@bazbt3:  p:32381 t:32381
2017-10-06 04:54:25+00:00
#ThemeMonday suggestions so far: BitCoin, Sports, BrokeTech, Books & Uncertain - poll soon
---------------
@bazbt3:  p:32382 t:32382
2017-10-06 04:57:49+00:00
#ThemeMonday is on 9 October! @blumenkraft set up this Patter (chat) room - come on in! :)
---------------
@bazbt3:  p:32383 t:32383
2017-10-06 05:04:56+00:00
If you're unfamiliar with #ThemeMonday, go here: https://wiki.pnut.io/ThemeMonday
---------------
@schmidt_fu:  p:32430 t:32430
2017-10-06 12:58:45+00:00
I tend to second the #BooksMonday, since any kind of literacy and education seem to be utterly missing from politics in many countries currently.
---------------
@bazbt3:  p:32433 t:32433
2017-10-06 13:09:24+00:00
@schmidt_fu We need a #ThemeMonday poll setting up
---------------
@bazbt3:  p:32466 t:32466
2017-10-06 18:26:12+00:00
It's nearly #ThemeMonday and we now have a poll! Vote now to choose a theme. For Monday. :)

https://doodle.com/poll/5qmippkn66cu5i8r
---------------
@bazbt3:  p:32622 t:32622
2017-10-07 17:11:08+00:00
#ThemeMonday
Don't forget to vote in the poll for our Monday theme!

https://doodle.com/poll/5qmippkn66cu5i8r

It's nearly Sunday and we currently have a tie!!
We don't have many votes yet because I was late posting, after an *Uncertain* week, no time. ;)
---------------
@bazbt3:  p:32763 t:32763
2017-10-08 16:23:58+00:00
Our theme for tomorrow is
#BookMonday!
I closed the poll, here:
https://doodle.com/poll/5qmippkn66cu5i8r

A shame I didn't prepare early, again. Next month I'd appreciate being kicked around a bit to remind me, early.
---------------

Choice? 
```

## Next steps:
Go to the [Technical](/docs/30-technical.md) primer to see what's going on behind the scenes.
