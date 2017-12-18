"""PigPen, a Python app for @33MHz's pnut.io social network.

     ___          ___
    / _ |__ ___  / _ | ___  ___
   / ////_// _ \/ //// // |/ _ |
  / __// // //// __// ___ / // /
 /_/  /_/ |_ //_/   |___//_//_/
         /__/
v0.3.19 for Python 3.5

Site, changelog: https://github.com/bazbt3/PigPen

BASIC coding style by: @bazbt3"""


# SETUP:

# Import @33MHz and @thrrgilag's library for interacting with pnut.io:
import pnutpy

# Used to load default and user configuration data:
import configparser
	
# Used to display images:
from PIL import Image
import requests
from io import BytesIO

# For future expansion and for testing:
import time

# Define probably way too many global variables:
global action, channelcount, channelid, channelnumber, channeltype, isdeleted, maxpostlen, me, number, postcontent, postid, posttext, postthreadid, retrievecount
action = ""
channelid = 0
channelnumber = ""
channeltype = ""
isdeleted = ""
me = ""
number = 0
postcontent = ()
postid = 0
postthreadid = 0
posttext = ""

# Define fixed count:
maxpostlen = 256
# Define *default* user-variable counts:
retrievecount = 20
channelcount = 30

# Setup continues after the function definitions.

# DEFINE FUNCTIONS:

def authorise():
	"""
	Authorise user using a token previously obtained from the network.
	
	Arguments:
		none
	User input:
		none
	Dependencies:
		File "secrettoken.txt" must already exist in the same folder as the application. It must contain only the token ontained from pnut.io. See the GitHub repo's docs for more.
	"""
	tokenfile = open("secrettoken.txt", "r")
	token = tokenfile.read()
	token = token.strip()
	pnutpy.api.add_authorization_token(token)

def getme():
	"""
	Get the current user id and username from the server.
	
	Arguments:
		none
	User input:
		none
	"""
	global me, userid
	user = pnutpy.api.get_user("me")
	me = user[0]["username"]
	userid = user[0]["id"]

def menu():
	"""
	Displays main menu text and user's username.
	
	Arguments:
		none
	User input:
		none
	"""
	print("""
| PigPen | u:{0} @{1}
| help.menu | io.files | set.config
p.post r.reply rp.repost xp.x-post
 gm.mentions gt.timeline gg.globaltl
 gi.interact gth.getthrd gp.getpost
 gu.getuser  gup.usrpost f.follow
 gb.bookmrks b.bookmark  gh.hashtag
msg.message  gc.getchan  gcm.getmsgs
 gs.getsubs- sub.subchan uns.unsubch
sp.spamchn | del.mute/block | x.exit""".format(str(userid), str(me)))

def commandentry():
	"""
	Main menu user command input.
	
	Arguments:
		none
	User input:
		Command to execute.
		Mostly:
			if a function call passes 0 or "":
				ask for user input
			elif operand is passed:
				use that instead.
	"""
	choice = 'Little Bobby Tables'
	while choice != 'x':
		choice = input("Command? ")
		# Parse a 1 or 2-part command, extra text is ignored. Trailing comments: 'n/a'=not applicable:
		try:
			choice, operand = choice.split(" ", 1)
		except:
			operand = ""
		# Add commands in alphabetic order to easily scan through:
		if choice == 'b':
			bookmarkpost(operand)
		if choice == 'del': # n/a
			muteblockdelmenu()
		elif choice == 'f':
			followuser(operand)
		elif choice == 'gb':
			getbookmarks(operand)
		elif choice == 'gc':
			getchannel(operand)
		elif choice == 'gcm':
			getmessages(operand)
		elif choice == "gg": # n/a
			getglobal()
		elif choice == 'gh':
			gethashtag(operand)
		elif choice == "gi": # n/a
			getinteractions()
		elif choice == 'gm': # n/a
			getmentions()
		elif choice == 'gp':
			getpost(operand)
		elif choice == 'gs':
			getsubscribed(operand)
		elif choice == "gt": # n/a
			getunified()
		elif choice == 'gth':
			getthread(operand)
		elif choice == 'gu':
			getuser(operand)
		elif choice == 'gup':
			getuserposts(operand)
		elif choice == 'help': # n/a
			menu()
		elif choice == "io": # n/a
			filesmenu()
		elif choice == 'msg':
			createmessage(operand)
		elif choice == 'p':
			createpost(operand)
		elif choice == 'r':
			replypost(operand)
		elif choice == 'rp':
			repostpost(operand)
		elif choice == 'set': # n/a
			changesettings()
		elif choice == "sp":
			mentionsubscribers(operand)
		elif choice == "sub":
			subscribetochannel(operand)
		elif choice == "uns":
			unsubscribechannel() # no
		elif choice == "xp": # no
			xpost()
	# The app exits here once 'exit' is typed:
	print(" ")
	print("*You chose to exit.")


# --------- Single ------

# DEFINE FUNCTIONS FOR USER INTERACTIONS:

def createpost(cpposttext):
	"""
	Create a post.
	
	Arguments:
		posttext:
			if "":
				ask for input
			elif operand from calling function:
				use that instead.
	User input:
		Post text.
	"""
	global posttext
	postlimit = True
	while postlimit:
		if cpposttext == "":
			inputtext()
		else:
			posttext = cpposttext
		print(len(posttext))
		while len(posttext) > maxpostlen:
			postoverlength = len(posttext) - maxpostlen
			addans = ""
			if postoverlength > 1:
				addans = "s"
			print("-" * 31)
			print(posttext)
			print("-" * 31)
			print("*Ah. That was too long by " + str(postoverlength) + " character" + addans + ". To post, perhaps copy & edit the text above?)\n")
			inputtext()
		postlimit = False
	print("-" * 31)
	print(posttext)
	postcontent = pnutpy.api.create_post(data={'text': posttext})
	serverresponse("post", postcontent)

def createmessage(channelid):
	"""
	Create a message for a channel.

		Arguments:
		channelid:
			if "":
				ask for input
			elif operand from calling function:
				use that instead.
	User input:
		Channel number and message text.
	"""
	if channelid == "":
		while channelid == "":
			channelid = input("-Message to channel #? [return]=list\n")
			if channelid == "":
				getsubscribed("")
	inputtext()
	postcontent = pnutpy.api.create_message(channelid, data={'text': posttext})
	serverresponse("message", postcontent)

def xpost():
	"""
	Create a message for a specific channel then use the same text in a post. Does not permit crossposting messages sent to private channels.
	
	Arguments:
		none
	User input:
		Channel number and message.
	"""
	global channelid, posttext
	createmessage("")
	# Get channel name:
	channelcontent = pnutpy.api.get_channel(channelid, include_raw=True)
	getchannelname(channelid, channelcontent)
	# Do not crosspost messages sent to private channels:
	if channeltype == "pm":
		print("*The app does not allow crossposting of messages sent to private channels. The post will not be created.\nSorry.")
	else:
		# Add an x-post footer then create the post without user input:
		posttext += "\n\n" + channelname + " "
		channelurl = "https://patter.chat/room/" + str(channelid)
		channelurlmd = "[<=>](" + channelurl + ")"
		posttext += channelurlmd
		createpost(posttext)

def replypost(postnum):
	"""
	Reply to a post.
	
	Arguments:
		postnum:
			Post number to reply to.
				if postnum == "":
					ask for post number to reply to
				else:
					reply to global postum
	User input:
		Post number and/or post text.
	"""
	getme()
	global posttext
	posttext = ''
	if str(postnum) == "":
		postnum = input("Reply to postnum? ")
	postcontent = pnutpy.api.get_post(postnum)
	if not "is_deleted" in postcontent[0]:
		postlimit = True
		while postlimit:
			# Create body text:
			inputtext()
			# Test for users also mentioned then add all in reply, but excluding self:
			alsoname = ""
			alsomentions = ""
			number = 30
			while number >= 0:
				try:
					alsoname = postcontent[0]["content"]["entities"]["mentions"][number]["text"]
					# Strip self:
					if alsoname != me:
						alsomentions += " @" + alsoname
				except Exception:
					pass
				number -= 1
			posttext = "@" + postcontent[0]["user"]["username"] + " " + posttext
			if alsomentions:
				posttext += "\n/" + alsomentions
			# Ensure post is not over-long:
			if len(posttext) > maxpostlen:
				print("")
				print("*** Too big, " + str(len(posttext)) + " chars.) Redo:")
			else:
				postlimit = False
		pnutpy.api.create_post(data={'reply_to': postnum, 'text': posttext})
		serverresponse("post", postcontent)

def repostpost(postnum):
	"""
	Repost a post.
	
	Arguments:
		postnum:
			Post number to repost.
				if postnum == "":
					ask for post number to repost
				else:
					repost global postnum
	User input:
		Post number.
	"""
	if str(postnum) == "":
		postnum = input("Repost postnum? ")
	postcontent = pnutpy.api.repost_post(postnum)
	serverresponse("repost", postcontent)

def bookmarkpost(postnum):
	"""
	Bookmark a post.
	
	Arguments:
		postnum:
			Post number to bookmark.
				if postnum == "":
					ask for post number to bookmark
				else:
					bookmark global postnum
	User input:
		Post number.
	"""
	if str(postnum) == "":
		postnum = input("Bookmark postnum? ")
	postcontent = pnutpy.api.bookmark_post(postnum)
	serverresponse("bookmark", postcontent)

def followuser(usernum):
	"""
	Follow a user.
	
	Arguments, user input:
		User number.
	"""
	if str(usernum) == "":
		usernum = input("Follow usernum? ")
	postcontent = pnutpy.api.follow_user(usernum)
	serverresponse("followed", postcontent)

def getpost(postnum):
	"""
	Get a post, provided it has not been deleted.
	
	Arguments, user input:
		Post number.
	"""
	if str(postnum) == "":
		postnum = input("Get postnum? ")
	postcontent = pnutpy.api.get_post(postnum, include_raw= True)
	print("--------------")
	if not "is_deleted" in postcontent[0]:
		userstatus(postcontent)
		timestarrpstatus(postcontent)
		print(postcontent[0]["content"]["text"])
		# Check for oembed file:
		try:
			raw = postcontent[0]['raw'][0]
			checkoembed(postcontent, raw)
		except:
			pass
		postfooter(postcontent)
	else:
		print("[Post was deleted]")
	print("---------------")

def getuser(usernum):
	"""
	Get a user's details: username & name, account type, locale, bio, interactions.
	
	Arguments, user input:
		User number.
	"""
	
	# Get a user's data:
	if str(usernum) == "":
		usernum = input("Get data, usernum? ")
	postcontent = pnutpy.api.get_user(usernum)
	print("")
	print("@" + postcontent[0]["username"] + " - " + postcontent[0]["type"])
	if postcontent[0]["type"] == 'human':
		try:
			username = postcontent[0]["name"]
		except (KeyError):
			username = ""
		print(username)
		if postcontent[0]["locale"]:
			print(postcontent[0]["locale"])
		if postcontent[0]["timezone"]:
			print(postcontent[0]["timezone"])
	bio = False
	try:
		pnutbio = postcontent[0]["content"]["text"]
		bio = True
		print(pnutbio)
	except (KeyError):
		bio = False
	if bio == False:
		print("-no bio")
	print("posts: " + str(postcontent[0]["counts"]["posts"]))
	print("followers: " + str(postcontent[0]["counts"]["followers"]))
	print("following: " + str(postcontent[0]["counts"]["following"]))
	print("bookmarks: " + str(postcontent[0]["counts"]["bookmarks"]))
	print("")

def subscribetochannel(channelnum):
	"""
	Subscribe to a public (chat) channel.
	
	Arguments, user input:
		Channel number.
	"""
	if str(channelnum) == "":
		channelnum = input("Subscribe to channelnum? ")
	postcontent = pnutpy.api.subscribe_channel(channelnum)
	serverresponse("subscribed", postcontent)

def unsubscribechannel():
	"""
	Unsubscribe from a channel.
	
	Arguments:
		none
	User input:
		Channel number.
	"""
	print("*No undo. (Resubscribe later.)")
	deleteit = input("Unsubscribe from a channel: are you sure? (y/n)")
	if deleteit == "y":
		channelnum = input("*Unsubscribe from channel number? ")
		postcontent = pnutpy.api.subscribe_channel(channelnum)
		serverresponse("unsubscribed", postcontent)
	else:
		print("-not unsubscribed")

def getchannel(channelnumber):
	"""
	Get a public (chat) channel's details and most recent message.
	
	Arguments, user input:
		Channel number.
	"""
	if str(channelnumber) == "":
		channelnumber = input("Get data, channelid? ")
	channelcontent = pnutpy.api.get_channel(channelnumber, include_raw=True)
	getchannelname(channelnumber, channelcontent)
	print("---------------")
	print("#" + str(channelcontent[0]["id"]) + " " + channelname + " c:" + "@" + channelcontent[0]["owner"]["username"])
	# Build recent message, unless it's been deleted:
	try:
		recentmessageid = str(channelcontent[0]['recent_message_id'])
		channelid = channelcontent[0]["id"]
		message = pnutpy.api.get_message(channelid, recentmessageid)
		# Check for deleted message content first (using an exception isn't the best way!):
		messagecontent = message[0]["content"]["text"]
		# Display if not deleted:
		print("last message: " + recentmessageid + ":")
		print("@" + message[0]["user"]["username"] + ":")
		print(messagecontent)
	except:
		print("*Most recent message deleted (or had no content.)")
	print("---------------")
	subbies = input("*Get a list of the channel user numbers (y/n)? ")
	if subbies == "y":
		getsubscribers(channelnumber)
	print("---------------")


# --------- Multiple ------

# DEFINE INTERACTIONS WITH MULTIPLE RESULTS:

def getunified():
	"""
	Get the application user's own 'Unified' post stream.
	
	Arguments:
		none
	User input:
		none
	"""
	postcontent = pnutpy.api.users_post_streams_unified(count = retrievecount, include_raw=True)
	displaypost(postcontent)

def getglobal():
	"""
	Get the Global post stream.
	
	Arguments:
		none
	User input:
		none
	"""
	postcontent = pnutpy.api.posts_streams_global(count = retrievecount, include_raw=True)
	displaypost(postcontent)

def getmentions():
	"""
	Get an account's mentions.
	
	Arguments:
		none
	User input:
		User number.
	"""
	userid = input("User mentions, userid? [return]=me: ")
	if userid == '':
		userid = "me"
	postcontent = pnutpy.api.users_mentioned_posts(userid, count=retrievecount, include_raw=True)
	displaypost(postcontent)

def getuserposts(userid):
	"""
	Get an account's posts.
	
	Arguments:
		none
	User input:
		User number.
	"""
	if str(userid) == "":
		userid = input("User posts, userid? [return]=me: ")
		if userid == "":
			userid = "me"
	postcontent = pnutpy.api.users_posts(userid, count=retrievecount, include_raw=True)
	displaypost(postcontent)

def getinteractions():
	"""
	Get the application user's interactions.
	
	Arguments:
		none
	User input:
		User number.
	"""
	userid = input("Interacts, userid? [return]=me: ")
	if userid == '':
		userid = "me"
	postcontent = pnutpy.api.interactions_with_user(userid, count=retrievecount)
	global number
	number = retrievecount
	print("---------------")
	while number >= 0:
		try:
			print(postcontent[0][number]["action"] + " by @" + postcontent[0][number]["users"][0]["username"] + " ref.:")
			print(postcontent[0][number]["event_date"])
			print(postcontent[0][number]["objects"][0]["content"]["text"])
			print("---------------")
		except:
			pass
		number -= 1

def getthread(postnum):
	"""
	Get a thread.
	
	Arguments:
		postnum:
			Post number to thread.
				if postnum == "":
					ask for post number to thread
				else:
					thread from post
	User input:
		Post number, threads are displayed beginning with postnum.
	"""
	if str(postnum) == "":
		postnum = input("Get threadid? ")
	postcontent = pnutpy.api.posts_thread(postnum, count=retrievecount, include_raw=True)
	displaypost(postcontent)

def getbookmarks(userid):
	"""
	Get a user's bookmarks.
	
	Arguments:
		none
	User input:
		User number.
	"""
	if str(userid) == "":
		userid = input("Bookmarks, userid? [return]=me: ")
	if userid == '':
		userid = "me"
	postcontent = pnutpy.api.users_bookmarked_posts(userid, count=retrievecount, include_raw=True)
	displaypost(postcontent)

def gethashtag(hashtag):
	"""
	Get a list of posts containing the required hashtag.
	
	Arguments, user input:
		Hashtag text.
	"""
	if hashtag == "":
		hashtag = input("Get hashtag? ")
	postcontent = pnutpy.api.posts_with_hashtag(hashtag, count = retrievecount, include_raw=True)
	displaypost(postcontent)

def getsubscribed(output):
	"""
	Get a list of the application user's subscribed channels.
	
	Arguments:
		output:
			The "v" flag indicates verbose output; anything else passed to this function gives an abbreviated listing.
	User input:
		none
	"""
	channelcontent = pnutpy.api.subscribed_channels(count=channelcount)
	global number
	number = channelcount
	print("---------------")
	while number >= 0:
		try:
			channelnumber = channelcontent[0][number]["id"]
			# Differentiate netween Chat and PM channels:
			channeltype = str(channelcontent[0][number]["type"])[13:]
			# Get chat channel name:
			# Thanks @hutattedonmyarm!
			channelname = ""
			if channeltype == "chat":
				channelnumraw = pnutpy.api.get_channel(channelnumber, include_raw=True)
				try:
					channelname = channelnumraw[0]["raw"][0]["value"]["name"]
				except:
					channelname = channelnumraw[0]["raw"][1]["value"]["name"]
			# Check for unread:
			if channelcontent[0][number]["has_unread"]:
				channelunread = "[u]"
			else:
				channelunread = ""
			# Build and display listing:
			print(channelunread + "#" + str(channelnumber) + ": " + channelname)
			print(channeltype + " c:@" + channelcontent[0][number]["owner"]["username"])
			# Check output type: standard or verbose:
			if output == "v":
				# Build last message in channel:
				recentmessageid = str(channelcontent[0][number]['recent_message_id'])
				print("last: " + recentmessageid + ":")
				channelid = channelcontent[0][number]["id"]
				message = pnutpy.api.get_message(channelid, recentmessageid)
				print("@" + message[0]["user"]["username"] + ": " + message[0]["content"]["text"])
			print("---------------")
		except:
			pass
		number -= 1

def getmessages(channelnumber):
	"""
	Get a list of messages in a public channel, or a private channel the user has authorisation for.
	
	Arguments:
		none
	User input:
		Channel number.
	"""
	if channelnumber == "":
		while channelnumber == "":
			channelnumber = input("-Messages in channel? [return]=list\n")
			if channelnumber == "":
				getsubscribed("")
	postcontent = pnutpy.api.get_channel_messages(channelnumber, count = retrievecount, include_raw=True)
	displaymessage(postcontent)

def getsubscribers(channelnumber):
	"""
	Get a list of subscribers to a channel. Maximum 50. Called from getchannel.
	
	Arguments, user input:
		Channel number.
	"""
	if str(channelnumber) == "":
		channelnumber = input("-Subscribers in channel number? ")
	postcontent = pnutpy.api.subscribed_users(channelnumber)
	number = 50
	print("---------------")
	while number >= 0:
		try:
			userid = postcontent[0][number]["id"]
			username = "@" + postcontent[0][number]["username"]
			print (userid, username)
		except:
			pass
		number -= 1

def mentionsubscribers(channelnumber):
	"""
	Get a list of subscribers to a channel and create a message mentioning all. Maximum 50.
	
	Arguments, user input:
		Channel number, message.
	"""
	global posttext
	posttext = ""
	if str(channelnumber) == "":
		channelnumber = input("-Spam channel number? ")
	postcontent = pnutpy.api.subscribed_users(channelnumber)
	number = 50
	recipients = "/"
	while number >= 0:
		try:
			recipientname = postcontent[0][number]["username"]
			if recipientname != me:
				recipients += "@" + recipientname + " "
		except:
			pass
		number -= 1
#	postcontent = pnutpy.api.get_user(usernum)
	print("-Enter the message:")
	inputtext()
	posttext += ("\n" + recipients)
	print(posttext)
	postpause = input("*Are you sure? (y/n)")
	if postpause == "y":
		postcontent = pnutpy.api.create_message(channelid, data={'text': posttext})
		serverresponse("message", postcontent)
	else:
		print("*Message not sent")


# --------- Files ------

def filesmenu():
	"""
	Files menu.
	
	Arguments:
		none
	User input:
		The command to execute.
	"""
	choice = input("""
| files |
gf = get a file
gmf = get my files
upload = upload an image
avn = set normal avatar
avt = set ThemeMonday avatar
[return] = quit
""")
	if choice == "gf":
		getfile()
	if choice == "gmf":
		getmyfiles()
	elif choice == "upload":
		uploadanimage("")
	elif choice == "avn":
		setnormalavatar()
	elif choice == "avt":
		settmavatar()

def getmyfiles():
	"""
	Get a list of the user's files.
	
	Arguments:
		none
	User input:
		none.
	"""
	# Test with a big count to :
	count = 25
	number = count - 1
	filescontent = pnutpy.api.get_my_files(count = count)
	# Display the most recent data:
	print(filescontent[0][0])
	print("-" * 31)
	# Display the most recent by count:
	while number >= 0:
		print("-" * 31)
		print("id:", filescontent[0][number]["id"])
		print("token:", filescontent[0][number]["file_token"])
		print(filescontent[0][number]["created_at"])
		print(filescontent[0][number]["type"])
		print(filescontent[0][number]["kind"])
		print("w:", filescontent[0][number]["image_info"]["width"])
		print("h:", filescontent[0][number]["image_info"]["height"])
		print(filescontent[0][number]["name"])
		print(filescontent[0][number]["source"]["name"])
		number -= 1
	print("-" * 31)
	print("Listing is for analysis, not users.")

def getfile():
	"""
	Get a single file by id.
	
	Arguments:
		none
	User input:
		none.
	"""
	fileid = 1700
	filecontent = pnutpy.api.get_file(fileid)
	print(filecontent)
	print("-" * 31)
	print("Listing is for analysis, not users.")

def uploadanimage(file_name):
	"""
	Upload an image. Dependent on a file existing in the same folder as the PigPen application.
	
	Adapted from the official pnutpy documentation.
	Arguments:
		file_name:
			Can be passed to the function.
	User input:
		file_name:
			Input by user if not passed to the function.
	Optional metadata (include it in file_data):
		is_public = False
		mime_type = 'text/plain'
		sha256 = <sha256 hash> #API will reject if it doesn't match with the actual sha256 hash
	"""
	# If empty filename, ask for a filename: 
	if file_name == "":
		file_name = input("If the file is present in the images/ folder with the application, enter its full filename, or [return]=quit: ")
	# If a filename is passed to this function or if the user enters a filename then attempt to upload it:
	if file_name != "":
		file_name = "images/" + file_name
		# The file itself; the 'b' binary switch is necessary, otherwise the ascii codec attempts to decode it:
		file = open(file_name, 'rb')
		# Required metadata in addition to the filename to upload:
		# Needs investigation:
		file_type = 'io.pnut.core.image'
		# Can be 'image' or 'other':
		file_kind = 'image'
		# Build the file data:
		file_data = {'type': file_type, 'kind': file_kind, 'name': file_name, 'is_public': True}
		# Create the file:
		pnut_file = pnutpy.api.create_file(files={'content':file}, data=file_data)
		# Return server response:
		serverresponse("uploaded", pnut_file)

def setnormalavatar():
	"""
	DOES NOT WORK YET. Set the user's normal avatar image. Can either be used for its initial upload or after a #ThemeMonday event change.
	
	Uses the same basic code as uploadanimage hence the lack of duplicated comments.
	Arguments:
		none
	User input:
		none
	"""
	# The folder and filename of the 'normal' avatar image:
	file_name = "avatar.jpg"
	file = open(file_name, 'rb')
	file_type = 'io.pnut.core.image'
	file_kind = 'image'
	file_data = {'type': file_type, 'kind': file_kind, 'name': file_name}
	pnut_file = pnutpy.api.update_avatar(files={'content':file}, data=file_data)
	serverresponse("avatar set", pnut_file)


# --------- Mute/block/delete ------

def muteblockdelmenu():
	"""
	Submenu to hide away all the unpalatable things.
	
	Arguments:
		none
	User input:
		The command to execute.
	"""
	choice = input("""
| mute/block/delete |
delp = delete a post
muteu = mute a user
unmuteu = unmute a user
mutec = mute a channel
unmutec = unmute a user
[return] = quit
""")
	if choice == "delp":
		deletepost()
	elif choice == "mutec":
		mutechannel()
	elif choice == "muteu":
		muteuser()
	elif choice == "unmutec":
		unmutechannel()
	elif choice == "unmuteu":
		unmuteuser()

def deletepost():
	"""
	Delete a post.
	
	Arguments:
		none
	User input:
		Post id.
	"""
	print("*No undo. (None.)")
	deleteit = input("Delete a post: are you sure? (y/n)")
	if deleteit == "y":
		postid = input("*Delete post, number? ")
		postcontent = pnutpy.api.delete_post(postid)
		serverresponse("post deleted", postcontent)
	else:
		print("-nothing deleted")

def mutechannel():
	"""
	Mute a channel.
	
	Arguments:
		none
	User input:
		Channel number.
	"""
	channelnum = input("*Mute channel number? ")
	postcontent = pnutpy.api.mute_channel(channelnum)
	serverresponse("channel muted",postcontent)

def unmutechannel():
	"""
	Unmute a channel.
	
	Arguments:
		none
	User input:
		Channel number.
	"""
	channelnum = input("*Unmute channel number? ")
	postcontent = pnutpy.api.unmute_channel(channelnum)
	serverresponse("channel unmuted", postcontent)

def muteuser():
	"""
	Mute a user.
	
	Arguments:
		none
	User input:
		Channel number.
	"""
	usernum = input("*Mute user number? ")
	postcontent = pnutpy.api.mute_user(usernum)
	serverresponse("user muted", postcontent)

def unmuteuser():
	"""
	Unmute a user.
	
	Arguments:
		none
	User input:
		Channel number.
	"""
	usernum = input("*Unmute user number? ")
	postcontent = pnutpy.api.unmute_user(usernum)
	serverresponse("user unmuted", postcontent)


# --------- Admin. misc. ------

# DEFINE OTHER ROUTINES:

def changesettings():
	"""
	Changes global settings.
	
	Arguments:
		none
	User input:
		The setting to change:
			retrievecount and channelcount = the number of posts fetched from the server. No input validation.
	"""
	global retrievecount, channelcount
	choice = input(("""
| settings |
gc = change general count? ({0})
cc = change channel count? ({1})
[return] = back
""").format(str(retrievecount), str(channelcount)))
	# Set global retrieve count
	rcount = retrievecount
	if choice == "gc":
		print("-general count is currently", retrievecount)
		rcount = input("*Please change, to (>0)? ")
		if int(rcount) > 0:
			retrievecount = int(rcount)
			print("-general count is now", retrievecount, "posts")
	# Set channels retrieve count
	ccount = channelcount
	if choice == "cc":
		print("-channel count is currently", channelcount)
		ccount = input("*Please change, to (>0)? ")
		if int(ccount) > 0:
			channelcount = int(ccount)
			print("-channel count is now", channelcount, "posts")
	# Every time settings menu is used, save to "ppconfig.ini" file:
	config["USER"]["retrievecount"] = str(retrievecount)
	config["USER"]["channelcount"] = str(channelcount)
	with open ("ppconfig.ini", "w") as configfile:
		config.write(configfile)
	print("-settings saved\n")

def inputtext():
	"""
	Takes user input, passes it back to the calling function.
	
	Arguments:
		none
	User input:
		Text.
	Special:
		if textinput.startswith "/me":
			create a post reminiscent of an iOS Mutter IRC app "/me" post.
	"""
	global posttext
	posttext = ''
	textinput = ""
	while not textinput:
		textinput = input("Write here (\\n=newline): ")
		if not textinput:
			print("-Empty post, retry-")
	# Silly things:
	# IRC-like /me:
	if textinput.startswith("/me"):
		textinput = "+" + me + textinput[3:]
	# Back to sensible
	splittext = textinput.split(r'\n')
	for sentence in splittext:
		posttext = posttext + sentence + "\n"
	posttext = posttext.strip()

def displaypost(postcontent):
	"""
	Displays a list of posts (not a messages), provided they have not been deleted.
	
	Arguments:
		postcontent:
			The posts' content.
	User input:
		none
	"""
	global number
	number = retrievecount
	print("---------------")
	while number >= 0:
		try:
			if not "is_deleted" in postcontent[0][number]:
				# Build user status:
				postid = str(postcontent[0][number]["id"])
				postuserid = str(postcontent[0][number]["user"]["id"])
				postthreadid = str(postcontent[0][number]["thread_id"])
				userstatus = "@" + postcontent[0][number]["user"]["username"] + ": [u:" + postuserid
				if postcontent[0][number]["user"]["you_follow"]:
					userstatus += "+f"
				if postcontent[0][number]["user"]["follows_you"]:
					userstatus += "+F"
				print(userstatus + "]")
				# Build post status indicators:
				poststatus = str(postcontent[0][number]["created_at"]) + " ["
				if postcontent[0][number]["you_bookmarked"]:
					poststatus += "*"
				if postcontent[0][number]["you_reposted"]:
					poststatus += "rp"
				print(poststatus + "]")
				# Display post text:
				print(postcontent[0][number]["content"]["text"])
				# Check for oembed file:
				try:
					raw = postcontent[0][number]['raw'][0]
					checkoembed(postcontent[0][number], raw)
				except:
					pass
				# Build hierarchy links:
				postrefs = " id:" + postid
				if "reply_to" in postcontent[0][number]:
					postrefs += " rep:" + str(postcontent[0][number]["reply_to"])
				postrefs += " thd:" + postthreadid
				print(postrefs)
				inlinepostinteraction(postid, postthreadid)
				if action == "x":
					number = 0
		except:
			pass
		number -= 1
	print("")

def inlinepostinteraction(postid, postthreadid):
	"""
	Displays an inline post interaction menu and accepts commands from it.
	
	Arguments:
		postid:
			The post id currently in focus.
		postthreadid:
			The thread in which the post exists.
	User input:
		Command to execute.
	"""
	global action
	validaction = False
	separatormenu = " ------------------------------- "
	menuseparator = "  Inline interactions menu:\n  [return].next r.reply rp.repost\n  b.bookmark gth.get thread\n  x.exit"
	divider = separatormenu
	while not validaction:
		action = input(divider)
		if action == "help":
			print(menuseparator)
		if action == "":
			validaction = True
		if action == "r":
			replypost(postid)
			validaction = True
		if action == "rp":
			repostpost(postid)
			validaction = True
		if action == "b":
			bookmarkpost(postid)
			validaction = True
		if action == "gth":
			getthread(postthreadid)
			validaction = True
			print("-back to list")
		if action == "x":
			print("-back to main menu")
			validaction = True
			return

def displaymessage(postcontent):
	"""
	Displays a list of messages (not posts.)
	
	Arguments:
		postcontent:
			The messages' content.
	User input:
		none
	"""
	global number
	number = retrievecount
	print("---------------")
	while number >= 0:
		try:
			if not "is_deleted" in postcontent[0][number]:
				# Build post status indicators:
				userstatus = "@" + postcontent[0][number]["user"]["username"] + ": [u:" + str(postcontent[0][number]["user"]["id"])
				if postcontent[0][number]["user"]["you_follow"]:
					userstatus += "+f"
				if postcontent[0][number]["user"]["follows_you"]:
					userstatus += "+F"
				print(userstatus + "]")
				# Add date & time:
				print(str(postcontent[0][number]["created_at"]))
				# Add post content/
				print(postcontent[0][number]["content"]["text"])
				# Check for oembed file:
				try:
					raw = postcontent[0][number]['raw'][0]
					checkoembed(postcontent[0][number], raw)
				except:
					pass
				print("---------------------------------")
		except:
			pass
		number -= 1
	print("")

def getchannelname(channelnumber, channelcontent):
	"""
	Gets the desired channel mame from the server, for use in the function calling it.
	
	Arguments:
		channelnumber:
			The channel mumber to be queried.
		channelcontent:
			The message's content, from which this function extracts the name associated with the channel number.
	User input:
		none
	"""
	# Differentiate netween Chat and PM channels:
	global channelname, channeltype
	channeltype = channelcontent[0]["type"][13:]
	# Get chat channel name:
	# Thanks @hutattedonmyarm!
	if channeltype == "chat":
		channelnumraw = pnutpy.api.get_channel(channelnumber, include_raw=True)
		try:
			channelname = channelnumraw[0]["raw"][0]["value"]["name"]
		except:
			channelname = channelnumraw[0]["raw"][1]["value"]["name"]
	if channeltype == "pm":
		channelname = "*PM"

def userstatus(postcontent):
	"""
	Extracts the username, id, following and follower status from a post's content.
	
	Arguments:
		postcontent:
			The contents of a single post.
	User input:
		none
	"""
	userstatus = "@" + postcontent[0]["user"]["username"] + ": [u:" + str(postcontent[0]["user"]["id"])
	if postcontent[0]["user"]["you_follow"]:
		userstatus += "+f"
	if postcontent[0]["user"]["follows_you"]:
		userstatus += "+F"
	print(userstatus + "]")

def timestarrpstatus(postcontent):
	"""
	Extracts the created at, bookmarked and repost status from a post's content.
	
	Arguments:
		postcontent:
			The contents of a single post.
	User input:
		none
	"""
	poststatus = str(postcontent[0]["created_at"]) + " ["
	if postcontent[0]["you_bookmarked"]:
		poststatus += "*"
	if postcontent[0]["you_reposted"]:
		poststatus += "rp"
	print(poststatus + "]")

def checkoembed(postcontent, raw):
	"""
	Extracts any oembed-ed image and link from a post's content.
	
	Arguments:
		postcontent:
			The contents of a single post.
		raw:
			The 'raw' content attached to a post.
	User input:
		none
	"""
	try:
		if raw["type"] == "io.pnut.core.oembed":
			# Get image page URL:
			oembedimgurl = raw["value"]["url"]
			print("[url:]")
			print(oembedimgurl)
			# Get thumbnail URL:
			oembedthumburl = raw["value"]["thumbnail_url"]
			# Open 'thumbnail' image from URL:
			response = requests.get(oembedthumburl)
			# Display image:
			img = Image.open(BytesIO(response.content))
			img.show()
	except (KeyError):
		pass

def postfooter(postcontent):
	"""
	Extracts a post id, post replying to and thread from a single post.
	
	Arguments:
		postcontent:
			The contents of a single post.
	User input:
		none
	"""
	# Display post data
	postrefs = " id:" + str(postcontent[0]["id"])
	if "reply_to" in postcontent[0]:
		postrefs += " rep:" + str(postcontent[0]["reply_to"])
	postrefs += " thd:" + str(postcontent[0]["thread_id"])
	print(postrefs)

def serverresponse(interaction, postcontent):
	"""
	Displays status returned from the server after posts, messages, etc.
	
	Arguments:
		postcontent:
			The server's response.
	User input:
		none
	"""
	status = ()
	status = postcontent[1]["code"]
	if status == 200:
		print("-" + interaction + " ok")
	elif status == 201:
		print("-" + interaction + " created")
	else:
		print(str(status) + "? hmmm... what's that now?")


# --------- Main ------

# MAIN ROUTINE:

def main():
	"""
	Sets up the application, displays the menu, then waits for commands.
	
	Arguments:
		none
	User input:
		Commands from the menus.
	"""
	# Get authorisation token from file:
	authorise()
	# Get pnut.io username:
	getme()
	# Display menu:
	menu()
	# Begin command entry, exit on 'exit':
	commandentry()

# --------- Set defaults ------

# Load defaults and any previous user-applied changes from "ppconfig.ini", initially only 'defaultretrievecount' and 'retrievecount':
try:
	config = configparser.ConfigParser()
	config.read("ppconfig.ini")
	retrievecount = int(config["USER"]["retrievecount"])
	channelcount = int(config["USER"]["channelcount"])
except:
	config = configparser.ConfigParser()
	config["USER"] = {}
	config["USER"]["retrievecount"] = "retrievecount"
	config["USER"]["channelcount"] = "channelcount"
	print("""
| PigPen | setup |
*You'll see this only once.
Please choose the number of items to display from the following menu. ([return] accepts the defaults.)\n""")
	changesettings()
	print("Thanks.")

# STOP FIDDLING WITH STUFF, DO IT!
quit = "n"
while quit != "y":
	main()
	quit = input("-Are you sure (y/n)")
print("-Goodbye.")
