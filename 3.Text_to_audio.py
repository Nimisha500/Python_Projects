from gtts  import gTTS
from playsound import playsound

audio='speech.mp3'
audio1='speech1.mp3'
language = 'en'
sp = gTTS(text ="Artificial intelligence (AI) is intelligence demonstrated by machines, unlike the natural intelligence displayed by humans and animals, which involves consciousness and emotionality.",lang = language, slow = False)
sp1= gTTS(text="Hallo,Ich bin gut",lang='de',slow=False)

sp.save(audio)
playsound(audio)

sp1.save(audio1)
playsound(audio1)


