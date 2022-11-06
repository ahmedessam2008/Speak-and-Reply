import pyttsx3
import speech_recognition
import pyaudio

# engine = pyttsx3.init() # object creation
# """ RATE Property"""
# engine.setProperty('rate', 100)     # setting up new voice rate
# """VOLUME Property"""
# engine.setProperty('volume',1.5)    # setting up volume level  between 0 and 1
# """VOICE Property"""
# voices = engine.getProperty('voices')       #getting details of current voice
# #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male,  1 for female
# engine.setProperty('voice', voices[1].id)
# text_to_speach = "Hello World! My current speaking rate is"
# engine.say(text_to_speach)
# engine.say(text_to_speach)
# engine.runAndWait()
# engine.stop()
# """Saving Voice to a file"""
# # On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()

rec = speech_recognition.Recognizer() # For create new instance for listen

while True:
  with speech_recognition.Microphone() as MicSource: # For create new instance for speeking
    print("Say Some Thing: ....... ")
    audio = rec.listen(MicSource)  # save the sound it heard in variable audio
  
  text = rec.recognize_google(audio)  # service from google to convert the sound to words 
  if "hello" in text:
    print("Hello Ahmed")
  elif "old" in text:
    print("i am 50 years old")
  else:
    print("i dont anderstand you")
    
