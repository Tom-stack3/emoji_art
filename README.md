# emoji_art
A python program to generate Emoji art. The art is generated in a fixed width of 10 emojis, in order to be compatible with WhatsApp Messages.

**Functionalities:**
1. Transform an Image into Emoji art.
2. Transform simple text into Emoji art (customizable colors).
3. Draw Among-us character in Emoji art (customizable colors).

## Examples:
### 1 - Image to Emoji art
```python
drawing = Drawing()
drawing.translate_image("image/src/here.cool", True)
# The second parameter is to decide whether the NEAREST filter is applied (applied by default).
# (See examples in the "NEAREST filter" section)
```
| Input Image  | Result | Source|
| ------------- | ------------- | ------------- |
| <img src="./examples/cuba.jpg" width="225"> |❤️💙💙💙💙💙💙💙💙💙<br>❤️❤️❤️🤍🤍🤍🤍🤍🤍🤍<br>❤️🤍❤️❤️💙💙💙💙💙💙<br>❤️❤️❤️🤍🤍🤍🤍🤍🤍🤍<br>❤️💙💙💙💙💙💙💙💙💙 | Flag of Cuba |
| <img src="./examples/guinea.png" width="225"> |❤️❤️❤️💛💛💛💛💚💚💚<br>❤️❤️❤️💛💛💛💛💚💚💚<br>❤️❤️❤️💛💛💛💛💚💚💚<br>❤️❤️❤️💛💛💛💛💚💚💚<br>❤️❤️❤️💛💛💛💛💚💚💚<br>❤️❤️❤️💛💛💛💛💚💚💚<br>❤️❤️❤️💛💛💛💛💚💚💚| Flag of Guinea |
| <img src="./examples/tanzania.png" width="225"> |💚💚💚💚💚💚💚💛🖤🖤<br>💚💚💚💚💚💛🖤🖤🖤💛<br>💚💚💚💚💛🖤🖤🖤💛💙<br>💚💚💚🖤🖤🖤🖤💙💙💙<br>💚💛🖤🖤🖤💛💙💙💙💙<br>💛🖤🖤🖤💛💙💙💙💙💙<br>🖤🖤💛💙💙💙💙💙💙💙| Flag of Tanzania |
| <img src="./examples/discord.jpg" width="225">|💜💜💜💜💜💜💜💜💜💜<br>💜💜💜💜💜💜💜💜💜💜<br>💜💜💜🤍💜💜🤍💜💜💜<br>💜💜🤍🤍🤍🤍🤍🤍💜💜<br>💜💜🤍🤍🤍🤍🤍🤍🤍💜<br>💜🤍🤍💜🤍💜💜🤍🤍💜<br>💜🤍🤍🤍🤍🤍🤍🤍🤍💜<br>💜💜🤍💜💜💜💜🤍💜💜<br>💜💜💜💜💜💜💜💜💜💜<br>💜💜💜💜💜💜💜💜💜💜|Discord's logo|

### 2 - Text to Emoji art
```python
drawing = Drawing()
drawing.add_text("Some Text", "<main_color>", "<background_color>")
```


`drawing.add_text("Hi", "blue", "pink")`

💗💗💗💗💗💗💗💗💗💗\
💗💗💙💗💗💗💗💙💗💗\
💗💗💙💗💗💗💗💙💗💗\
💗💗💙💗💗💗💗💙💗💗\
💗💗💙💙💙💙💙💙💗💗\
💗💗💙💗💗💗💗💙💗💗\
💗💗💙💗💗💗💗💙💗💗\
💗💗💙💗💗💗💗💙💗💗\
💗💗💙💗💗💗💗💙💗💗\
💗💗💗💗💗💗💗💗💗💗\
💗💗💗💗💙💗💗💗💗💗\
💗💗💗💗💗💗💗💗💗💗\
💗💗💗💗💙💗💗💗💗💗\
💗💗💗💗💙💗💗💗💗💗\
💗💗💗💗💙💗💗💗💗💗\
💗💗💗💗💙💗💗💗💗💗\
💗💗💗💗💙💗💗💗💗💗\
💗💗💗💗💗💗💗💗💗💗


### 3 - Among-us character
```python
drawing = Drawing()
drawing.draw_amogus("<body_color>", "<background_color>")
```

`drawing.draw_amogus("pink", "green")`

💚💚💚💚💚💚💚💚💚💚\
💚💚💚💚💗💗💗💗💚💚\
💚💚💚💗💗💗💗💗💗💚\
💚💚💚💗💗💙💙💙💙💚\
💚💗💗💗💗💙💙💙💙💚\
💚💗💗💗💗💙💙💙💙💚\
💚💗💗💗💗💗💗💗💗💚\
💚💗💗💗💗💗💗💗💗💚\
💚💗💗💗💗💗💗💗💗💚\
💚💚💚💗💗💗💗💗💗💚\
💚💚💚💗💗💚💗💗💚💚\
💚💚💚💗💗💚💗💗💚💚\
💚💚💚💚💚💚💚💚💚💚


### NEAREST filter:
| Without the NEAREST filter  | With the NEAREST filer | Logo|
| ------------- | ------------- | ------------- |
|🤍🤍🤍🤍🤍💗🤍🤍🤍🤍<br>🤍🤍💗❤️❤️❤️❤️💗🤍🤍<br>🤍💗❤️❤️❤️💗❤️💗🤍🤍<br>🤍❤️❤️🤍🤍🤍🤍🤍🤍🤍<br>💛🧡💗🤍🤍🤍🤍🤍🤍🤍<br>💛🧡🤍🤍🤍💙💙💙💙💜<br>💛🧡🤍🤍🤍🤍🤍💜💙💜<br>🤍💚💚🤍🤍🤍🤍💙💙🤍<br>🤍💜💚💚💙💜💚💙💜🤍<br>🤍🤍💜💚💚💚💚💙🤍🤍<br>🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍  | 🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍<br>🤍🤍💗❤️❤️❤️❤️❤️🤍🤍<br>🤍❤️❤️❤️❤️❤️❤️❤️🤍🤍<br>🤍❤️❤️🤍🤍🤍🤍🤍🤍🤍<br>🤍🧡❤️🤍🤍🤍🤍🤍🤍🤍<br>🧡🧡🤍🤍🤍💙💙💙💙💙<br>🤍🧡💜🤍🤍🤍🤍🤍💙🤍<br>🤍💚💚🤍🤍🤍🤍💙💙🤍<br>🤍💚💚💚💚💚💚💙💙🤍<br>🤍🤍💚💚💚💚💚💚🤍🤍<br>🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍|[Google's favicon](./examples/google_logo.png)|
|🤍🤍💜🤎🖤🖤🤎💜🤍🤍<br>🤍🤎🖤🖤🖤🖤🖤🖤🤎🤍<br>💜🖤💜💜💜💜💜💜🖤💜<br>🖤🖤🤍🤍🤍🤍🤍🤍🖤🤎<br>🖤🖤🤍🤍🤍🤍🤍🤍🖤🖤<br>🖤🖤🤍🤍🤍🤍🤍🤍🖤🖤<br>🖤🖤💜🤍🤍🤍🤍💜🖤🤎<br>💜🤎🤎🤎🤍🤍🤎🖤🖤💜<br>🤍🤎🤎💜🤍🤍🤎🖤🤎🤍<br>🤍🤍💜💜🤍🤍💜💜🤍🤍|🤍🤍🤍🖤🖤🖤🖤🤍🤍🤍<br>🤍🖤🖤🖤🖤🖤🖤🖤🖤🤍<br>🤍🖤🤍🤍🤍🤍🤍🤍🖤🤍<br>🖤🖤🤍🤍🤍🤍🤍🤍🖤🖤<br>🖤🖤🤍🤍🤍🤍🤍🤍🖤🖤<br>🖤🖤🤍🤍🤍🤍🤍🤍🖤🖤<br>🖤🖤🤍🤍🤍🤍🤍🤍🖤🖤<br>🤍🖤🖤🖤🤍🤍🖤🖤🖤🤍<br>🤍🖤🖤🤍🤍🤍🖤🖤🖤🤍<br>🤍🤍🤍🖤🤍🤍🖤🤍🤍🤍|[GitHub mark logo](./examples/github_logo.png)|
|🤍🤍💗❤️❤️❤️❤️💗🤍🤍<br>🤍💗❤️❤️❤️❤️❤️❤️💗🤍<br>🤍🤎❤️❤️❤️❤️❤️❤️❤️🤍<br>💙🤎🤎💗💜💜💗🧡💛💛<br>💚💚🤎💜💙💙💜💛💛💛<br>💚💚🤎💜💙💙💜💛💛💛<br>💙💚💚💙💜💙🤍💛💛💛<br>🤍💚💚💚💙💙💛💛💛🤍<br>🤍💙💚💚💚💚💛💛🤍🤍<br>🤍🤍🤍💙💚💛💛🤍🤍🤍 | 🤍🤍🤍❤️❤️❤️❤️🤍🤍🤍<br>🤍🤎❤️❤️❤️❤️❤️❤️❤️🤍<br>🤍🤎❤️❤️❤️❤️❤️❤️❤️🤍<br>💚🤎🤎🤍💙💙🤍💛💛💛<br>💚💚🤎💙💙💙💙💛💛💛<br>💚💚💚💙💙💙💙💛💛💛<br>💚💚💚🤍💙💙🤍💛💛💛<br>🤍💚💚💚💚💚💛💛💛🤍<br>🤍💚💚💚💚💚💛💛💛🤍<br>🤍🤍🤍💚💚💛💛🤍🤍🤍|[Google Chrome icon](./examples/chrome_logo.png)|

