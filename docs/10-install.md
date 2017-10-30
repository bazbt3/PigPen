# Installing PigPen.py
Incomplete, potentially misleading instructions follow.  This is very much a work in progress.

## Prerequisites:
* A [pnut.io](https://pnut.io) account; no [developer account](https://pnut.io/dev) is required for single-user apps,
* Python 2, I made this using the iOS [Pythonista app](http://omz-software.com/pythonista/),
* [`StaSh`](https://gist.github.com/CodyKochmann/4d6b40e77ba862e634185a038d2c3f13), a bash-like shell for Pythonista, to give `pip`, which allows installation of…
* @thrrgilag's [`PNUTpy`](https://github.com/pnut-api/PNUTpy) library. (FYI: It's Python 2, I'm wondering about forking it and converting to Python 3.)

## First steps:
1. Copy the `PigPen.py` and `secrettoken.txt files from here and save in whichever directory you intend to run the app from.
1. You will need a pnut.io account, and to visit [developer account](https://pnut.io/dev).
1. Create an app at the page, which will create 2 unique codes, then authorise it which will create a token.
1. Overwrite the contents of `secrettoken.txt` with the token, ensuring to remove any trailing linefeeds before saving it.

## Run PigPen for the first time:
(I have not included instructions for making the file executable by file permissions of shebangs, it's beyond the remit of this page; Pythonista doesn't require it.)

[instructions to follow]

## Next steps:
To find out how to start posting, blogging, and read about some current limitations, please read the **[Usage document.](/docs/20-usage.md)**
