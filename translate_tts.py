from gtts import gTTS
from googletrans import Translator
import os

def transnsay(text,lang):
    translator = Translator()
    translation = translator.translate(text, dest=lang)
    #return translation.pronunciation

    myobj = gTTS(text=translation.pronunciation, lang='en', slow=False)
    myobj.save("tts.mp3")
    os.system("play tts.mp3")
    os.system('echo stars | sudo -S rm tts.mp3')

#transnsay("hello world",'ta')
