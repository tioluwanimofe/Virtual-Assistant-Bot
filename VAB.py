# Description: This is a virtual assistant program that gets the date, current time, responds back with a random
# greeting , and returns information on a person.

# pip install pyaudio
# pip install SpeechRecognition
# pip install gTTs(google text to speed) package
# pip install wikipedia
# pip install Google Maps
# pip install tracker
# Import the libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

# import googlesearch
# import tracker

# Ignore any warning messages
warnings.filterwarnings('ignore')

# Record audio and return it as a string
# Record the audio.
r = sr.Recognizer()  # Creating a recognizer object

# Open the microphone and start recording
with sr.Microphone() as source:
    print('Say something pls!!!')
    audio = r.listen(source)

# Use Google's speech recognition
data = ''
try:
    data = r.recognize_google(audio)
    words = ['this is a boy', 'okay vab', 'vab']
    # A list of wake words
    # Check to see if the users command/text contains a wakeWord/phrase
    Opemipo = data.split()
    f = "Yes master, I heard your wake-word"
    mofe = 'You said: ' + data
    if words in Opemipo:
        my_obj = gTTS(text=f, lang='en', slow=False)
        # Save the converted audio to a file
        my_obj.save('assistant_response.mp3')

        # Play the converted file
        os.system('start assistant_response.mp3')

        # A function to get the virtual assistant response orally and not written/texted.
        # Convert the text to speech.
    else:
        my_obj = gTTS(text=mofe, lang='en', slow=False)

        # Save the converted audio to a file
        my_obj.save('assistant_response.mp3')

        # Play the converted file
        os.system('start assistant_response.mp3')

        print(mofe)


    # A function to get the current date.
    def getDate():
        now = datetime.datetime.now()
        my_date = datetime.datetime.today()
        weekday = calendar.day_name[my_date.weekday()]  # e.g. Friday.
        monthNum = now.month
        dayNum = now.dayx
        # Record the audio
        text = recordAudio()
        response = ''

        # Check for the wake word/phrase


    if wakeWord(text):

        # Check for greetings by the user
        response = response + greeting(text)

        # Check to see if the user said anything having to do with date
        if 'date' in text:
            getDate()
            response = response + ' ' + get_date + '.'

            # Check to see if the user said anything having to do with the time
        if 'time' in text:
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour >= 12:
                meridiem = 'p.m'  # Post meridiem (PM) after mid-day
                hour = now.hour - 12
            else:
                meridiem = 'a.m'  # Ante-Meridiem(AM) before mid-day
                hour = now.hour

                # Convert minute into a proper string.
            if now.minute < 10:
                minute = '0' + str(now.minute)
            else:
                minute = str(now.minute)

                response = response + ' ' + 'It is  ' + str(hour) + ':' + minute + ' ' + meridiem + '.'
            # Check to see if the user said 'who is'.
        if 'who is' in text:
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki


except sr.UnknownValueError:
    # Check for unknown errors
    print('I do not understand what you said. Please repeat your words slowly again')
except sr.RequestError as e:
    b = str(e)
    print('Request results from Google Speech Recognition service error: ' + b)
