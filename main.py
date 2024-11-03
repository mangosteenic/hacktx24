from anaylsisAI import *
from IntervieweeSpeechRec import *
from InterviewerAI import *
import random

# Main Code

# Clear the contents of the file 
with open('output.txt', 'r+') as file:
    file.truncate(0)  # Clear the file contents   


text_to_speech("Welcome to the interview bot!")

# Randomly determine the number of questions (between 5 and 10)
number_of_questions = 3
text_to_speech(f"The interview will consist of {number_of_questions} questions.\n")

# Generate the first question to kick off the interview
initial_question = generate_initial_question()

for x in range (number_of_questions - 1):  # -1 because we already asked the first question
    user_input = recognize_speech()
    # Generate a follow-up based on the user's response
    follow_up = generate_follow_up(user_input)

    # Ask the follow-up question
    if follow_up.strip():
        print(f"Bot: {follow_up}")
        user_input = recognize_speech()  # Allow user to answer the follow-up
         
    # Generate a new question to continue the interview
    if (x < number_of_questions - 2):
        continue_question = generate_question()
        print(f"Bot: {continue_question}")

# End the interview with a closing statement
end_statement = generate_end_statement()
print(f"Bot: {end_statement}")

# Conclude the Interview Section
# Continuing with the Analysis 

file_path = 'output.txt'
transcript = read_transcript(file_path)

# Analyze the transcript and print feedback
feedback = analyze_transcript(transcript)
print("Feedback:\n", feedback)
