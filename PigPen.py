#     ___          ___
#    / _ |__ ___  / _ | ___  __ 
#   / ////_// _ \/ //// // |/  \
#  / __// // //// __// ___ / /\|
# /_/  /_/ |_ //_/   |___//_//_/
#         /__/   
# v0.3.2 for Python 3.5

# PigPen, a Python app for @33MHz's pnut.io social network

# Site, changelog: https://github.com/bazbt3/PigPen
# made by: @bazbt3


# SETUP:

# Import @33MHz and @thrrgilag's library for interacting with pnut.io
import pnutpy
# Import other libraries:
# May not need this (was used for early Python 2.7 exception handling):
import sys

# Define global variables
global action, isdeleted, maxpostlen, me, number, postcontent, postid, posttext, postthreadid, retrievecount
action = ''
isdeleted = ''
maxpostlen = 256
me = ''
number = 0
postcontent = ()
postid = 0
postthreadid = 0
posttext = ''
retrievecount = 30


# AUTHORISATION:

# Authorise using secret token
tokenfile = open("secrettoken.txt", "r")
token = tokenfile.read()
token = token.strip()
pnutpy.api.add_authorization_token(token)


# DEFINE SUBROUTINES:

def menu():
	# Displays menu text
	print("""| PigPen | pnut u:@{0}
gg global timeline  gt your timeline
p  post     rp repost   gm mentions
r reply     gth getthrd gp getpost
b bookmark  gb bookmrks gh 'hashtag'
f follow    gu getuser  gi interacts
msg message gms getmsgs gs getsubs
gc getchanl sub subscribechannel
| help=menu exit=exit""".format(str(me)))
	

# DEFINE INTERACTIONS WITH SINGLE RESULTS:

def createpost():
	# Create a post, < maxpostlen
	postlimit = True
	while postlimit: 
		inputtext()
		if len(posttext) > maxpostlen:
			print("")
			print("*** Too big, " + str(len(posttext)) + " chars.) Redo:")
		else:
			postlimit = False
	postcontent = pnutpy.api.create_post(data={'text': posttext})
	serverresponse(postcontent)

def replypost(postnum):
	# Reply to a post
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

def createmessage():
	# Create a message
	channelid = input("Message to channelid? ")
	inputtext()
	postcontent = pnutpy.api.create_message(channelid, data={'text': posttext})
	serverresponse(postcontent)

def repostpost(postnum):
	# Repost a post
	if postnum == 0:
		postnum = input("Repost postnum? ")
	postcontent = pnutpy.api.repost_post(postnum)
	serverresponse(postcontent)

def bookmarkpost(postnum):
	# Bookmark a post
	if postnum == 0:
		postnum = input("Bookmark postnum? ")
	postcontent = pnutpy.api.bookmark_post(postnum)
	serverresponse(postcontent)

def followuser():
	# Follow a user
	usernum = input("Follow usernum? ")
	postcontent = pnutpy.api.follow_user(usernum)
	serverresponse(postcontent)

def getpost():
	# Get a post
	postnum = input("Get postnum? ")
	postcontent = pnutpy.api.get_post(postnum, include_raw = True)
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
			thing = postcontent[0]["content"]["text"]
		except (KeyError):
			dunmyvalue = 0
		print(thing)
	print("")
	print("posts: " + str(postcontent[0]["counts"]["posts"]))
	print("followers: " + str(postcontent[0]["counts"]["followers"]))
	print("following: " + str(postcontent[0]["counts"]["following"]))
	print("bookmarks: " + str(postcontent[0]["counts"]["bookmarks"]))
	print("")

def subscribetochannel():
	# Subscribe to a channel
	channelnum = input("Subscribe to channelnum? ")
	postcontent = pnutpy.api.subscribe_channel(channelnum)
	serverresponse(postcontent)

def getchannel():
	# Get channel details
	channelnumber = input("Get data, channelnum? ")
	channelcontent = pnutpy.api.get_channel(channelnumber, include_raw=True)
	channelname = channelcontent[0]["raw"][0]["value"]["name"]
	print("---------------")
	print("#" + str(channelcontent[0]["id"]) + " " + channelname + " c:" + "@" + channelcontent[0]["owner"]["username"])
	recentmessageid = str(channelcontent[0]['recent_message_id'])
	print("last: " + recentmessageid + ":")
	channelid = channelcontent[0]["id"]
	message = pnutpy.api.get_message(channelid, recentmessageid)
	print("@" + message[0]["user"]["username"] + ":")
	print(message[0]["content"]["text"])
	print("---------------")


# DEFINE INTERACTIONS WITH MULTIPLE RESULTS:

def getunified():
	# Get unified timeline
	# (Server returns last 20 by default)
	postcontent = pnutpy.api.users_post_streams_unified(count = retrievecount, include_raw = True)
	displaypost(postcontent)

def getglobal():
	# Get global timeline
	# (Server returns last 20 by default)
	postcontent = pnutpy.api.posts_streams_global(count = retrievecount, include_raw = True)
	displaypost(postcontent)

def getmentions():
	# Get mentions
	# (Server returns last 20 by default)
	userid = input("User mentions, userid? [return]=me: ")
	if userid == '':
		userid = "me"
	postcontent = pnutpy.api.users_mentioned_posts(userid, count = retrievecount, include_raw = True)
	displaypost(postcontent)

def getinteractions():
	# Get user interactions
	# (Server returns last 20 by default)
	userid = input("Interacts, userid? [return]=me: ")
	if userid == '':
		userid = "me"
	postcontent = pnutpy.api.interactions_with_user(userid, count = retrievecount)
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
	# Get thread
	# (Server returns last 20 by default)
	if postnum == 0:
		postnum = input("Get threadid? ")
	postcontent = pnutpy.api.posts_thread(postnum, count = retrievecount, include_raw = True)
	displaypost(postcontent)

def getbookmarks():
	# Get bookmarks
	# (Server returns last 20 by default)
	userid = input("Bookmarks, userid? [return]=me: ")
	if userid == '':
		userid = "me"
	postcontent = pnutpy.api.users_bookmarked_posts(userid, count = retrievecount, include_raw = True)
	displaypost(postcontent)

def gethashtag():
	# Get hashtag
	# (Server returns last 20 by default)
	hashtag = input("Get hashtag? ")
	postcontent = pnutpy.api.posts_with_hashtag(hashtag, count = retrievecount, include_raw = True)
	displaypost(postcontent)

def getsubscribed():
	# Get subscribed channels
	# (Server returns last 20 by default)
	# Duplicates code in getchannel
	channelcontent = pnutpy.api.subscribed_channels(count = retrievecount)
	global number
	number = retrievecount
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
				channelname = channelnumraw[0]["raw"][0]["value"]["name"]
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
	# Get messages
	# (Server returns last 20 by default)
	global channelnumber
	channelnumber = input("Messages in channelnum? ")
	postcontent = pnutpy.api.get_channel_messages(channelnumber, count = retrievecount)
	displaymessage(postcontent)


# DEFINE OTHER ROUTINES:

def getme():
	global me
	userid = pnutpy.api.get_user("me")
	me = userid[0]["username"]

def inputtext():
	# Input text, '\n'=newline:
	global posttext
	posttext = ''
	textinput = ""
	while not textinput:
		textinput = input("Write here (\\n=newline): ")
		if not textinput:
			print ("-Empty post, retry-")
	# Silly things:
	if textinput.startswith("/me"):
		textinput = "+" + me + textinput[3:]
	# Back to sensible
	splittext = textinput.split(r'\n')
	for sentence in splittext:
		posttext = posttext + sentence + "\n"
	posttext = posttext.strip()

def displaypost(postcontent):
	# Display post (not message) content:
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
#				checkoembed(postcontent, "")
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
	global action
	validaction = False
	separatormenu = " ------------------------------- "
	menuseparator = "  Inline interactions menu:\n  [enter]=next r=reply rp=repost\n  b=bookmark gth=get thread\n  x=exit"
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
			postid = 0
			validaction = True
			print("-back to list-")
		if action == "x":
			print("-back to main menu-")
			validaction = True
			return

def displaymessage(postcontent):
	# Display message (not post) content
	# Same base as displaypost() but with interaction status indicators removed
	global number
	number = retrievecount
	print("---------------")
	while number >= 0:
		try:
			if not "is_deleted" in postcontent[0][number]:
				userstatus = "@" + postcontent[0][number]["user"]["username"] + ":" + " ["
				if postcontent[0][number]["user"]["you_follow"]:
					userstatus += "+f"
				if postcontent[0][number]["user"]["follows_you"]:
					userstatus += "+F"
				print(userstatus + "]")
				print(postcontent[0][number]["content"]["text"])
				print("---------------------------------")
		except:
			dummyvalue = 0
			# Not needed
		number -= 1
	print("")

def userstatus(postcontent):
	# Display poster status
	userstatus = "@" + postcontent[0]["user"]["username"] + ": [u:" + str(postcontent[0]["user"]["id"])
	if postcontent[0]["user"]["you_follow"]:
		userstatus += "+f"
	if postcontent[0]["user"]["follows_you"]:
		userstatus += "+F"
	print(userstatus + "]")

def timestarrpstatus(postcontent):
	# Display my interactions
	poststatus = str(postcontent[0]["created_at"]) + " ["
	if postcontent[0]["you_bookmarked"]:
		poststatus += "*"
	if postcontent[0]["you_reposted"]:
		poststatus += "rp"
	print(poststatus + "]")

def checkoembed(postcontent, raw):
	try:
		if raw["type"] == "io.pnut.core.oembed":
			# Get image page URL:
			oembedimgurl = raw["value"]["url"]
			print("[url:]")
			print(oembedimgurl)
			# Get thumbnail URL:
			oembedimgthumb = raw["value"]["thumbnail_url"]
			print("[thumb:]")
			print(oembedimgthumb)
	except (KeyError):
		dummyvalue = 0

def postfooter(postcontent):
	# Display post data
	postrefs = " id:" + str(postcontent[0]["id"])
	if "reply_to" in postcontent[0]:
		postrefs += " rep:" + str(postcontent[0]["reply_to"])
	postrefs += " thd:" + str(postcontent[0]["thread_id"])
	print(postrefs)

def serverresponse(postcontent):
	# Return server response code
	status = ()
	status = postcontent[1]["code"]
	if status == 200:
		print("ok")
	elif status == 201:
		print("ok")
	else:
		print(str(status) + " = hmmm...")


# MAIN ROUTINE:

# Get pnut.io username
getme()
# Display menu
menu()

# Command entry:
# The menu has no input validation outside valid options:
choice = 'Little Bobby Tables'
while choice != 'exit':
	choice = input("Choice? ")
	# Add in alphabetic order to easily scan through
	if choice == 'b':
		bookmarkpost(0)
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
	elif choice == "gu":
		getuser()
	elif choice == 'help':
		menu()
	elif choice == 'msg':
		createmessage()
	elif choice == 'p':
		createpost()
	elif choice == 'r':
		replypost(0)
	elif choice == 'rp':
		repostpost(0)
	elif choice == "sub":
		subscribetochannel()

# The app exits here once 'exit' is typed:
print(" ")
print("You chose 'exit': Goodbye!")

