# Installing PigPen.py
Incomplete, potentially misleading instructions follow.  This is very much a work in progress.

## Prerequisites:
* A [pnut.io](https://pnut.io) account; no [developer account](https://pnut.io/dev) is required for single-user apps,
* Python. I made this using the iOS [Pythonista app](http://omz-software.com/pythonista/),
* [`StaSh`](https://gist.github.com/CodyKochmann/4d6b40e77ba862e634185a038d2c3f13), a bash-like shell for Pythonista, to give access to `pip`, which allows installation of…
* @33MHz & @thrrgilag's [`PNUTpy`](https://github.com/pnut-api/PNUTpy) library. (FYI: It's compatible with Python 2 and 3.)

## First steps:
(Assuming you're running Pythonista, {p} = a Pythonista-specific instruction.)
1. You will need a pnut.io account, and to visit your developer account page.
1. **Create an app at the page**, which will create 2 unique codes, then authorise it which will create a token.
1. **Create a new `PigPen` directory** wherever directory you intend to run the app from.
1. **Copy the `PigPen.py`, `secrettoken.txt` file from here** and save it there.
1. **Overwrite the contents of `secrettoken.txt` with the token**, ensuring to remove any trailing linefeeds before saving it.
1. {p} **Install `StaSh`** following the instructions as it runs and from the link above.
1. {p} I *think* `Stash` must be executed at this stage to install a script and extension folder; read the instructions.
1. {p} **Kill then reopen Pythonista** to properly install `Stash`, if you didn't read the instructions.
1. **Follow PNUTpy's installation instructions, and `$ pip install pnutpy`**.
1. {p} For the hell of it, **kill then re-open Pythonista.**

## Run PigPen for the first time:
Run the `PigPen.py script`; it's as simple as that!

(I have not included instructions for making the file executable by file permissions of shebangs, it's beyond the remit of this page; Pythonista doesn't require it.)

## Next steps:
To find out how to start posting, reading, starring, etc., and read about some current limitations, please read the **[Usage document.](20-usage.md)**
