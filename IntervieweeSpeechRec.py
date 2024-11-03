import speech_recognition as sr
import keyboard

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        # Capture audio from the microphone

        audio = recognizer.listen(source)

        try:
            # Use Google Web Speech API to recognize speech
            text = recognizer.recognize_google(audio)
            with open('C:/Users/ayesh/Downloads/Hackathon-24/output.txt', 'a') as file:
                file.write(f"User: {text}\n")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that. Try Again")
            with open('C:/Users/ayesh/Downloads/Hackathon-24/output.txt', 'a') as file:
                file.write(f"User: \n")
            return ""
        except sr.RequestError:
            print("Sorry, there seems to be an issue with the service. Try Again")
            with open('C:/Users/ayesh/Downloads/Hackathon-24/output.txt', 'a') as file:
                file.write(f"User: \n")  
            return ""

"""if __name__ == "__main__":
    while True: 
        recognize_speech()
        print("Next:")""" 


        