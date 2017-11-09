# PigPen, a Python app for @33MHz's pnut.io social network.
# v0.1.29
# Site, changelog: https://github.com/bazbt3/PigPen
# made by: @bazbt3


# SETUP:

# Import @thrrgilag's library for interacting with pnut.io
import pnutpy
import sys

# Define global variables
global me, postcontent, number, posttext, jsondata, isdeleted
me = ''
postcontent = ()
number = 0
posttext = ''
jsondata = ()
isdeleted = ''


# AUTHORISATION:

# Authorise using secret token
tokenfile = open("secrettoken.txt", "r")
token = tokenfile.read()
token = token.strip()
pnutpy.api.add_authorization_token(token)


# DEFINE SUBROUTINES:

def menu():
# Displays menu text
	print "| PigPen | pnut u:" + str(me) + " |"
	print "menu=menu exit=exit"
	print "p  post     rp repost   m  mentions"
	print "r reply     g  getpost  gt getthread"
	print "s getsubs   sub subchan gc getchan"
	print "msg message gm getmsgs"
	print "gh hashtag  b bookmark  gb bookmarks"
	print "f follow    gu getuser  i interact's"
	print "t your tl   gg global"
	

# DEFINE INTERACTIONS WITH SINGLE RESULTS:

def createpost():
# Create a post
	inputtext()
	postcontent = pnutpy.api.create_post(data={'text': posttext})
	serverresponse(postcontent)

def replypost():
# Reply to a post
	getme()
	global posttext
	posttext = ''
	postnum= raw_input("Reply to postnum: ")
	postcontent = pnutpy.api.get_post(postnum)
	if not "is_deleted" in postcontent[0]:
		print "---------------"
		print "Replying to @" + postcontent[0]["user"]["username"] + ":"
		print postcontent[0]["content"]["text"]
		print "Don't forget to mention all!"
		print "---------------"
		inputtext()
		posttext = "@" + postcontent[0]["user"]["username"] + " " + posttext
		pnutpy.api.create_post(data={'reply_to': postnum, 'text': posttext})
		serverresponse(postcontent)

def createmessage():
# Create a message
	channelid = raw_input("channelid: ")
	inputtext()
	postcontent = pnutpy.api.create_message(channelid, data={'text': posttext})
	serverresponse(postcontent)

def repostpost():
# Repost a post
	postnum = raw_input("postnum: ")
	postcontent = pnutpy.api.repost_post(postnum)
	serverresponse(postcontent)

def getpost():
# Get a post
	postnum = raw_input("postnum: ")
	postcontent = pnutpy.api.get_post(postnum)
	print postcontent[0]
	print "--------------"
	if not "is_deleted" in postcontent[0]:
		userstatus(postcontent)
		timestarrpstatus(postcontent)
		print postcontent[0]["content"]["text"]
		postfooter(postcontent)
	else:
		print "[Post was deleted]"
	print "---------------"

def bookmarkpost():
# Bookmark a post
	postnum = raw_input("postnum: ")
	postcontent = pnutpy.api.bookmark_post(postnum)
	serverresponse(postcontent)

def followuser():
# Follow a user
	usernum = raw_input("usernum: ")
	postcontent = pnutpy.api.follow_user(usernum)
	serverresponse(postcontent)

def getuser():
# Get a user's data
	usernum = raw_input("usernum: ")
	postcontent = pnutpy.api.get_user(usernum)
	print ""
	print postcontent[0]["username"] + " - " + postcontent[0]["type"]
	if postcontent[0]["type"] == 'human':
		if postcontent[0]["name"]:
			print postcontent[0]["name"]
		if postcontent[0]["locale"]:
			print postcontent[0]["locale"]
		if postcontent[0]["timezone"]:
			print postcontent[0]["timezone"]
		if postcontent[0]["content"]["text"]:
			print postcontent[0]["content"]["text"]
	print ""
	print "posts: " + str(postcontent[0]["counts"]["posts"])
	print "followers: " + str(postcontent[0]["counts"]["followers"])
	print "following: " + str(postcontent[0]["counts"]["following"])
	print "bookmarks: " + str(postcontent[0]["counts"]["bookmarks"])
	print ""

def subscribetochannel():
# Subscribe to a channel
	channelnum = raw_input("channelnum: ")
	postcontent = pnutpy.api.subscribe_channel(channelnum)
	serverresponse(postcontent)

def getchannel():
# Get channel details
# Small mods to getsubscribed code
	channelnumber = raw_input("channelnum: ")
	channelcontent = pnutpy.api.get_channel(channelnumber, data={'include_raw': '1', 'include_channel_raw': '1', 'include_user_raw': '1'})
	print "---------------"
	print "#" + str(channelcontent[0]["id"]) + " o: " + "@" + channelcontent[0]["owner"]["username"]
	recentmessageid = str(channelcontent[0]['recent_message_id'])
	print "most recent: " + recentmessageid + ":"
	channelid = channelcontent[0]["id"]
	message = pnutpy.api.get_message(channelid, recentmessageid)
	print "@" + message[0]["user"]["username"] + ":"
	print message[0]["content"]["text"]
	print "---------------"


# DEFINE INTERACTIONS WITH MULTIPLE RESULTS:

def getunified():
# Get unified timeline
# (Server returns last 20 by default)
	postcontent = pnutpy.api.users_post_streams_unified()
	displaypost(postcontent)

def getglobal():
# Get global timeline
# (Server returns last 20 by default)
	postcontent = pnutpy.api.posts_streams_global()
	displaypost(postcontent)

def getmentions():
# Get mentions
# (Server returns last 20 by default)
	userid = raw_input("user_id ([return]=me): ")
	if userid == '':
		userid = "me"
	postcontent = pnutpy.api.users_mentioned_posts(userid)
	displaypost(postcontent)

def getinteractions():
# Get user interactions
# (Server returns last 20 by default)
	userid = raw_input("user_id ([return]=me): ")
	if userid == '':
		userid = "me"
	postcontent = pnutpy.api.interactions_with_user(userid)
	global number
	number = 19
	print "---------------"
	while number >= 0:
		try:
			print postcontent[0][number]["action"] + " by @" + postcontent[0][number]["users"][0]["username"] + " ref.:"
			print postcontent[0][number]["event_date"]
			print postcontent[0][number]["objects"][0]["content"]["text"]
			print "---------------"
		except:
			sys.exc_clear()
		number -= 1

def getthread():
# Get thread
# (Server returns last 20 by default)
	thread = raw_input("thread: ")
	postcontent = pnutpy.api.posts_thread(thread, data={'count': '50'})
	displaypost(postcontent)

def getbookmarks():
# Get bookmarks
# (Server returns last 20 by default)
	userid = raw_input("user_id ([return]=me): ")
	if userid == '':
		userid = "me"
	postcontent = pnutpy.api.users_bookmarked_posts(userid)
	displaypost(postcontent)

def gethashtag():
# Get hashtag
# (Server returns last 20 by default)
	hashtag = raw_input("hashtag: ")
	postcontent = pnutpy.api.posts_with_hashtag(hashtag)
	displaypost(postcontent)

def getsubscribed():
# Get subscribed channels
# (Server returns last 20 by default)
# Duplicates code in getchannel
	channelcontent = pnutpy.api.subscribed_channels()
	global number
	number = 19
	print "---------------"
	while number >= 0:
		try:
			print "#" + str(channelcontent[0][number]["id"]) + " o: " + "@" + channelcontent[0][number]["owner"]["username"]
			recentmessageid = str(channelcontent[0][number]['recent_message_id'])
			print "most recent: " + recentmessageid + ":"
			channelid = channelcontent[0][number]["id"]
			message = pnutpy.api.get_message(channelid, recentmessageid)
			print message[0]["content"]["text"]
			print "---------------"
		except:
			sys.exc_clear()
		number -= 1

def getmessages():
# Get messages
# (Server returns last 20 by default)
	global channelnumber
	channelnumber = raw_input("channelnum: ")
	postcontent = pnutpy.api.get_channel_messages(channelnumber)
	displaymessage(postcontent)


# DEFINE OTHER ROUTINES:

def getme():
	global me
	userid = pnutpy.api.get_user("me")
	me = "@" + userid[0]["username"]

def inputtext():
# Input text, '\n'=newline
	global posttext
	posttext = ''
	textinput = raw_input("posttext (\\n): ")
	# Silly things:
	if textinput.startswith("/me"):
		textinput = "+bazbt3" + textinput[3:]
	# Back to sensible
	splittext = textinput.split(r'\n')
	for sentence in splittext:
		posttext = posttext + sentence + "\n"
	posttext = posttext.strip()

def userstatus(postcontent):
# Display poster status
	userstatus = "@" + postcontent[0]["user"]["username"] + ": [u:" + str(postcontent[0]["user"]["id"])
	if postcontent[0]["user"]["you_follow"]:
		userstatus += "+f"
	if postcontent[0]["user"]["follows_you"]:
		userstatus += "+F"
	print userstatus + "]"

def timestarrpstatus(postcontent):
# Display my interactions
	poststatus =  str(postcontent[0]["created_at"]) + " ["
	if postcontent[0]["you_bookmarked"]:
		poststatus += "*"
	if postcontent[0]["you_reposted"]:
		poststatus += "rp"
	print poststatus + "]"

def postfooter(postcontent):
# Display post data
	postrefs = " id:" + str(postcontent[0]["id"])
	if "reply_to" in postcontent[0]:
		postrefs += " rep:" + str(postcontent[0]["reply_to"])
	postrefs += " thd:" + str(postcontent[0]["thread_id"])
	print postrefs

def displaypost(postcontent):
# Display post (not message) content
	global number
	number = 25
	print "---------------"
	while number >= 0:
		try:
			if not "is_deleted" in postcontent[0][number]:
				# Build user status:
				userstatus = "@" + postcontent[0][number]["user"]["username"] + ": [u:" + str(postcontent[0][number]["user"]["id"])
				if postcontent[0][number]["user"]["you_follow"]:
					userstatus += "+f"
				if postcontent[0][number]["user"]["follows_you"]:
					userstatus += "+F"
				print userstatus + "]"
				# Build post status indicators:
				poststatus =  str(postcontent[0][number]["created_at"]) + " ["
				if postcontent[0][number]["you_bookmarked"]:
					poststatus += "*"
				if postcontent[0][number]["you_reposted"]:
					poststatus += "rp"
				print poststatus + "]"
				# Display post text:
				print postcontent[0][number]["content"]["text"]
				# Build hierarchy links:
				postrefs = " id:" + str(postcontent[0][number]["id"])
				if "reply_to" in postcontent[0][number]:
					postrefs += " rep:" + str(postcontent[0][number]["reply_to"])
				postrefs += " thd:" + str(postcontent[0][number]["thread_id"])
				print postrefs
				print "---------------------------------"
		except:
			sys.exc_clear()
		number -= 1
	print""

def displaymessage(postcontent):
# Display message (not post) content
# Same base as displaypost() but with interaction status indicators removed
	global number
	number = 19
	print "---------------"
	while number >=0:
		try:
			if not "is_deleted" in postcontent[0][number]:	
				userstatus = "@" + postcontent[0][number]["user"]["username"] + ":" + " ["
				if postcontent[0][number]["user"]["you_follow"]:
					userstatus += "+f"
				if postcontent[0][number]["user"]["follows_you"]:
					userstatus += "+F"
				print userstatus + "]"
				print postcontent[0][number]["content"]["text"]
				print "---------------------------------"
		except:
			sys.exc_clear()
		number -= 1
	print ""

def serverresponse(postcontent):
# Return server response code
	status = ()
	status = postcontent[1]["code"]
	if status == 200:
		print "ok"
	elif status == 201:
		print "ok"
	else:
		print str(status) + " = hmmm..."


# MAIN ROUTINE:

# Get app user ID
getme()
# Display menu
menu()

#Command entry:
# The menu has no input validation outside valid options:
choice = 'Little Bobby Tables'
while choice != 'exit':
	choice = raw_input("Choice? ")
	if choice == 'p':
 		createpost()
	elif choice == 'r':
		replypost()
	elif choice == 'b':
		bookmarkpost()
	elif choice == 'rp':
		repostpost()
	elif choice == 'f':
		followuser()
	elif choice == 'g':
		getpost()
	elif choice == 'm':
		getmentions()
	elif choice == 'gh':
		gethashtag()
	elif choice == 's':
		getsubscribed()
	elif choice == 'msg':
		createmessage()
	elif choice == 'gt':
		getthread()
	elif choice == 'gc':
		getchannel()
	elif choice == 'gm':
		getmessages()
	elif choice == 'gb':
		getbookmarks()
	elif choice == "t":
		getunified()
	elif choice == "gg":
		getglobal()
	elif choice == "i":
		getinteractions()
	elif choice == "gu":
		getuser()
	elif choice == "sub":
		subscribetochannel()
	elif choice == 'menu':
		menu()

# The app exits here once 'exit' is typed:
print " "
print "You chose 'exit': Goodbye!"
