from gtts import gTTS
import os

text = "Hello, World!"
tts = gTTS(text=text, lang='en', slow=False)
tts.save("hello.mp3")

os.system("start hello.mp3")