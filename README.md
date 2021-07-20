# whatsapp_art
A python program to generate Emoji art. The art is generated in a fixed width of 10 emojis, in order to be compatible with Whatsapp Messages.

## Functionalities:
1. Transform an Image into Emoji art.
2. Transform simple text into Emoji art (customizable colors).
3. Draw Among-us character in Emoji art (customizable colors).

## Examples:
(1 - Image to Emoji art)

| Input Image  | Result | Source|
| ------------- | ------------- | ------------- |
| <img src="./examples/cuba.jpg" width="225"> |❤️💙💙💙💙💙💙💙💙💙<br>❤️❤️❤️🤍🤍🤍🤍🤍🤍🤍<br>❤️🤍❤️❤️💙💙💙💙💙💙<br>❤️❤️❤️🤍🤍🤍🤍🤍🤍🤍<br>❤️💙💙💙💙💙💙💙💙💙 | Flag of Cuba |
| <img src="./examples/guinea.png" width="225"> |❤️❤️❤️💛💛💛💛💚💚💚<br>❤️❤️❤️💛💛💛💛💚💚💚<br>❤️❤️❤️💛💛💛💛💚💚💚<br>❤️❤️❤️💛💛💛💛💚💚💚<br>❤️❤️❤️💛💛💛💛💚💚💚<br>❤️❤️❤️💛💛💛💛💚💚💚<br>❤️❤️❤️💛💛💛💛💚💚💚| Flag of Guinea |
| <img src="./examples/tanzania.png" width="225"> |💚💚💚💚💚💚💚💛🖤🖤<br>💚💚💚💚💚💛🖤🖤🖤💛<br>💚💚💚💚💛🖤🖤🖤💛💙<br>💚💚💚🖤🖤🖤🖤💙💙💙<br>💚💛🖤🖤🖤💛💙💙💙💙<br>💛🖤🖤🖤💛💙💙💙💙💙<br>🖤🖤💛💙💙💙💙💙💙💙| Flag of Tanzania |
| <img src="./examples/discord.jpg" width="225">|💜💜💜💜💜💜💜💜💜💜<br>💜💜💜💜💜💜💜💜💜💜<br>💜💜💜🤍💜💜🤍💜💜💜<br>💜💜🤍🤍🤍🤍🤍🤍💜💜<br>💜💜🤍🤍🤍🤍🤍🤍🤍💜<br>💜🤍🤍💜🤍💜💜🤍🤍💜<br>💜🤍🤍🤍🤍🤍🤍🤍🤍💜<br>💜💜🤍💜💜💜💜🤍💜💜<br>💜💜💜💜💜💜💜💜💜💜<br>💜💜💜💜💜💜💜💜💜💜|Discord's logo|
| <img src="./examples/chrome_logo.png" width="225">| 🤍🤍🤍❤️❤️❤️❤️🤍🤍🤍<br>🤍🤎❤️❤️❤️❤️❤️❤️❤️🤍<br>🤍🤎❤️❤️❤️❤️❤️❤️❤️🤍<br>💚❤️🤎🤍💙💙🤍💛💛💛<br>💚💚🤎💙💙💙💙💛💛💛<br>💚💚💚💙💙💙💙💛💛💛<br>💚💚💚🤍💙💙🤍💛💛💛<br>🤍💚💚💚💚💚💛💛💛🤍<br>🤍💚💚💚💚💚💛💛💛🤍<br>🤍🤍🤍💚💚💛💛🤍🤍🤍<br>| Google Chrome icon|







### the NEAREST filter:
| without the NEAREST filter  | with the NEAREST filer | Logo|
| ------------- | ------------- | ------------- |
|🤍🤍🤍🤍🤍💗🤍🤍🤍🤍<br>🤍🤍💗❤️❤️❤️❤️💗🤍🤍<br>🤍💗❤️❤️❤️💗❤️💗🤍🤍<br>🤍❤️❤️🤍🤍🤍🤍🤍🤍🤍<br>💛🧡💗🤍🤍🤍🤍🤍🤍🤍<br>💛🧡🤍🤍🤍💙💙💙💙💜<br>💛🧡🤍🤍🤍🤍🤍💜💙💜<br>🤍💚💚🤍🤍🤍🤍💙💙🤍<br>🤍💜💚💚💙💜💚💙💜🤍<br>🤍🤍💜💚💚💚💚💙🤍🤍<br>🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍  | 🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍<br>🤍🤍💗❤️❤️❤️❤️❤️🤍🤍<br>🤍❤️❤️❤️❤️❤️❤️❤️🤍🤍<br>🤍❤️❤️🤍🤍🤍🤍🤍🤍🤍<br>🤍🧡❤️🤍🤍🤍🤍🤍🤍🤍<br>🧡🧡🤍🤍🤍💙💙💙💙💙<br>🤍🧡💜🤍🤍🤍🤍🤍💙🤍<br>🤍💚💚🤍🤍🤍🤍💙💙🤍<br>🤍💚💚💚💚💚💚💙💙🤍<br>🤍🤍💚💚💚💚💚💚🤍🤍<br>🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍|[Google's favicon](./examples/google_logo.png)|
|🤍🤍💜🤎🖤🖤🤎💜🤍🤍<br>🤍🤎🖤🖤🖤🖤🖤🖤🤎🤍<br>💜🖤💜💜💜💜💜💜🖤💜<br>🖤🖤🤍🤍🤍🤍🤍🤍🖤🤎<br>🖤🖤🤍🤍🤍🤍🤍🤍🖤🖤<br>🖤🖤🤍🤍🤍🤍🤍🤍🖤🖤<br>🖤🖤💜🤍🤍🤍🤍💜🖤🤎<br>💜🤎🤎🤎🤍🤍🤎🖤🖤💜<br>🤍🤎🤎💜🤍🤍🤎🖤🤎🤍<br>🤍🤍💜💜🤍🤍💜💜🤍🤍|🤍🤍🤍🖤🖤🖤🖤🤍🤍🤍<br>🤍🖤🖤🖤🖤🖤🖤🖤🖤🤍<br>🤍🖤🤍🤍🤍🤍🤍🤍🖤🤍<br>🖤🖤🤍🤍🤍🤍🤍🤍🖤🖤<br>🖤🖤🤍🤍🤍🤍🤍🤍🖤🖤<br>🖤🖤🤍🤍🤍🤍🤍🤍🖤🖤<br>🖤🖤🤍🤍🤍🤍🤍🤍🖤🖤<br>🤍🖤🖤🖤🤍🤍🖤🖤🖤🤍<br>🤍🖤🖤🤍🤍🤍🖤🖤🖤🤍<br>🤍🤍🤍🖤🤍🤍🖤🤍🤍🤍|[GitHub mark logo](./examples/github_logo.png)|
|🤍🤍💗❤️❤️❤️❤️💗🤍🤍<br>🤍💗❤️❤️❤️❤️❤️❤️💗🤍<br>🤍🤎❤️❤️❤️❤️❤️❤️❤️🤍<br>💙🤎🤎💗💜💜💗🧡💛💛<br>💚💚🤎💜💙💙💜💛💛💛<br>💚💚🤎💜💙💙💜💛💛💛<br>💙💚💚💙💜💙🤍💛💛💛<br>🤍💚💚💚💙💙💛💛💛🤍<br>🤍💙💚💚💚💚💛💛🤍🤍<br>🤍🤍🤍💙💚💛💛🤍🤍🤍 | 🤍🤍🤍❤️❤️❤️❤️🤍🤍🤍<br>🤍🤎❤️❤️❤️❤️❤️❤️❤️🤍<br>🤍🤎❤️❤️❤️❤️❤️❤️❤️🤍<br>💚🤎🤎🤍💙💙🤍💛💛💛<br>💚💚🤎💙💙💙💙💛💛💛<br>💚💚💚💙💙💙💙💛💛💛<br>💚💚💚🤍💙💙🤍💛💛💛<br>🤍💚💚💚💚💚💛💛💛🤍<br>🤍💚💚💚💚💚💛💛💛🤍<br>🤍🤍🤍💚💚💛💛🤍🤍🤍|[Google Chrome icon](./examples/chrome_logo.png)|

