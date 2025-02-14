import speech_recognition as aa  # To understand our commands
import pyttsx3  # This responds to us
import pywhatkit  # Helps play YouTube videos based on commands
import datetime  
import wikipedia  # Helps fetch information from Wikipedia when asked

listener = aa.Recognizer()  # Listener which recognizes our voice
machine = pyttsx3.init()  # Initializing text-to-speech

def talk(text):
    machine.say(text)
    machine.runAndWait()  # Ensures the assistant finishes speaking before proceeding

def input_instruction():
    try:  # If microphone doesn't work, this try & except will help without showing an error
        with aa.Microphone() as origin:  # Uses microphone to listen to our voice
            print("Listening...")
            speech = listener.listen(origin)  # Records speech using listener.listen(origin)
            instruction = listener.recognize_google(speech)  # Converts speech to text using Google’s Speech Recognition API
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', "").strip()  # Removing 'jarvis' and extra spaces
                print(instruction)
                return instruction
    except Exception as e:
        print("Error:", e)
        return ""  # Return empty string instead of a space

def play_jarvis():
    instruction = input_instruction()  # Get the user's voice command
    if not instruction:
        return  # Exit function if instruction is None or empty
    
    print(instruction)
    
    if "play" in instruction:
        song = instruction.replace('play', "").strip()#.strip():-to remove extra spaces when replacing words
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time: " + time)
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        talk("Today's date: " + date)
    elif 'how are you' in instruction:
        talk('I am fine, how about you?')
    elif 'what is your name' in instruction:
        talk('I am Jarvis, what can I do for you?')
    elif 'who is' in instruction:
        human = instruction.replace('who is', "").strip()
        try:
            info = wikipedia.summary(human, 1)  # Fetch a 1-line summary from Wikipedia
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError:
            talk("There are multiple results. Please be more specific.")
        except wikipedia.exceptions.PageError:
            talk("Sorry, I couldn't find information on that.")
    else:
        talk('Please repeat')
play_jarvis()
