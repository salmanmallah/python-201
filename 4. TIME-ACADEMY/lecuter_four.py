# """
# All about function.
# """

# i = 0
# while i <= 10:
#     print(i)
#     i += 2



import sys
import pyttsx3


# we would initialize the Engine TTS
tts=pyttsx3.init()
while True:
    text=input("Enter the text you want:")
    if text.upper()=="QUIT":
        print("THanks for playing BYE BYE")
        sys.exit
    tts.say(text)
    # THis line will make the engine to say it 
    tts.runAndWait()