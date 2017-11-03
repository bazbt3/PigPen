# CHANGELOG
(Most recent on top.)

### Upcoming:
* Fix for routines that fail with fewer than 20 list items.
* Adding channel list names and descriptions.

### 2017-11-03: v0.01.21 (hmmm…):
* Added: List last 20 posts in a thread. *(No error handling: app* **will** *exit with `list index out of range` for conversations with fewer than 20 posts.)*
* Added: List last 20 messages for a channel. *(No error handling: app* **will** *exit with `list index out of range` for channels with fewer than 20 messages.)*
* Changed: Menu order, attempting a more intelligent grouping.
* Changed: Code: Created displaypost() subroutine to reduce duplication in similar routines.
* Deprecated: -
* Removed: -
* Fixed: If server response is not 200, PigPen now returns a purposely-ambiguous 'hmmm…' instead of 'oops!'
* Security: -

### 2017-11-02: v0.01.20 (@jws):
* Added: Listing of posts containing a specified hashtag (last 20.)
* Added: Create a message to send to a chatroom or private thread. Need to know the pre-existing channel number.
* Added: Subscribed channel listing. Returns *only* channel number, owner/creator and the most recent message with its id. See also next item.
* Added: Get a channel. Returns content for one post using code modified from above. Potentially useful as a subroutine?
* Changed: Code: Reordered routines: post, reply and message pushed together.
* Deprecated: -
* Removed: pprint module import: I decided to examine JSON outside Pythonista.
* Fixed: -
* Security: -

### 2017-11-02: v0.01.19 (Threadsbared):
* Added thread id to every displayed mention.
* Reversed mentions sort order: most recent is last, at the bottom of the list, onscreen.


### 2017-11-01: v0.01.18 (Mentions):
* Added rudimentary mentions list display: the default number of 20 most recent, *unsorted* returned from the server with no parameters requested other than `user_id`.
* Added mentions JSON file in examples folder.
* (Intermediate, breaking, local test versions omitted from release.)

### 2017-10-31: v0.01.14 (Incompatible):
* Fixed the rudimentary feedback after interactions - anything other than '200' now doesn't kill the app. (I tried concatenating an integer and text, tsk!)

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
