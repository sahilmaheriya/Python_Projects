from gtts import gTTS

# you can read text

text = "hello! my name is sahil maheriya"

# and you can also read file

f = open('random.txt', 'r')

text = f.read()

language = "en"

obj = gTTS(text = text, lang = language, slow = False)

obj.save("sample.mp3")
