posttext = ""
rawtext = raw_input("Sentence to split: ")
splittext = rawtext.split(r'\n')
for sentence in splittext:
	posttext = posttext + sentence + "\n" 
print posttext.strip()
