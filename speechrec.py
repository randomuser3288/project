import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print("Adjusting for ambient noise, please wait...")
    recognizer.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = recognizer.listen(source)

try:
    print("You said: " + recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
