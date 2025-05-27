import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musiclibrary
import pywhatkit 
import google.generativeai as genai 




recognizer = sr.Recognizer()
engine = pyttsx3.init()


genai.configure(api_key="enter your own API key")  #your actual key
model = genai.GenerativeModel("gemini-1.5-flash")



voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #female voice k liye index 1 
engine.setProperty('rate', 150) # Speed of speech
engine.setProperty('volume', 1.0) # Volume level (0.0 to 1.0)




def speak(text):
    time.sleep(0.3)
    engine.say(text)
    engine.runAndWait()

#function to ask Gemini AI
def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt) 
        return response.text
    except Exception as e:
        print(f"Error using Gemini: {e}")
        return "Sorry, something went wrong with the AI response."




def processcommand(c):
  if "open google" in c.lower():
    webbrowser.open("https://www.google.com")
  elif "open youtube" in c.lower():
    webbrowser.open("https://www.youtube.com")
  elif "open facebook" in c.lower():
    webbrowser.open("https://www.facebook.com")
  elif "open instagram" in c.lower():
    webbrowser.open("https://www.instagram.com")
  elif "open linkedin" in c.lower():
    webbrowser.open("https://www.linkedin.com")
  elif "introduce yourself" in c.lower():
    speak("I am Vani, your virtual assistant. I can help you with various tasks like searching the web, playing music, and answering questions.")
  elif c.lower().startswith("play"):
    
    try:  
        song = c.replace("play", "").strip() # Remove the word "play" from the command
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song) # This will play the song on YouTube
    
    except Exception as e:
            speak("Sorry, I couldn't play the song.")
            print(e)

  else:
    speak("Let me think...")
    answer = ask_gemini(c)
    speak(answer)
   



if __name__ =="__main__":
    speak(" initializing Vani.....")
    while True:
    # listen for the wake word "Sakhi" 
    # obtain audio from the microphone
    # obtain audio from the microphone
     r = sr.Recognizer()
     

     # recognize speech using Google Speech Recognition
     print("recognizing...")
     try:
       
        with sr.Microphone() as source:
         print("Listening...")
         audio = r.listen(source, timeout=3 , phrase_time_limit=3)

        word = r.recognize_google(audio)
        if(word.lower()=="vani"):
           speak("Yaa Vani is here")
           
           # listen for the command after the wake word
           
           with sr.Microphone() as source:
            print("Vani Active...")
            audio = r.listen(source , timeout=6  , phrase_time_limit=5)
            command = r.recognize_google(audio)
            print(command)

            processcommand(command) 

        
           

     except Exception as e:
       print(" error; {0}".format(e))



