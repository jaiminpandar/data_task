from gtts import gTTS
from io import BytesIO
import speech_recognition

a=gTTS('Hy JAIMIN I love You')
a.save('ronu.mp3')
b = gTTS('Nowdays i miss you so much ronak when will you come dear', lang='en',slow=False)
b.save('sonu.mp3')

file = open("sonu.txt", "r").read().replace("\n", " ")
speech = gTTS(text = str(file),lang='en',slow = False)
speech.save("reader.mp3")


#Task Day 3 using random paswrd generate and library gtts for voice recognize and all
#matplotlib use
#NLP NLU AND NLG information tokenization lemmetization etc