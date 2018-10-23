import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    print("say Something")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
print(type(audio))   
try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
