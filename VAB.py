# Description: This is a virtual assistant program that gets the date, current time, responds back with a random greeting
#               , and returns information on a person.

# pip install pyaudio
# pip install SpeechRecognition
# pip install gTTs(google text to speed) package
# pip install wikipedia
# pip install google maps
# pip install tracker
#Import the libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import googlesearch
#import tracker

# Ignore any warning messages
warnings.filterwarnings('ignore')

# Record audio and return it as a string
def recordAudio():

    #Record the audio.
    r = sr.Recognizer() #Creating a recognizer object

    #Open the microphone and start recording
    with sr.Microphone() as source:
       print('Say something pls!!!')
       audio = r.listen(source)
 
    #Use Googles speech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' +data)
    except sr.UnknownValueError: # check for unknown errors
        print('I do not understand what you said. Please repeat your words slowly again')
    except sr.RequestError as e:
        print('Request results from Google speech Recognition service error ' + e)

    return data

# A function to get the virtual assistant response orally and not written/texted.

def assistantResponse(text):

    print(text)

    #convert the text to speech.
    myobj = gTTS(text= text, lang='en', slow=False)

    #Save the converted audio to a file
    myobj.save('assistant_response.mp3')

    #Play the converted file
    os.system('start assistant_response.mp3')
# A function for wake words or phrases
def wakeWord(text):
      WAKE_WORDS = ['hey vab', 'mofe is the greatest', 'mofe', 'okay vab', 'vab']
      #A list of wake words

      text = text.lower() #Converting the text to all lower case words
      #Check to see if the users command/text contains a wakeWord/phrase
      for phrase in WAKE_WORDS:
          if phrase in text:
              return True

      # If the wakeWord isn't found in the text from the loop
      return False

# A function to get the current date.
def getDate():

    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()] # e.g. Friday.
    monthNum = now.month
    dayNum = now.day

    # A lists of months
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    #A list of ordinal numbers
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st' ]
    return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + 'the' + ordinalNumbers[dayNum - 1] + ' . '

# A function to return a random greeting response
def greeting(text):
    #Greeting inputs
    GREETING_INPUTS = ['hi', 'hey there!!', 'hola', 'greetings', 'wassup', 'hello', 'sup', 'morning', 'afternoon' ]

    #Greeting responses.
    GREETING_RESPONSES = ['Howdy', 'Hi, I am VAB', 'Hello','Greetings to you to', 'I am good', 'Sup', 'Good morning to you to', 'Good afternoon to you to', ]
    #Check if the user's input is a greeting, return a randomly chosen greeting response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'
    #If no greeting was detected, then return an empty string
    return ' '

#A function to get a persons first and last name from the text
def getPerson(text):

    wordList = text.split() #Splitting the text into a list of words
    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) -1 and wordList[i].lower() == 'who' and wordList(i+1).lower() == 'is':
            return wordList[i+2] + ' '+ wordList[i+3]


while True:

    #Record the audio
    text = recordAudio()
    response = ''

    #Check for the wake word/phrase
    if(wakeWord(text) == True):

        #Check for greetings by the user
        response = response + greeting(text)

        #Check to see if the user said anything having to do with date
        if('date' in text):
             get_date = getDate()
             response = response + ' ' + get_date +'.'

        #Check to see if the user said anything having to do with the time
        if('time' in text):
             now = datetime.datetime.now()
             meridiem =''
             if now.hour >= 12:
                 meridiem = 'p.m' # Post meridiem (PM) after mid-day
                 hour = now.hour - 12
             else:
                meridiem = 'a.m' # Ante-Meridiem(AM) before mid-day
                hour = now.hour

             #Convert minute into a proper string.
             if now.minute <10:
                 minute = '0' + str(now.minute)
             else:
                 minute = str(now.minute)

             response = response +' ' +'It is  '+str(hour)+ ':' + minute+ ' ' +meridiem+'.'
        #Check to see if the user said 'who is'.
        if('who is' in text):
             person = getPerson(text)
             wiki = wikipedia.summary(person, sentences=2)
             response = response + ' ' + wiki