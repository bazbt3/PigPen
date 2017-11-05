# Using PigPen.py
Document needs work.

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

PigPen | menu=menu exit=exit
 p post        m mentions(user)
 r reply       g get post
 rp repost     gt get thread
 f follow      gh get hashtag
 b bookmark    gb get bookmarks
 u unified tl  gg get global tl
 msg message   gm get msgs
 s subscribed  gc get channel
Choice? m
user_id ([return]=me): 
---------------
@schmidt_fu: [u:106+f+F]
2017-10-31 12:01:23+00:00 []
@33MHz @bazbt3 Posting to channels would be a nice addition to #rtpaasfp anyway. Apart from that, the current posting rate doesn't seem alarming to me, <30 posts/hour on the most days, even with the last 100 users added.
 id:214999 rep:214637 thd:214632
---------------------------------
@blumenkraft: [u:15+f+F]
2017-10-31 12:03:08+00:00 []
@schmidt_fu posing to channels for RtPaaS (fP) is already on the issues list. :) @33MHz @bazbt3 
 id:215000 rep:214999 thd:214632
---------------------------------
@schmidt_fu: [u:106+f+F]
2017-10-31 12:03:50+00:00 []
@blumenkraft Very cool! @bazbt3 @33MHz 
 id:215001 rep:215000 thd:214632
---------------------------------
@bazbt3: [u:175+f+F]
2017-11-01 22:01:45+00:00 []
Heh! Getting there @bazbt3. :)
 id:216136 rep:216133 thd:216133
---------------------------------
@33MHz: [u:1+f+F]
2017-11-01 22:02:20+00:00 []
@bazbt3 sweet :D
 id:216137 rep:216133 thd:216133
---------------------------------
@jws: [u:7+f+F]
2017-11-01 22:24:51+00:00 [* rp]
@bazbt3 Pnut qua parser IF ;) @33MHz
 id:216149 rep:216142 thd:216133
---------------------------------
@jws: [u:7+f+F]
2017-11-02 12:29:42+00:00 [*]
@bazbt3 Suggest you check out:

KeepAChangeLog.com to polish your changelog format.

Multiline strings with “”” delimiters to simplify some of your text displays.

f-strings to simplify interpolation.
 id:216603 rep:216429 thd:216429
---------------------------------
@jws: [u:7+f+F]
2017-11-02 12:40:10+00:00 []
@bazbt3 Mostly that grouping by Added, Removed, Changed, Fixed, etc sections makes it a lot easier to get the gist of a version’s changes.
 id:216621 rep:216620 thd:216429
---------------------------------
@hutattedonmyarm: [u:46+f+F]
2017-11-04 22:10:42+00:00 [*]
Congratulations @bazbt3, you are now a member of #PnutClub 🥜 (2016+ posts)! Next: ☎️ at 2600 posts
 id:218326 rep:204782 thd:204752
---------------------------------
@hutattedonmyarm: [u:46+f+F]
2017-11-04 22:11:21+00:00 []
Congratulations @bazbt3, you are now a member of #PnutClub 🥜 (2016+ posts)! Next: ☎️ at 2600 posts
 id:218335 rep:204782 thd:204752
---------------------------------
@hutattedonmyarm: [u:46+f+F]
2017-11-04 22:12:34+00:00 []
Congratulations @bazbt3, you are now a member of #PnutClub 🥜 (2016+ posts)! Next: ☎️ at 2600 posts
 id:218357 rep:204782 thd:204752
---------------------------------
@hutattedonmyarm: [u:46+f+F]
2017-11-04 22:12:38+00:00 []
Congratulations @bazbt3, you are now a member of #PnutClub 🥜 (2016+ posts)! Next: ☎️ at 2600 posts
 id:218360 rep:204782 thd:204752
---------------------------------
@hutattedonmyarm: [u:46+f+F]
2017-11-04 22:16:30+00:00 []
@bazbt3 I broke the authentication. That's why it's going nuts and posting as me
 id:218380 rep:218379 thd:204752
---------------------------------
@hutattedonmyarm: [u:46+f+F]
2017-11-04 22:25:28+00:00 []
@bazbt3 Glad I found the problem reasonably fast! I switched the auth to SSL, but forgot to update the redirect URI in the dev dashboard, so shit went haywire when trying to re-authenticate (which I had to do for upcoming features)
 id:218392 rep:218387 thd:204752
---------------------------------
@jws: [u:7+f+F]
2017-11-05 00:01:28+00:00 []
@bazbt3 Guy Fawkes night? I forget that’s so near Halloween. No-one celebrates it here.
 id:218431 rep:218323 thd:218323
---------------------------------
@schmidt_fu: [u:106+f+F]
2017-11-05 06:29:03+00:00 []
@bazbt3 I need to catch up on this. You're writing an pnut app for private tokens in Python?
 id:218588 rep:218456 thd:218456
---------------------------------
@schmidt_fu: [u:106+f+F]
2017-11-05 12:01:31+00:00 []
@bazbt3 Oh, great! I understand it's targeted at an app platform on iOS - but have you run it somewhere else? Is there anything specific to Pythonista?
 id:218746 rep:218737 thd:218456
---------------------------------
@jws: [u:7+f+F]
2017-11-05 12:09:00+00:00 [*]
@schmidt_fu Pythonista’s default set of libraries includes some nice-to-haves that aren’t in the stdlib but are readily available with pip. There are Pythonista-specific libs for UI and integrating with iOS system features, but I doubt @bazbt3 is using any
 id:218749 rep:218746 thd:218456
---------------------------------
@dasdom: [u:19+f+F]
2017-11-05 14:27:25+00:00 []
@bazbt3 I’m in the example! \o/
 id:218835 rep:218827 thd:218456
---------------------------------
@blumenkraft: [u:15+f+F]
2017-11-05 16:10:45+00:00 []
@bazbt3 it came to mind looking at the wiki. ;)
 id:218934 rep:218851 thd:218840
---------------------------------

Choice? 
```

## Next steps:
Go to the [Technical](/docs/30-technical.md) primer to see what's going on behind the scenes.
