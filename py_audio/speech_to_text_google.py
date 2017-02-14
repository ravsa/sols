import speech_recognition

speech = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    audio = speech.listen(source)
print speech.recognize_google(audio)
