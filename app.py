import speech_recognition as sr
import keyboard

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Скажи, что надо ввести:')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='ru-RU')
        print(text)
        keyboard.write(f' {text} ')
    except:
        print('Я вас не понял')