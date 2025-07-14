
import pywhatkit

try:
    song=input("Enter the song you want to listen :")
    pywhatkit.playonyt(song)
    print("Successfully played your song!")

except:
    print('An unexcepted Error!')