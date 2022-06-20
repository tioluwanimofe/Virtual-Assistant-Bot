"""Description: This is a virtual assistant program that gets the date, current time, responds back with a random
 greeting , and returns information on a person."""

import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import requests

month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December']

ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                  '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th',
                  '25th', '26th', '27th', '28th', '29th', '30th', '31st']  # A list of ordinal numbers

GREETING_INPUTS = ['hi', 'hey there!!', 'hola', 'greetings', 'was sup', 'hello', 'sup', 'morning', 'afternoon']

GREETING_RESPONSES = ['Howdy', 'Hi, I am VAB', 'Hello', 'Greetings to you to', 'I am good', 'Sup',
                      'Good morning to you to', 'Good afternoon to you to', ]  # Greeting responses.

data = ''
try:
    # while True:
    warnings.filterwarnings('ignore')  # Ignore any warning messages
    r = sr.Recognizer()  # Creating a recognizer object
    with sr.Microphone() as source:  # Open the microphone and start recording
        print('Say something pls!!!')
        audio = r.listen(source)

    ''' A function to get the virtual assistant response orally and not written/texted.'''
    data = r.recognize_google(audio)  # Use Google's speech recognition
    Opemipo = data.split()
    mofe = 'You said: ' + data
    wakeWord = ['hello', 'boy']  # A list of wake words
    Supreme = ['mofe', 'muffin']

    def getDate():  # A function to get the current date.
        present = datetime.datetime.now()
        my_date = datetime.datetime.today()
        weekday = calendar.day_name[my_date.weekday()]  # e.g. Friday.
        monthNum = present.month
        dayNum = present.day
        i = 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' ' + 'the' + ' ' + ordinalNumbers[dayNum - 1] + \
            '. '
        your_date = gTTS(text=i, lang='en', slow=False)  # Convert the text to speech.
        your_date.save('assistant_date.mp3')  # Save the converted audio to a file
        os.system('start assistant_date.mp3')  # Play the converted file
        print(mofe)
        print("I said: " + i)


    def greeting():  # A function to return a random greeting response
        # Check if the user's input is a greeting, return a randomly chosen to greet response
        k = random.choice(GREETING_RESPONSES) + '.'
        your_greeting = gTTS(text=k, lang='en', slow=False)  # Convert the text to speech.
        your_greeting.save('assistant_greeting.mp3')  # Save the converted audio to a file
        os.system('start assistant_greeting.mp3')  # Play the converted file
        print(mofe)
        print("I said: " + k)


    def getPerson():  # A function to get a persons first and last name from the text
        for i in range(0, len(wordList)):
            if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList(i + 1).lower() == 'is':
                return wordList[i + 2] + ' ' + wordList[i + 3]


    if any(Adesanya in Opemipo for Adesanya in wakeWord):
        my_obj = gTTS(text="Yes master, I heard your wake-word", lang='en', slow=False)  # Convert the text to speech.
        my_obj.save('assistant_response.mp3')  # Save the converted audio to a file
        os.system('start assistant_response.mp3')  # Play the converted file
        teni = 'You said: ' + data
        print(teni)
        print("I said: Yes master, I heard your wake-word")

        r = sr.Recognizer()  # Creating a recognizer object
        with sr.Microphone() as source:  # Open the microphone and start recording
            print('Say something pls!!!')
            audio = r.listen(source)
        data = r.recognize_google(audio)
        Opemipo = data.split()
        # Check for greetings by the user
        while True:
            if 'date' in Opemipo:  # Check to see if the user said anything having to do with date
                getDate()
                break

            if any(Adesanya in Opemipo for Adesanya in GREETING_INPUTS):
                greeting()
                break

            if 'time' in Opemipo:  # Check to see if the user said anything having to do with the time
                meridiem = ''
                now = datetime.datetime.now()
                if now.hour >= 12:
                    meridiem = 'p.m'  # Post meridiem (PM) after mid-day
                    hour = now.hour - 12
                else:
                    meridiem = 'a.m'  # Ante-Meridiem(AM) before mid-day
                    hour = now.hour

                if now.minute < 10:
                    minute = '0' + str(now.minute)  # Convert minute into a proper string.
                else:
                    minute = str(now.minute)
                t = 'It is  ' + str(hour) + ':' + minute + ' ' + meridiem + '.'
                your_time = gTTS(text=t, lang='en', slow=False)  # Convert the text to speech.
                your_time.save('assistant_time.mp3')  # Save the converted audio to a file
                os.system('start assistant_time.mp3')  # Play the converted file
                print(mofe)
                print("I said: " + t)
                break

            if 'who is' in Opemipo:  # Check to see if the user said 'who is'.
                person = getPerson()
                wiki = wikipedia.summary(person, sentences=2)
                your_person = gTTS(text=wiki, lang='en', slow=False)  # Convert the text to speech.
                your_person.save('assistant_person.mp3')  # Save the converted audio to a file
                os.system('start assistant_person.mp3')  # Play the converted file
                print(mofe)
                print("I said: " + wiki)
                break

    elif any(Adesanya in Opemipo for Adesanya in Supreme):
        Tio = 'Yes Supreme Master, you called the Supreme wake-word, " Adesanya Tioluwanimofe".'
        my_obj = gTTS(text=Tio, lang='en', slow=False)  # Convert the text to speech.
        my_obj.save('assistant_response.mp3')  # Save the converted audio to a file
        os.system('start assistant_response.mp3')  # Play the converted file
        teni = 'You said: ' + data
        print(teni)
        print("I said: Yes Supreme Master, I heard your wake-word")
        r = sr.Recognizer()  # Creating a recognizer object
        with sr.Microphone() as source:  # Open the microphone and start recording
            print('Say something pls!!!')
            audio = r.listen(source)
        data = r.recognize_google(audio)
        Opemipo = data.split()
        # Check for greetings by the user
        while True:
            if 'date' in Opemipo:  # Check to see if the user said anything having to do with date
                getDate()
                break

            if any(Adesanya in Opemipo for Adesanya in GREETING_INPUTS):
                greeting()
                break

            if 'time' in Opemipo:  # Check to see if the user said anything having to do with the time
                meridiem = ''
                now = datetime.datetime.now()
                if now.hour >= 12:
                    meridiem = 'p.m'  # Post meridiem (PM) after mid-day
                    hour = now.hour - 12
                else:
                    meridiem = 'a.m'  # Ante-Meridiem(AM) before mid-day
                    hour = now.hour

                if now.minute < 10:
                    minute = '0' + str(now.minute)  # Convert minute into a proper string.
                else:
                    minute = str(now.minute)
                t = 'It is  ' + str(hour) + ':' + minute + ' ' + meridiem + '.'
                your_time = gTTS(text=t, lang='en', slow=False)  # Convert the text to speech.
                your_time.save('assistant_time.mp3')  # Save the converted audio to a file
                os.system('start assistant_time.mp3')  # Play the converted file
                print(mofe)
                print("I said: " + t)
                break

            if 'who is' in Opemipo:  # Check to see if the user said 'who is'.
                person = getPerson()
                wiki = wikipedia.summary(person, sentences=2)
                your_person = gTTS(text=wiki, lang='en', slow=False)  # Convert the text to speech.
                your_person.save('assistant_person.mp3')  # Save the converted audio to a file
                os.system('start assistant_person.mp3')  # Play the converted file
                print(mofe)
                print("I said: " + wiki)
                break

    else:
        my_obj = gTTS(text='To access my features, you need to say a wake word', lang='en', slow=False)  # Convert the
        # text to speech.
        my_obj.save('assistant_response.mp3')  # Save the converted audio to a file
        os.system('start assistant_response.mp3')  # Play the converted file
        print(mofe)
        print(g)


except sr.UnknownValueError:  # Check for unknown errors
    print('I do not understand what you said. Please repeat your words slowly again')
except sr.RequestError as e:
    b = str(e)
    print('Request results from Google Speech Recognition service error: ' + b)
