import pyttsx3
import speech_recognition as sr 
import pyjokes 
import pywhatkit
import datetime
import wikipedia
from sys import exit 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa',' ')
                print(command)
        return command

    except:
        take_command()
    
def run_alexa():

    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing '+ song +'in youtube')
        song_name = song  
        pywhatkit.playonyt(song_name)

    elif 'time' in command :
        time = datetime.datetime.now().strftime("%I:%M:%p")
        talk('Current time is '+ time)

    # elif 'who the heck is' in command:
    #     person = command.replace('who the heck is','')
    #     info = wikipedia.summary(person,1)
    #     print(info)
    #     talk(info)

    elif 'date' in command:
        talk("sorry, I have a headache")        

    elif 'are you single' in command:
        talk('I am in a relationship with your wifi')
    
    elif 'jokes' in command:
        a = pyjokes.get_joke()
        print(a)
        talk(a)

    elif 'exit' in command:
        talk('Closing programme')
        exit()

    elif 'hello' or 'hey' in command:
        talk('hello, How may i help you')

    else:
        talk('please say the command again')

while True:
    run_alexa()
