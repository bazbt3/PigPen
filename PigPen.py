# PigPen, a Python app for the pnut.io social network
# @bazbt3

# THE APP:

# Import @thrrgilag's pnut.io library
import pnutpy

# Authorise using secret token
tokenfile = open("secrettoken.txt", "r")
token = tokenfile.read()
token = token.strip()
pnutpy.api.add_authorization_token(token)

# DEFINE SUBROUTINES:

# Displays menu text
def menu():
	print "PigPen menu:"
	print "  p =  post"
	print "  r =  reply"
	print "  b =  bookmark"
	print "  rp = repost"
	print "  g =  get post"
	print "  menu = redisplay menu"
	print "  exit = Exit"
	print " "

# DEFINE INTERACTIONS

# Create a post
def createpost():
	inputtext()
	post, meta = pnutpy.api.create_post(data={'text': posttext})

# Reply to a post
def replypost():
	postnum= raw_input("postnum: ")
	inputtext()
	post, meta = pnutpy.api.create_post(data={'reply_to': postnum, 'text': posttext})

# Bookmark a post
def bookmarkpost():
	postnum= raw_input("postnum: ")
	postcontent = pnutpy.api.bookmark_post(postnum)

# Repost a post
def repostpost():
	postnum= raw_input("postnum: ")
	postcontent = pnutpy.api.repost_post(postnum)

# Get a post
def getpost():
	postnum= raw_input("postnum: ")
	postcontent = pnutpy.api.get_post(postnum)
	print postcontent

# DEFINE OTHER ROUTINES

# Input text, act on '\n'
def inputtext():
	global posttext
	posttext = ""
	textinput = raw_input("posttext (\\n): ")
	splittext = textinput.split(r'\n')
	for sentence in splittext:
		posttext = posttext + sentence + "\n"
	posttext = posttext.strip()
	
# MAIN ROUTINE

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
	elif choice == 'g':
		getpost()
	elif choice == 'menu':
		menu()

# The app exits here once 'exit' is typed:
print " "
print "You chose 'exit': Goodbye!"
