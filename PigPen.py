# PigPen, a Python app for @33MHz's pnut.io social network.
# v0.1.25 - see changelog at:
# https://github.com/bazbt3/PigPen
# @bazbt3

# SETUP:

# Import @thrrgilag's library for interacting with pnut.io
import pnutpy

# Global variables
global postcontent, posttext, jsondata, me, isdeleted
postcontent = ()
posttext = ''
jsondata = ()
me = ''
isdeleted = ''


# AUTHORISATION, IDENTITY:

# Authorise using secret token
tokenfile = open("secrettoken.txt", "r")
token = tokenfile.read()
token = token.strip()
pnutpy.api.add_authorization_token(token)

# User ID
mefile = open("me.txt", "r")
me = mefile.read()
me = me.strip()


# DEFINE SUBROUTINES:

# Displays menu text
def menu():
	print "\nPigPen | menu=menu exit=exit"
	print " p post        m mentions(user)"
	print " r reply       g get post"
	print " rp repost     gt get thread"
	print " f follow      gh get hashtag"
	print " b bookmark    gb get bookmarks"
	print " u unified tl  gg get global tl"
	print " msg message   gm get msgs"
	print " s subscribed  gc get channel"


# DEFINE INTERACTIONS WITH SINGLE RESULTS:

# Create a post
def createpost():
	inputtext()
	postcontent = pnutpy.api.create_post(data={'text': posttext})
	serverresponse(postcontent)

# Reply to a post
def replypost():
	global posttext
	posttext =''
	postnum= raw_input("postnum: ")
	postcontent = pnutpy.api.get_post(postnum)
	if not "is_deleted" in postcontent[0]:
		print "---------------"
		print "Replying to @" + postcontent[0]["user"]["username"] + ":"
		print postcontent[0]["content"]["text"]
		print "---------------"
	inputtext()
	posttext = "@" + postcontent[0]["user"]["username"] + " " + posttext
	postcontent = pnutpy.api.create_post(data={'reply_to': postnum, 'text': posttext})
	serverresponse(postcontent)

# Create a message
def createmessage():
	channelid = raw_input("channelid: ")
	inputtext()
	postcontent = pnutpy.api.create_message(channelid, data={'text': posttext})
	serverresponse(postcontent)

# Repost a post
def repostpost():
	postnum = raw_input("postnum: ")
	postcontent = pnutpy.api.repost_post(postnum)
	serverresponse(postcontent)

# Get a post
def getpost():
	postnum = raw_input("postnum: ")
	postcontent = pnutpy.api.get_post(postnum)
	if not "is_deleted" in postcontent[0]:
		print "@" + postcontent[0]["user"]["username"] + ":"
		print postcontent[0]["created_at"]
		print postcontent[0]["content"]["text"]
	else:
		print "[Post was deleted]"
	print "---------------"

# Bookmark a post
def bookmarkpost():
	postnum = raw_input("postnum: ")
	postcontent = pnutpy.api.bookmark_post(postnum)
	serverresponse(postcontent)

# Follow a user
def followuser():
	usernum = raw_input("usernum: ")
	postcontent = pnutpy.api.follow_user(usernum)
	serverresponse(postcontent)

# Get channel details
# Small mods to getsubscribed code
def getchannel():
	channelnumber = raw_input("channelnum: ")
	channelcontent = pnutpy.api.get_channel(channelnumber, data={'include_raw': 1, 'include_channel_raw': 1})
#	print "---------------"
#	print channelcontent
#	print "---------------"
	print "#" + str(channelcontent[0]["id"]) + " o: " + "@" + channelcontent[0]["owner"]["username"]
	recentmessageid = str(channelcontent[0]['recent_message_id'])
	print "most recent: " + recentmessageid + ":"
	channelid = channelcontent[0]["id"]
	message = pnutpy.api.get_message(channelid, recentmessageid)
	print message[0]["content"]["text"]
	print "---------------"


# DEFINE INTERACTIONS WITH MULTIPLE RESULTS:

# Get user's unified timeline
# (Server returns last 20 by default)
def getunified():
	postcontent = pnutpy.api.users_post_streams_unified()
	displaypost(postcontent)

# Get global timeline
# (Server returns last 20 by default)
def getglobal():
	postcontent = pnutpy.api.posts_streams_global()
	displaypost(postcontent)

# Get mentions
# (Server returns last 20 by default)
def getmentions():
	userid = raw_input("user_id ([return]=me): ")
	if userid == '':
		userid = me
	postcontent = pnutpy.api.users_mentioned_posts(userid)
	displaypost(postcontent)

# Get thread
# (Server returns last 20 by default)
def getthread():
	thread = raw_input("thread: ")
	postcontent = pnutpy.api.posts_thread(thread)
	displaypost(postcontent)

# Get bookmarks
# (Server returns last 20 by default)
def getbookmarks():
	userid = raw_input("user_id ([return]=me): ")
	if userid == '':
		userid = me
	postcontent = pnutpy.api.users_bookmarked_posts(userid)
	displaypost(postcontent)

# Get hashtag
# (Server returns last 20 by default)
def gethashtag():
	hashtag = raw_input("hashtag: ")
	postcontent = pnutpy.api.posts_with_hashtag(hashtag)
	displaypost(postcontent)

# Get subscribed channels
# (Server returns last 20 by default)
# Duplicates code in getchannel
def getsubscribed():
	channelcontent = pnutpy.api.subscribed_channels()
	global number
	number = 19
	print "---------------"
	while number >= 0:
		print "#" + str(channelcontent[0][number]["id"]) + " o: " + "@" + channelcontent[0][number]["owner"]["username"]
		recentmessageid = str(channelcontent[0][number]['recent_message_id'])
		print "most recent: " + recentmessageid + ":"
		channelid = channelcontent[0][number]["id"]
		message = pnutpy.api.get_message(channelid, recentmessageid)
		print message[0]["content"]["text"]
		print "---------------"
		number -= 1

# Get messages
# (Server returns last 20 by default)
def getmessages():
	global channelnumber
	channelnumber = raw_input("channelnum: ")
	postcontent = pnutpy.api.get_channel_messages(channelnumber)
	displaymessage(postcontent)


# DEFINE OTHER ROUTINES:

# Input text, '\n'=newline
def inputtext():
	global posttext
	posttext = ''
	textinput = raw_input("posttext (\\n): ")
	splittext = textinput.split(r'\n')
	for sentence in splittext:
		posttext = posttext + sentence + "\n"
	posttext = posttext.strip()

# Display post (not message) content
def displaypost(postcontent):
	global number
	number = 19
	print "---------------"
	while number >= 0:
		if not "is_deleted" in postcontent[0][number]:
			userstatus = "@" + postcontent[0][number]["user"]["username"] + ": [u:" + str(postcontent[0][number]["user"]["id"])
			if postcontent[0][number]["user"]["you_follow"]:
				userstatus += "+f"
			if postcontent[0][number]["user"]["follows_you"]:
				userstatus += "+F"
			print userstatus + "]"
			# Builds status indicators
			poststatus =  str(postcontent[0][number]["created_at"]) + " ["
			if postcontent[0][number]["you_bookmarked"]:
				poststatus += "*"
			if postcontent[0][number]["you_reposted"]:
				poststatus += " rp"
			print poststatus + "]"
			print postcontent[0][number]["content"]["text"]
			postrefs = " id:" + str(postcontent[0][number]["id"])
			if "reply_to" in postcontent[0][number]:
				postrefs += " rep:" + str(postcontent[0][number]["reply_to"])
			postrefs += " thd:" + str(postcontent[0][number]["thread_id"])
			print postrefs
			print "---------------------------------"
		number -= 1
	print""

# Display message (not post) content
# Same base as displaypost() but with status indicators removed
def displaymessage(postcontent):
	global number
	number = 19
	print "---------------"
	while number >= 0:
		if not "is_deleted" in postcontent[0][number]:
			userstatus = "@" + postcontent[0][number]["user"]["username"] + ":" + " ["
			if postcontent[0][number]["user"]["you_follow"]:
				userstatus += "f"
			if postcontent[0][number]["user"]["follows_you"]:
				userstatus += "+F"
			print userstatus + "]"
			print postcontent[0][number]["content"]["text"]
			print "---------------------------------"
		number -= 1
	print""

# Return server response code
def serverresponse(postcontent):
	status = ()
	status = postcontent[1]["code"]
	if status == 200:
		print "ok"
	elif status == 201:
		print "ok"
	else:
		print str(status) + " = hmmm..."


# MAIN ROUTINE:

# Display menu
menu()
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
	elif choice == "u":
		getunified()
	elif choice == "gg":
		getglobal()
	elif choice == 'menu':
		menu()

# The app exits here once 'exit' is typed:
print " "
print "You chose 'exit': Goodbye!"
