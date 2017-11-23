# ppmentions
# v0.0.2
# (Restarted after losing sight of the goal, both locally and in the 0.3.6dev branch.)

# An app with one goal:
# To display mutual mentions between only 2 users. (A challemge for me from @schmidt_fu for the pnut.io #Hackathon!)

# Based on PigPen v0.3.6 (not yet released at ppmentions' first release) for Python 3.5, but with unnecessary functions removed.
# PigPen is a Python app for @33MHz's pnut.io social network.
# Site, changelog: https://github.com/bazbt3/PigPen

# Made by: @bazbt3

# DOES NOTHING YET.
# Nothing useful, nothing relevant to the original intent.
# The functions other than authorisation, setup and menu are simply placeholders.


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
global action, channelid, isdeleted, maxpostlen, me, number, postcontent, postid, posttext, postthreadid, retrievecount
action = ''
channelid = 0
isdeleted = ''
maxpostlen = 256
me = ''
number = 0
postcontent = ()
postid = 0
postthreadid = 0
posttext = ''
# retrievecount = 30

# Setup continues after the function definitions.


# DEFINE FUNCTIONS:

# RETAIN
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

# RETAIN
def getme():
	"""
	Get the current user id and username from the server.
	
	Arguments:
		none
	User input:
		none
	"""
	global me
	userid = pnutpy.api.get_user("me")
	me = userid[0]["username"]

# RETAIN
def menu():
	"""
	Displays mutual mentions shared between 2 users.
	
	Arguments:
		none
	User input:
		none
	"""
	print("""
| ppmentions | pnut u:@{0}

'do it' = get those mentions!

(interactions will come later)

help=menu
set=change settings
exit=exit
""".format(str(me)))

# RETAIN
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
				the routine uses the global variable passed from the routine calling it.
	"""
	choice = 'Little Bobby Tables'
	while choice != 'exit':
		choice = input("Choice? ")
		# Add in alphabetic order to easily scan through
		if choice == 'do it':
			getmutualmentions()
		elif choice == 'help':
			menu()
		elif choice == 'set':
			changesettings()
	# The app exits here once 'exit' is typed:
	print(" ")
	print("You chose 'exit': Goodbye!")


# DEFINE FUNCTIONS WITH SINGLE RESULTS FOR THE USER:

# THIS IS NEW!!!2!¡
def getmutualmentions():
	print("""
Is it done yet?

No. I need to ask for the user id to compare with and, er… other stuff first! Shhh…
""")

# REPURPOSE
# Use the core 'alsomentions' and subsequent poster ids to check for matches within the list
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

# RETAIN
# Until the new thing is built
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
	

# DEFINE INTERACTIONS WITH MULTIPLE RESULTS:

# MODIFY
# Or retain until the new thing is built
def getmentions():
	"""
	Get the application user's mentions.
	
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

# RETAIN
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


# DEFINE OTHER ROUTINES:

# RETAIN
def changesettings():
	"""
	Changes global settings.
	
	Arguments:
		none
	User input:
		The setting to change:
			retrievecount = the number of posts fetched from the server. No input validation.
	"""
	print(" " + "-" * 31 + " ")
	choice = input("""| settings |
rc change retrieved post count?
[return] = exit
""")
	if choice == "rc":
		global retrievecount
		try:
			dummyvalue = retrievecount
		except:
			retrievecount = 30
		print("retrievecount =", retrievecount, "now")
		rcount = input("Please change, to (>0)? ")
		if int(rcount) > 0:
			retrievecount = int(rcount)
			print("now", retrievecount, "posts")
			# Save to "ppm.ini" file:
			config["USER"]["retrievecount"] = str(retrievecount)
			with open ("ppm.ini", "w") as configfile:
				config.write(configfile)
	print(" " + "-" * 31 + " ")
	print("")

# RETAIN
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

# RETAIN
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

# RETAIN
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

# RETAIN
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

# RETAIN
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
		print("ok")
	elif status == 201:
		print("ok")
	else:
		print(str(status) + " = hmmm...")

# MAIN ROUTINE:

# RETAIN
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

# RETAIN
# Load defaults and any previous user-applied changes from "ppm.ini", initially only 'defaultretrievecount' and 'retrievecount':
try:
	config = configparser.ConfigParser()
	config.read("ppm.ini")
	retrievecount = int(config["USER"]["retrievecount"])
except:
	config = configparser.ConfigParser()
	config["USER"] = {}
	config["USER"]["retrievecount"] = "30"
	print("""
| ppmentions | Initialisation:
(You'll see this only once.)
Please decide on a default number of posts to retrieve - then choose the 'rc' option on the following menu.""")
	changesettings()
	print("Thanks.")

# STOP FIDDLING WITH STUFF, DO IT!
main()
