# CHANGELOG
(Most recent on top.)

### TODO:
* Change avatar (a precursor to other file operations in v0.3.)
* Pushed goal of display of longer timelines back from v0.3 to v0.4.

**Parallel project,** ***was intended for*** **a future pnut.io \#Hackathon:**    
`ppmentions.py` created, from a suggestion by @schmidt_fu for a list of mutual mentions. No external documentation; the intention is to roll the code into the main app.

### 2017-12-23: v0.3.23 (Broadcast):
* Added: -
* Changed: -
* Deprecated: `sp` 'spam channel' (with mentions) removed from main menu in favour of `bc` broadcast messages to channel subscribers.
* Removed: -
* Fixed: Broadcast now sends a message every 3.2 seconds. (Developer previously failed at the maths required to ensure PigPen wasn't rate-limited. Doh!)
* Security: -

### 2017-12-22: v0.3.22 (Broadcast):
* Added: Broadcast a message to every subscriber to a channel. Currently needs some manual input, i.e. the channel name or a hashtag or both.
  * **Future plans:**
  * Automatically add the channel name and ask for hashtag and header text.
  * Automatically crosspost a post to the channel and thus public timelines.
* Fixed: Tiny bug fixes, and terminology and layout tweaks.

### 2017-12-21: v0.3.21 (Meh):
* Fixed: xpost now sends both the message *and* now the post.

### 2017-12-19: v0.3.20 (Making Flippy Floppy):
* Deprecated: Removed buggy 2-part parsing from createpost; it's just as quick to type '`p`', `[return]` and then the post text.

### 2017-12-15: v0.3.19 (Road to Nowhere):
* Changed: Both 'createpost' and 'createmessage' now parse, as badly-described in previous commits. Perhaps confusingly, createpost can use post text whereas createmessage takes just the channel number. I'm leaving 'xpost' alone, it works (for me) better with user input for channel number and post.
* Changed: Commands are now split into command and everything else following the command, not ignoring everything after the second space character as before.
* Removed: 'zpost' removed from application; totally unused since its addition.

### 2017-12-10: v0.3.18 (Pompous?):
* Added: **Testing:** ~~Spam~~`sp`: Create a message in a channel mentioning all subscribers to that channel. Not *useful* as no mention alerts are created, it may even impact privacy concerns. Ultimate intention is to 'Broadcast' messages to subscribers, but that seems a bit ambitious.
* Added: New `io` > `gf` 'Get file' retrieves an file's *data* similarly to but more abbreviated than `gmf`; not for users yet.
* Changed: Can now get an abbreviated (`gs`) or a verbose (`gs v`) listing of subscribed channels *from the main menu*. Note: Default output is currently *abbreviated* but verbose might be more *useful*, displaying the most recent message.
* Changed: `gc` user listing now returns usernames with the user ids.
* Changed: Server responses now prefixed with the interaction type.
* Changed: Tiny install documentation update.
* Deprecated: zpost removed from menu; totally unused since its addition. (Code and command remain active.)
* Removed: -
* Fixed: -
* Security: -

### 2017-12-09: v0.3.17 (Uncertain):
* Added: 'Are you sure…?' when exiting.
* Added: 1 or 2-part command+operand parsing added to 'Bookmark post', 'get thread', 'reply post' and 'repost post'.
* Changed: 'Get channel messages' renamed from `gms` to `gcm`.
* Changed: Small changes to channels part of menu.
* Fixed: 'Get channel' command now informs the user if the most recent message in a channel was deleted (if message content text does not exist.)

### 2017-12-06: v0.3.16 (Intrusive?):
* Added: 'Get channel' now has the option to display a list of subscriber ids.

### 2017-12-06: v0.3.15 (mute):
* Added: Mute/block/delete submenu starting with delete post, with mute & unmute for both channels and users.

### 2017-12-05: v0.3.14 (mmmm… pi):
* Added: `gm` get messages and `gup` get user posts now usable with 1 or 2-way parsing.

### 2017-12-04: v0.3.13 (Eh?!):
* Added: Rudimentary parsing of 1- or 2-part commands (choice-operand.) Created at the whim of the developer and for speed of implementation.
* Changed: A few tiny code updates.

### 2017-12-03: v0.3.12 (Filing system):
* Added: Files menu (but may need a better command than `io`.)
* Added: Upload an image (from the `images/` folder within the app folder.)
* Added: Development only: List the application user's files; a bit raw, no actual images displayed yet.
* Added: *Started* to work on changing the user's avatar. **It doesn't work yet** but I've had @ludolphus' assistance.
* Changed: Can now display an abbreviated subscribed channel listing before creating a message or listing the messages in a channel.
* Removed: Unused `import time`.
* Fixed: Exit when inquiring a user without a bio; app instead indicates '-no bio'.

### 2017-11-27: v0.3.11 (Nosy):
* Added: Get posts by a user.
* Added: z-posts (crap name): Use a post to create a message in a chat or private channel. Currently limited to new posts which, as x-posts already exists, is somewhat redundant. The *intent* is to change the function for replies and reposts - allowing a conversation to continue other than in 'public.'

### 2017-11-26: v0.3.10 (Numbers):
* Added: Ability to choose number of channels to be retrieved. (Default = 30, which suits a tiny screen.)
* Added: Display images in messages.
* Added: Delete post.
* Changed: The general retrieve count *default* value is now, er… not determined yet. (Somewhere between 10 and 25, to suit a tiny screen.)

### 2017-11-25: v0.3.9 (Un- the first thing!):
* Added: Ability to unsubscribe from a channel.
* Changed: (HTTP) '201' server response is now "-created", with '200' remaining at "-ok".
* Changed: Menu layout. Radical!
* Fixed: After finding a post would be too long the app now correctly reports it won't work, then displays the too-long text to allow editing before posting. (Copy and paste.)

### 2017-11-24: v0.3.8 (Borked!):
* Fixed: Functions other than `getsubscribed` can now display either a channel name or private message status instead of exiting the app; `getchannelname` function added.
* Fixed: Crossposting is again possible from a chat channel to a post. (See also Security below.) The fix in v0.3.7 worked on the phone but I believe I deleted something crucial before uploading to GitHub.
* Security: Crossposting from a private message channel to a post is now prohibited. (This status is *very* loosely security-related, there's been nothing posted here so far!)

### 2017-11-24: v0.3.7 (Tweakage):
* Changed: Subtly changed a few menus; there's a long way to go before it'll be done.
* Fixed: Chat channels with channel avatars added subsequent to the API v0.7.4 update failed to show in both `getchannel` and the `getsubscribed` listing, and broke `crosspost` (after sending the message to the channel and before creating the post.)

### 2017-11-23: v0.3.6 (Ch-ch-ch-changes):
* Added: Settings menu: The first option modifies the number of posts retrieved. Note: it's currently applied to *every* post listing, a more granular approach is *needed*.
* Added: A Windows-like `ppconfig.ini` file to allow user settings to persist between sessions. (I'm not entirely certain this is the most 'Pythonic' way to do it.) Created by the app on first run. Dependent on `import configparser`. Currently holds only the number of posts the user wishes to be retrieved.

### 2017-11-19: v0.3.5 (Docstrings):

* Added: Code: Docstrings created in every module. Probably of little consequence.
* Changed: Code: Order of functions, change in progress; maybe more logical?
* Fixed: `getchannel` now works correctly, doesn't exit the app.

### 2017-11-18: v0.3.4 (a bit Saturday-ish):
**News:** The documentation is moving to GitHub Pages so ~~might break~~is of course temporarily borked.

* Removed: `import sys` - only used in my Python 2.7 catch-all exception handling.

### 2017-11-17: v0.3.3 (Spammy images!~~A bit spammy?~~):
* Added: Display embedded images in posts. It's a bit slow and there is of course no caching.
* Added: `xp x-post` crosspost a new message created in a Patter chatroom as a post.

### 2017-11-17: v0.3.2 (A bit too raw.):
* Fixed: 'Get interactions' broke with a request for raw data; request removed.

### 2017-11-17: v0.3.1 (Nearly images!):
* Added: Display one embedded image's *indicator, URL and thumbnail URL*, i.e. the app will not yet show an inline image; one must click the link. Probably buggy. (Tested initially using post 227199.)
* Changed: `createpost` does not allow an empty post to be sent. Perhaps a bit strict, thus not implemented elsewhere.
* Changed: For replies: Reduced slashes to 1 for mentions other than the original poster. Confirms more closely to the pnut standard.
* Fixed: Better error handling: Started to target exceptions for cases where data doesn't exist, e.g. `KeyError` for accounts missing usernames and/or bio text. (Tested with accounts 175 and, a random choice of 171.)

### 2017-11-15: v0.3.0 (Embiggened!):
#### News:
**The application is now Python 3.5-only.** The 2.7 app was created due to ignorance when it initially failed. Adding `import sys` fixed the fault in the noob catch-all-then-reset exception handlers. Note: the sys calls made simply aren't necessary in Python 3.5.
#### Version numbering:
Python 3.5 application starts at v0.3.0 simply to differentiate from Python 2.
 
* Added: Moar spaghetti code.
* Changed: Increased listings from server-default 20 posts to a hardcoded 30. Not friendly yet, being displayed from earliest to latest and with no persistence, hence no version increase.
* Deprecated: Er… does all the Python 2.7 stuff count?

### 2017-11-15: v0.2.4 (Now @hutattedonmyarm):
* Added: Chat channel names now appear in the Subscribed Channels listing, a major barrier passed thanks to @hutattedonmyarm's help.    
**Bug:** May break in the Get Channel routine.
* Fixed: Attributions: PNUTpy author: @33MHz, maintainer: @thrrgilag.

### 2017-11-13: v0.2.3 (pre-@hutattedonmyarm):
* Added: Inline display of thread when listing timeline. **Bug:** Exits current listing.
* Added: Check total length, including mentions, of post being replied to and force amendment if over-long. (Wastefully copies code from createpost routine.)
* Added: Channel type indicator, `chat` or `pm`.
* Changed: Menu items: `gt` now gets timeline, `gth` gets thread.

### 2017-11-12: v0.2.2 (Help!):
* Added: Inline help: type `help` during post listings. Much tidier. See also changes for main menu update.
Added: Subscribed channel list now has a `[u]` unread status indicator and displays the username of the most recent message poster.
* Added: Because the application is feature-complete and bug-free I added an ASCII art logo in the code.
* Changed: To redisplay the menu in the main routine type `help` instead of `menu`. Changed to be consistent with inline interactions.

### 2017-11-11: v0.2.1 (Remember!):
* Fixed: Main routine now calls the reply, bookmark and repost subroutines instead of exiting.
* Fixed: *Partial fix:* Inline menu character input now starts on next line *on my phone*. (Pythonista, iPhone 6, Menlo 14pt.)

### 2017-11-11: v0.2.0 (Spaghetti!):
#### v0.2.0 is here!
* Added: *Starting to add* actions in-line with the post listing in global, timeline, mentions, thread and bookmarks. First up: reply to, repost and bookmark a post. It's a bit rough. And ugly. And buggy. The remainder of the actions are placeholders. (And still only 20 posts per listing.)
* Removed: Repeat display of post to be replied to, during preparation for inline interactions. (It was intended to allow the user to be certain of replying to the correct post). 
* Removed: Superfluous jsondata variable.

### 2017-11-10: v0.1.32 (Oops!):
* Added: Test for too-long post, only in 'createpost' routine at this stage.
* Changed: Tweaked the menu layout yet again.
* Fixed: Accidental duplication of `gt` menu option for both get timeline and get thread.

### 2017-11-10: v0.1.31 (Clearer now? No.):
* Changed: More updates to menu, input requests made clearer.
* Removed: Accidental JSON display code from the getpost routine.

### 2017-11-09: v0.1.30 (Also):
* Added: Automatic reply to all users mentioned in post (limited to 30 names.) No selection or manual edit just yet.

### 2017-11-09: v0.1.29 (Bloat!):
* Added: Subscribe to a public channel (chatroom.)
* Added: Menu now has current user's username.
* Changed: Menu order. I'm trying and failing to make it sensible (tm).

### 2017-11-08: v0.1.28 (Exceptional!):
* Fixed: Channels and threads now display even when there are fewer than 20 items.

### 2017-11-07: v0.1.27 (Overload?):
* Added: Get a user bio. ***Buggy!***
* Changed: Increased number of Interactions from 1 to 20 (server default). Incomplete.
* Changed: Unified post and message status indicators.
* Removed: Reliance on user-entered user_id in 'me.txt' file. I read the API Resources > Users docs. *It's "me" when authenticated!*

### 2017-11-06: v0.1.26 (Interact-ish):
* Added: Started User Interactions. Returns only last one at this stage.
* Added: Username to 'get channel' display.
* Changed: Updated menu yet again. Unified timeline display is now 't' (was u.)

### 2017-11-05: v0.1.25 (Status symbol!):
* Added: The original poster's username is added to replies automatically now. Take care to check for other people before posting.
* Added/changed: Post and user status indicators:
    * User id,
    * `+f` = followed?
    * `+F` = follower?
    * `*` = bookmarked?
    * `rp` = reposted?
    * `id:` = post id,
    * `rep:` = replying to post,
    * `thd` = in thread.
* Changed: Tweaked post display order.

### 2017-11-05: v0.1.24 (Baleeted!):
* Added: Display Global timeline (added after fix below.)
* Changed: Get hashtag command is now `gh` (was `h`.)
* Fixed: Deleted posts are skipped, app no longer exits when encountered.

### 2017-11-05: v0.1.23 (Id):
* Added: Display Unified timeline.
* Added: **Bug:** Deleted posts in unified timeline exit the app.
* Changed: Bookmarks & mentions inquiries requiring a user id still default to requiring input, however pressing [return] inserts a user id saved in a user-created `me.txt` file. Temporary, perhaps.
* Fixed: If server response is 201, PigPen now returns 'ok'.

### 2017-11-04: v0.1.22 (Sensible):
**News:** Changed version numbering style from n.nn.n to n.n.n., e.g. 1.01.22 is now 1.1.22.

* Added: Get last 20 bookmarks. *(No error handling if fewer than 20 exist.)*
* Changed: Exiting now only requires lower case 'exit'.

### 2017-11-03: v0.01.21 (hmmm…):
* Added: List last 20 posts in a thread. *(No error handling: app* **will** *exit with `list index out of range` for conversations with fewer than 20 posts.)*
* Added: List last 20 messages for a channel. *(No error handling: app* **will** *exit with `list index out of range` for channels with fewer than 20 messages.)*
* Changed: Menu order, attempting a more intelligent grouping.
* Changed: Code: Created displaypost() subroutine to reduce duplication in similar routines.
* Fixed: If server response is not 200, PigPen now returns a purposely-ambiguous 'hmmm…' instead of 'oops!'

### 2017-11-02: v0.01.20 (@jws):
* Added: Listing of posts containing a specified hashtag (last 20.)
* Added: Create a message to send to a chatroom or private thread. Need to know the pre-existing channel number.
* Added: Subscribed channel listing. Returns *only* channel number, owner/creator and the most recent message with its id. See also next item.
* Added: Get a channel. Returns content for one post using code modified from above. Potentially useful as a subroutine?
* Changed: Code: Reordered routines: post, reply and message pushed together.
* Removed: pprint module import: I decided to examine JSON outside Pythonista.

### 2017-11-02: v0.01.19 (Threadsbared):
* Added: Thread id to every displayed mention.
* Changed: Reversed mentions sort order: most recent is last, at the bottom of the list, onscreen.


### 2017-11-01: v0.01.18 (Mentions):
* Added: Rudimentary mentions list display: the default number of 20 most recent, *unsorted* returned from the server with no parameters requested other than `user_id`.
* Added mentions JSON file in examples folder.
* (Intermediate, breaking, local test versions omitted from release.)

### 2017-10-31: v0.01.14 (Incompatible):
* Fixed: Rudimentary feedback after interactions - anything other than '200' now doesn't kill the app. (I tried concatenating an integer and text, tsk!)

### 2017-10-30: v0.01.13 (Prettier):
* Updated 'Get post' to show only the poster's username, post create date and post content. An improvement over the previous raw dump.
* Added rudimentary feedback after interactions - currently not those with displayed content.

### 2017-10-29: v0.01.12 (Follow):
* Added the ability to Follow a user (by number.)
* Started messing about with JSON for a later release; it's not going well.

### 2017-10-29: v0.01.11 (Newlines):
* Added newlines in posts - temporary kludge using `\n`, input by user.

### 2017-10-29: v0.01.10 (First upload, with the following features):
* Menu-based,
* Authorise with a single-user token saved in a plain text file - token generated at the pnut.io developer page,
* Post-related features:
  * Post,
  * Reply to a specific post number,
  * Bookmark a specific post number,
  * Repost a specific post number,
  * Get a post's content (raw response from server; not pretty).
* Added documentation, but not yet /docs/.
