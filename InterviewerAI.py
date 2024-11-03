from gtts import gTTS
import google.generativeai as genai
from pydub import AudioSegment
from pydub.playback import play

# AI's voice
def text_to_speech(text):
    # Initialize gTTS with the text to convert
    speech_AI = gTTS(text, lang='en')

    # Save the audio file
    speech_file = "C:/Users/ayesh/Downloads/Hackathon-24/speech.mp3"
    speech_AI.save(speech_file)

    # Load and play the audio file using pydub
    audio = AudioSegment.from_mp3(speech_file)
    play(audio)


# Configure the API key for Gemini
genai.configure(api_key="AIzaSyCcjSHe5m1XNVwEx-IJ9g2HPLMU5O7UWlc")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to generate the beginning to an interview
def generate_initial_question():
    prompt = "Generate the beginning of a behavioral interview as a friendly interviewer. Make sure to ask the candidate to tell you about themselves. Do not say anything else."
    response = model.generate_content(prompt)
    text_to_speech(response.text)
    with open('C:/Users/ayesh/Downloads/Hackathon-24/output.txt', 'a') as file:
        file.write(f"Bot: {response.text}\n")
    return response.text

# Function to generate an interview question
def generate_question():
    prompt = "Generate a behavioral interview question. Do not say anything else. The question may not be similar to questions you've previously asked. Take into account the candidate's previous responses if there are any."
    response = model.generate_content(prompt)
    text_to_speech(response.text)
    with open('C:/Users/ayesh/Downloads/Hackathon-24/output.txt', 'a') as file:
        file.write(f"Bot: {response.text}\n")
    return response.text

# Function to generate a follow-up question based on the candidate's response
def generate_follow_up(response_text):
    prompt = f"The candidate answered: '{response_text}'. Generate one relevant follow-up question based on their response. Do not say anything else. The question may not be similar to questions you've previously asked."
    response = model.generate_content(prompt)
    text_to_speech(response.text)
    with open('C:/Users/ayesh/Downloads/Hackathon-24/output.txt', 'a') as file:
        file.write(f"Bot: {response.text}\n")
    return response.text

# Function to generate an ending statement for the interview
def generate_end_statement():
    prompt = "Generate a closing statement to end an interview as an interviewer. Take into account the candidate's previous responses. Do not say anything else. Do not include information like names if the candidate did not give it to you."
    response = model.generate_content(prompt)
    text_to_speech(response.text)
    with open('C:/Users/ayesh/Downloads/Hackathon-24/output.txt', 'a') as file:
        file.write(f"Bot: {response.text}\n")
    return response.text
