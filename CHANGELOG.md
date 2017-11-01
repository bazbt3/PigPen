# CHANGELOG
(Most recent on top.)

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

