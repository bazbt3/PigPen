# PigPen, a Python app for the pnut.io social network.
# v0.01.12
# @bazbt3

# SETUP:

# Import @thrrgilag's pnut.io library
import pnutpy
# Import JSON to allow server responses to be parsed
import json

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
	print "m show menu"
	print "exit Exit\n"

# DEFINE INTERACTIONS

# Create a post
def createpost():
	inputtext()
	post, meta = pnutpy.api.create_post(data={'text': posttext})

# Repost a post
def repostpost():
	postnum = raw_input("postnum: ")
	postcontent = pnutpy.api.repost_post(postnum)

# Get a post
def getpost():
	global postcontent, jsondata
	postcontent = ()
	jsondata = ()
	postnum = raw_input("postnum: ")
	postcontent = pnutpy.api.get_post(postnum)
	# Print server JSON
	print postcontent

# Reply to a post
def replypost():
	postnum= raw_input("postnum: ")
	inputtext()
	post, meta = pnutpy.api.create_post(data={'reply_to': postnum, 'text': posttext})

# Bookmark a post
def bookmarkpost():
	postnum = raw_input("postnum: ")
	postcontent = pnutpy.api.bookmark_post(postnum)

# Follow a user
def followuser():
	usernum = raw_input("usernum: ")
	postcontent = pnutpy.api.follow_user(usernum)

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
		menu()

# The app exits here once 'exit' is typed:
print " "
print "You chose 'exit': Goodbye!"
