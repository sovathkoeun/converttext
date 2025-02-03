from gtts import gTTS
import os

text = open("data.txt", "r").read()


language = 'en'
slow = False
tts = gTTS(text=text, lang=language, slow=slow)
tts.save("output.mp3")

os.system("output.mp3")