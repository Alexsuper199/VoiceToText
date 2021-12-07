import speech_recognition as sr
import keyboard

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Tell me what to enter:')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(text)
        keyboard.write(f' {text} ')
    except:
        print(I did not understand you')
