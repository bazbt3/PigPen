# Technical

## Things to note:
* This application `PigPen.py` is being developed on a iPhone within the Pythonista app IDE, using **Python 3.5** from v0.2.5 onwards.  Due to my misunderstanding of its requirements after an early failure to run the imported PNUTpy routines I started off with Python 2.7. It's unnecessary, I'm converting this to Python 3.5.
* There's a way to go before this is as 'modular' as I'd like.
* What there is, it works - provided a valid secret token is used.
* What there is, it's a noob's *second* attempt at proper Python interacting with an API.  Please tread carefully.

## A running client's file list:
**Valid at v0.3.6 onwards.**
### The main application:
* `PigPen.py`.
### Necessary before the application will run:
* `secrettoken.txt             ` - contains the secret token.
### Created by the app when first run after installation:
* `config.ini` - a persistent settings file.

## Limitations:
* Text commands only.
* No deletions yet.
* No files support yet, that includes embedded images.
* The rest is very rough.

## Error trapping:
* Checks JSON for presence of `is_deleted` field and bypasses the post's display.
* That's it.  It's hardly error trapping is it.

## Security:
* Don't share keys or tokens, especially by accident with the code.
* No, I haven't.  I currently copy individual files between the Pythonista IDE and Working Copy git apps.

## Next steps:
See the **[Roadmap](90-roadmap.md)** for plans for future development.
