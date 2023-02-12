import requests
import speech_recognition as sr
from gtts import gTTS
import pygame

bot_message = ""
message = ""
arr = []

while bot_message != "Terimakasih sudah menggunakan layanan kami. Sampai jumpa!":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Katakan sesuatu!")
        audio = r.listen(source)
        try:
            message = r.recognize_google(audio, language="id-ID")
            print("Anda berkata: {}".format(message))
        except:
            print("Maaf, tidak dapat mengenali apa yang Anda katakan")
    if len(message) == 0:
        continue
    print("Mengirim pesan sekarang...")
    response = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})
    # print("Bot mengatakan, ", end = ' ')
    for i in response.json():
        text = i['text']
        print(f"{text}")
        arr.append(text)
    for j in arr:
        bot_message += ' ' + j
    output = gTTS(text=bot_message, lang='id')
    output.save("output.mp3")
    bot_message = ""
    arr = []
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    pygame.quit()
