#     ___          ___
#    / _ |__ ___  / _ | ___  __
#   / ////_// _ \/ //// // |/  |
#  / __// // //// __// ___ / /||
# /_/  /_/ |_ //_/   |___//_//_/
#         /__/
# v0.3.11 for Python 3.5

# PigPen, a Python app for @33MHz's pnut.io social network.

# Site, changelog: https://github.com/bazbt3/PigPen

# Made by: @bazbt3


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
# Define user-variable counts:
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
| help=menu | set=settings | ex=exit
p.post r.reply rp.repost xp.x-post
 gm.mentions gt.timeline gg.globaltl
 gi.interact gth.getthrd gp.getpost
 gu.getuser  gup.usrpost f.follow
 gb.bookmrks b.bookmark  gh.hashtag
msg.message  gs.getsubs  gms.getmsgs
 gc.getchan  sub.subchan uns.unsubch
------------ dp.delpost. zp.zpost!""".format(str(userid), str(me)))

def commandentry():
	"""
	Main menu user command input.
	
	Arguments:
		none
	User input:
		Command to execute.
	Discrepancies (I might have had a reason for this):
		1. Mostly:
			if a function call passes 0:
				ask for user input
			else:
				the routine uses the global variable passed from the routine calling it
		2. createpost and createmessage are currently different:
			if the function call passes True:
				ask for user input
			else:
				the routine uses the global variable passed from the routine calling it
	"""
	choice = 'Little Bobby Tables'
	while choice != 'ex':
		choice = input("Choice? ")
		# Add in alphabetic order to easily scan through
		if choice == 'b':
			bookmarkpost(0)
		if choice == 'dp':
			deletepost()
		elif choice == 'f':
			followuser()
		elif choice == 'gb':
			getbookmarks()
		elif choice == 'gc':
			getchannel()
		elif choice == "gg":
			getglobal()
		elif choice == 'gh':
			gethashtag()
		elif choice == "gi":
			getinteractions()
		elif choice == 'gm':
			getmentions()
		elif choice == 'gms':
			getmessages()
		elif choice == 'gp':
			getpost()
		elif choice == 'gs':
			getsubscribed()
		elif choice == "gt":
			getunified()
		elif choice == 'gth':
			getthread(0)
		elif choice == 'gu':
			getuser()
		elif choice == 'gup':
			getuserposts()
		elif choice == 'help':
			menu()
		elif choice == 'msg':
			createmessage(True)
		elif choice == 'p':
			createpost(True)
		elif choice == 'r':
			replypost(0)
		elif choice == 'rp':
			repostpost(0)
		elif choice == 'set':
			changesettings()
		elif choice == "sub":
			subscribetochannel()
		elif choice == "uns":
			unsubscribefromchannel()
		elif choice == "xp":
			xpost()
		elif choice == "zp":
			zpost()
	# The app exits here once 'exit' is typed:
	print(" ")
	print("*You chose to exit: Goodbye!")

# ------------------------------

# DEFINE FUNCTIONS FOR USER INTERACTIONS:

def createpost(inputflag):
	"""
	Create a post.
	
	Arguments:
		inputflag:
			if True: ask for input,
			if False: use global posttext
	User input:
		Post text.
	"""
	postlimit = True
	while postlimit:
		if inputflag == True:
			inputtext()
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
	postcontent = pnutpy.api.create_post(data={'text': posttext})
	serverresponse(postcontent)

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
		serverresponse(postcontent)
	else:
		print("-nothing deleted")

def createmessage(inputflag):
	"""
	Create a message for a channel.
	
	Arguments:
		inputflag:
			if True: ask for input,
			if False: use global posttext and channel
	User input:
		Channel number and/or message text.
	"""
	global channelid, posttext
	if inputflag == True:
		channelid = input("Message to channelid? ")
		inputtext()
	postcontent = pnutpy.api.create_message(channelid, data={'text': posttext})
	serverresponse(postcontent)

def xpost():
	"""
	Create a message for a specific channel then use the same text in a post. Does not permit crossposting messages sent to private channels.
	
	Arguments:
		none
	User input:
		Channel number and message.
	"""
	global channelid, posttext
	createmessage(True)
	# Get channel name:
	channelcontent = pnutpy.api.get_channel(channelid, include_raw=True)
	getchannelname(channelid, channelcontent)
	# Do not crosspost messages sent to private channels:
	if channeltype == "pm":
		print("*Right now the app does not allow crossposting messages sent to private channels.\nSorry.")
	else:
		# Add an x-post footer then create the post without user input:
		posttext += "\n\nx-post: " + channelname + " "
		channelurl = "https://patter.chat/room/" + str(channelid)
		channelurlmd = "[<=>](" + channelurl + ")"
		posttext += channelurlmd
		createpost(False)

def zpost():
	"""
	Create a post then use the same text to send a message to a specific channel. Permits crossposting messages to private channels.
	
	Arguments:
		none
	User input:
		Channel number and post.
	"""
	global channelid, posttext
	createpost(True)
	channelid = input("\nMessage for channelid? ")
	posttext += "\n\n[x-post from global]"
	createmessage(False)

def replypost(postnum):
	"""
	Reply to a post.
	
	Arguments:
		postnum:
			Post number to reply to.
				if postnum == 0:
					ask for post number to reply to
				else:
					reply to global postum
	User input:
		Post number and/or post text.
	"""
	getme()
	global posttext
	posttext = ''
	if postnum == 0:
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
					dummyvalue = 0
					# Not needed
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
		serverresponse(postcontent)

def repostpost(postnum):
	"""
	Repost a post.
	
	Arguments:
		postnum:
			Post number to repost.
				if postnum == 0:
					ask for post number to repost
				else:
					repost global postnum
	User input:
		Post number.
	"""
	if postnum == 0:
		postnum = input("Repost postnum? ")
	postcontent = pnutpy.api.repost_post(postnum)
	serverresponse(postcontent)

def bookmarkpost(postnum):
	"""
	Bookmark a post.
	
	Arguments:
		postnum:
			Post number to bookmark.
				if postnum == 0:
					ask for post number to bookmark
				else:
					bookmark global postnum
	User input:
		Post number.
	"""
	if postnum == 0:
		postnum = input("Bookmark postnum? ")
	postcontent = pnutpy.api.bookmark_post(postnum)
	serverresponse(postcontent)

def followuser():
	"""
	Follow a user.
	
	Arguments:
		none
	User input:
		User number.
	"""
	usernum = input("Follow usernum? ")
	postcontent = pnutpy.api.follow_user(usernum)
	serverresponse(postcontent)

def getpost():
	"""
	Get a post, provided it has not been deleted.
	
	Arguments:
		none
	User input:
		Post number.
	"""
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
			dummyvalue = 0
		postfooter(postcontent)
	else:
		print("[Post was deleted]")
	print("---------------")

def getuser():
	"""
	Get a user's details: username & name, account type, locale, bio, interactions.
	
	Arguments:
		none
	User input:
		User number.
	"""
	
	# Get a user's data
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
		try:
			pnutbio = postcontent[0]["content"]["text"]
		except (KeyError):
			dummyvalue = 0
		print(pnutbio)
	print("")
	print("posts: " + str(postcontent[0]["counts"]["posts"]))
	print("followers: " + str(postcontent[0]["counts"]["followers"]))
	print("following: " + str(postcontent[0]["counts"]["following"]))
	print("bookmarks: " + str(postcontent[0]["counts"]["bookmarks"]))
	print("")

def subscribetochannel():
	"""
	Subscribe to a public (chat) channel.
	
	Arguments:
		none
	User input:
		Channel number.
	"""
	channelnum = input("Subscribe to channelnum? ")
	postcontent = pnutpy.api.subscribe_channel(channelnum)
	serverresponse(postcontent)

def unsubscribefromchannel():
	"""
	Unsubscribe from a channel.
	
	Arguments:
		none
	User input:
		Channel number.
	"""
	print("*No undo. (Resubscribe later.")
	deleteit = input("Unsubscribe: are you sure? (y/n)")
	if deleteit == "y":
		channelnum = input("*Unsubscribe from channel number? ")
		postcontent = pnutpy.api.subscribe_channel(channelnum)
		serverresponse(postcontent)
	else:
		print("-not unsubscribed")

def getchannel():
	"""
	Get a public (chat) channel's details and most recent message.
	
	Arguments:
		none
	User input:
		Channel number.
	"""
	channelnumber = input("Get data, channelid? ")
	channelcontent = pnutpy.api.get_channel(channelnumber, include_raw=True)
	getchannelname(channelnumber, channelcontent)
	print("---------------")
	print("#" + str(channelcontent[0]["id"]) + " " + channelname + " c:" + "@" + channelcontent[0]["owner"]["username"])
	recentmessageid = str(channelcontent[0]['recent_message_id'])
	print("last: " + recentmessageid + ":")
	channelid = channelcontent[0]["id"]
	message = pnutpy.api.get_message(channelid, recentmessageid)
	print("@" + message[0]["user"]["username"] + ":")
	print(message[0]["content"]["text"])
	print("---------------")


# ------------------------------

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

def getuserposts():
	"""
	Get an account's posts.
	
	Arguments:
		none
	User input:
		User number.
	"""
	userid = input("User posts, userid? [return]=me: ")
	if userid == '':
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
			dummyvalue = 0
			# Not needed
		number -= 1

def getthread(postnum):
	"""
	Get a thread.
	
	Arguments:
		postnum:
			Post number to thread.
				if postnum == 0:
					ask for post number to thread
				else:
					thread from post
	User input:
		Post number, threads are displayed beginning with postnum.
	"""
	if postnum == 0:
		postnum = input("Get threadid? ")
	postcontent = pnutpy.api.posts_thread(postnum, count=retrievecount, include_raw=True)
	displaypost(postcontent)

def getbookmarks():
	"""
	Get the application user's bookmarks.
	
	Arguments:
		none
	User input:
		User number.
	"""
	userid = input("Bookmarks, userid? [return]=me: ")
	if userid == '':
		userid = "me"
	postcontent = pnutpy.api.users_bookmarked_posts(userid, count=retrievecount, include_raw=True)
	displaypost(postcontent)

def gethashtag():
	"""
	Get a list of posts containing the required hashtag.
	
	Arguments:
		none
	User input:
		Hashtag text.
	"""
	hashtag = input("Get hashtag? ")
	postcontent = pnutpy.api.posts_with_hashtag(hashtag, count = retrievecount, include_raw=True)
	displaypost(postcontent)

def getsubscribed():
	"""
	Get a list of the application user's subscribed channels.
	
	Arguments:
		none
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
			if channeltype == "chat":
				channelnumraw = pnutpy.api.get_channel(channelnumber, include_raw=True)
				try:
					channelname = channelnumraw[0]["raw"][0]["value"]["name"]
				except:
					channelname = channelnumraw[0]["raw"][1]["value"]["name"]
				print(channelname + ":")
			# Check for unread:
			if channelcontent[0][number]["has_unread"]:
				channelunread = "[u]"
			else:
				channelunread = ""
			# Build and display listing:
			print(channelunread + "#" + str(channelcontent[0][number]["id"]) + " " + channeltype + " c:@" + channelcontent[0][number]["owner"]["username"])
			# Build last message in channel:
			recentmessageid = str(channelcontent[0][number]['recent_message_id'])
			print("last: " + recentmessageid + ":")
			channelid = channelcontent[0][number]["id"]
			message = pnutpy.api.get_message(channelid, recentmessageid)
			print("@" + message[0]["user"]["username"] + ": " + message[0]["content"]["text"])
			print("---------------")
		except:
			dummyvalue = 0
			# Not needed
		number -= 1

def getmessages():
	"""
	Get a list of messages in a public channel, or a private channel the user has authorisation for.
	
	Arguments:
		none
	User input:
		Channel number.
	"""
	global channelnumber
	channelnumber = input("Messages in channelnum? ")
	postcontent = pnutpy.api.get_channel_messages(channelnumber, count = retrievecount, include_raw=True)
	displaymessage(postcontent)


# ------------------------------

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
	choice = input(("""| settings |
gc = change general count? ({0})
cc = change channel count? ({1})
[return] = back
""").format(str(retrievecount), str(channelcount)))
	# Set global retrieve count
	rcount = retrievecount
	if choice == "gc":
		# Does retrievecount variable already exist?
#		try:
#			dummyvalue = retrievecount
#		except:
#			retrievecount = 15
		print("-general count is currently", retrievecount)
		rcount = input("*Please change, to (>0)? ")
		if int(rcount) > 0:
			retrievecount = int(rcount)
			print("-general count is now", retrievecount, "posts")
	# Set channels retrieve count
	ccount = channelcount
	if choice == "cc":
		# Does channelcount variable already exist?
#		try:
#			dummyvalue = channelcount
#		except:
#			channelcount = 30
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
	print("-saved\n")

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
					dummyvalue = 0
					# Not needed
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
			dummyvalue = 0
			# Not needed
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
	menuseparator = "  Inline interactions menu:\n  [enter].next r.reply rp.repost\n  b.bookmark gth.get thread\n  x.exit"
	divider = separatormenu
	while not validaction:
		action = input(divider)
		if action == "help":
			print(menuseparator)
		if action == "":
			validaction = True
		if action == "r":
			replypost(postid)
			postid = 0
			validaction = True
		if action == "rp":
			repostpost(postid)
			postid = 0
			validaction = True
		if action == "b":
			bookmarkpost(postid)
			postid = 0
			validaction = True
		if action == "gth":
			getthread(postthreadid)
			# postid = 0 was here
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
					dummyvalue = 0
				print("---------------------------------")
		except:
			dummyvalue = 0
			# Not needed
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
		dummyvalue = 0

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

def serverresponse(postcontent):
	"""
	Displays status returned from the server after posts, messages, etc.
	
	Arguments:
		postcontent:
			The server's JSON response.
	User input:
		none
	"""
	status = ()
	status = postcontent[1]["code"]
	if status == 200:
		print("-ok")
	elif status == 201:
		print("-created")
	else:
		print(str(status) + "? hmmm... what's that now?")


# ------------------------------

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

# ------------------------------

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
main()
