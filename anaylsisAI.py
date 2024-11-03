import spacy
from textblob import TextBlob
from collections import Counter

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# List of common filler words
filler_words = ["uh", "um", "like", "I think", "maybe", "sort of"]

def analyze_transcript(transcript):
    # Analyze the transcript using spaCy
    doc = nlp(transcript)
    feedback = []

    # Check for filler words
    filler_detected = False
    for token in doc:
        if token.text.lower() in filler_words:
            filler_detected = True
            feedback.append(f"Filler word detected: '{token.text}'")
    
    if filler_detected:
        feedback.append("Suggestion: Try to minimize filler words for clearer communication.")

    # Rule-based analysis for vague language
    if "I don’t remember" in transcript or "I guess" in transcript:
        feedback.append("Response contains vague language. Be more specific. Try to provide concrete examples or details.")

    # Sentiment Analysis
    blob = TextBlob(transcript)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        feedback.append("Overall sentiment: Positive")
    elif sentiment < 0:
        feedback.append("Overall sentiment: Negative")
    else:
        feedback.append("Overall sentiment: Neutral")

    # Keyword Extraction
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    keyword_freq = Counter(keywords).most_common(5)
    feedback.append("Top keywords: " + ", ".join([f"{word} ({freq})" for word, freq in keyword_freq]))
    
    # Suggestion based on keywords
    if any(keyword in ['project', 'customer'] for keyword, _ in keyword_freq):
        feedback.append("Suggestion: Provide more detailed explanations of your projects and customer interactions.")

    # Length of Responses
    responses = [sent.text for sent in doc.sents]
    average_length = sum(len(resp.split()) for resp in responses) / len(responses) if responses else 0
    feedback.append(f"Average response length: {average_length:.2f} words")
    
    # Suggestion based on response length
    if average_length < 15:
        feedback.append("Suggestion: Your responses are on the shorter side. Consider adding more explanations and details to enhance your answers.")
    elif average_length > 30:
        feedback.append("Suggestion: Your responses are quite lengthy. Aim to be more concise while still providing enough information.")

    return "\n".join(feedback)

# Example interview transcript
def read_transcript(file_path):
    with open(file_path, 'r') as file:
        transcript = file.read()
    return transcript


"""if __name__ == "__main__":
    # Specify the path to the transcript file
    file_path = 'example.txt'  # Make sure this file exists in the same directory

    # Read the transcript from the file
    transcript = read_transcript(file_path)

    # Analyze the transcript and print feedback
    feedback = analyze_transcript(transcript)
    print("Feedback:\n", feedback)"""