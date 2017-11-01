# PigPen, a Python app for the pnut.io social network.
# v0.01.18
# @bazbt3

# SETUP:

# Import @thrrgilag's pnut.io library
import pnutpy
from pprint import pprint

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
	print "m mentions"
	print "menu show menu"
	print "exit Exit\n"


# DEFINE INTERACTIONS WITH SINGLE RESULTS:

# Create a post
def createpost():
	inputtext()
	postcontent = pnutpy.api.create_post(data={'text': posttext})
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

# Reply to a post
def replypost():
	postnum= raw_input("postnum: ")
	inputtext()
	postcontent = pnutpy.api.create_post(data={'reply_to': postnum, 'text': posttext})
	serverresponse(postcontent)

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


# DEFINE INTERACTIONS WITH MULTIPLE RESULTS:

# Get mentions
# (Server returns last 20 by default)
def getmentions():
	userid = raw_input("user_id: ")
	postcontent = pnutpy.api.users_mentioned_posts(userid)
	global number
	number = 0
	print "---------------"
	print "thread: " + postcontent[0][number]["thread_id"]
	print "---------------"
	while number <19:
		print "post:   " + str(postcontent[0][number]["id"])
		print "@" + postcontent[0][number]["user"]["username"] + ":"
		print postcontent[0][number]["created_at"]
		print postcontent[0][number]["content"]["text"]
		print "---------------"
		number += 1
	print ""
	print serverresponse(postcontent)


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
	elif choice == 'menu':
		menu()

# The app exits here once 'exit' is typed:
print " "
print "You chose 'exit': Goodbye!"
