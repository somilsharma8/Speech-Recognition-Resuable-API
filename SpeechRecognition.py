# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import speech_recognition as sr
import pyttsx3
from flask import Flask, request, make_response
from flask_restful import Resource, Api
import os

cf_port = os.getenv("PORT")
app = Flask(__name__)
api = Api(app)

r = sr.Recognizer()

def SpeakText(command):

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    print(voices)
    engine.setProperty('voice', voices[2].id)

    engine.say(command)
    engine.runAndWait()

@app.route('/activateSpeechRecognition', methods=["GET"])
def runner():

    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2)

            audio2 = r.listen(source2)

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            #print('Did you say ' + MyText)
            print(MyText)
            words = MyText.split()
            print("Here's the second word: " + words[1])
            #SpeakText(MyText)

            if (MyText != None):
                return make_response('Speech recognised and broken into words', 200, {'words': words})

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")

    #return make_response('Speech recognised and broken into words', 200, {'words': 'attach words here'})
    return make_response('Nothing has been said', 200)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if cf_port is None:
        app.run(host='0.0.0.0', port='8885')
    else:
        app.run(host='0.0.0.0', port=int(cf_port))
