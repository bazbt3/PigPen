# PigPen, a Python app for the pnut.io social network.
# v0.01.20
# @bazbt3

# SETUP:

# Import @thrrgilag's pnut.io library
import pnutpy

# Global variables
global postcontent, jsondata
postcontent = ()
jsondata = ()


# AUTHORISATION:

# Authorise using secret token
tokenfile = open("secrettoken.txt", "r")
token = tokenfile.read()
token = token.strip()
pnutpy.api.add_authorization_token(token)


# DEFINE SUBROUTINES:

# Displays menu text
def menu():
	print "\nPigPen menu:"
	print "p post         rp repost(n)"
	print "g getpost(n)   r  reply(n)"
	print "b bookmark(n)  f follow(n)"
	print "m mentions(u)  h hashtag(t)"
	print "msg create message(n)"
	print "s subscribed   gc get channel(n)"
	print "menu show menu"
	print "exit Exit\n"


# DEFINE INTERACTIONS WITH SINGLE RESULTS:

# Create a post
def createpost():
	inputtext()
	postcontent = pnutpy.api.create_post(data={'text': posttext})
	serverresponse(postcontent)

# Reply to a post
def replypost():
	postnum= raw_input("postnum: ")
	inputtext()
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
	# Print server JSON
	print "@" + postcontent[0]["user"]["username"] + ":"
	print postcontent[0]["created_at"]
	print postcontent[0]["content"]["text"]
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
# Small mods to code from getsubscribed
def getchannel():
	number = raw_input("channelnum: ")
	channelcontent = pnutpy.api.get_channel(number, data={'include_raw': 1})
	print "#" + str(channelcontent[0]["id"]) + " o: " + "@" + channelcontent[0]["owner"]["username"]
	recentmessageid = str(channelcontent[0]['recent_message_id'])
	print "most recent: " + recentmessageid + ":"
	channelid = channelcontent[0]["id"]
	message = pnutpy.api.get_message(channelid, recentmessageid)
	print message[0]["content"]["text"]
	print "---------------"


# DEFINE INTERACTIONS WITH MULTIPLE RESULTS:
# *Lots* of duplication!

# Get mentions
# (Server returns last 20 by default)
def getmentions():
	userid = raw_input("user_id: ")
	postcontent = pnutpy.api.users_mentioned_posts(userid)
	global number
	number = 19
	print "---------------"
	while number >= 0:
		print "@" + postcontent[0][number]["user"]["username"] + ":  " + "p:" + str(postcontent[0][number]["id"]) + " t:" + postcontent[0][number]["thread_id"]
		print postcontent[0][number]["created_at"]
		print postcontent[0][number]["content"]["text"]
		print "---------------"
		number -= 1
	print ""

# Get hashtag
# (Server returns last 20 by default)
def gethashtag():
	hashtag = raw_input("hashtag: ")
	postcontent = pnutpy.api.posts_with_hashtag(hashtag)
	global number
	number = 19
	print "---------------"
	while number >= 0:
		print "@" + postcontent[0][number]["user"]["username"] + ":  " + "p:" + str(postcontent[0][number]["id"]) + " t:" + postcontent[0][number]["thread_id"]
		print postcontent[0][number]["created_at"]
		print postcontent[0][number]["content"]["text"]
		print "---------------"
		number -= 1

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


# DEFINE OTHER ROUTINES:

# Input text, '\n'=newline
def inputtext():
	global posttext
	posttext = ""
	textinput = raw_input("posttext (\\n): ")
	splittext = textinput.split(r'\n')
	for sentence in splittext:
		posttext = posttext + sentence + "\n"
	posttext = posttext.strip()

# Return server response code
def serverresponse(postcontent):
	status = ()
	status = postcontent[1]["code"]
	if status == 200:
		print "ok"
	else:
		print str(status) + " = oops!"


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
	elif choice == 'h':
		gethashtag()
	elif choice == 's':
		getsubscribed()
	elif choice == 'gc':
		getchannel()
	elif choice == 'msg':
		createmessage()
	elif choice == 'menu':
		menu()

# The app exits here once 'exit' is typed:
print " "
print "You chose 'exit': Goodbye!"
