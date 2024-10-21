import json
import random
import re
import nltk
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer

# Load the JSON data
with open('mental_health_data.json') as file:
    data = json.load(file)

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()


# Function to preprocess user input
def preprocess_input(input_text):
    input_text = input_text.lower()
    input_text = re.sub(r'[^a-zA-Z\s]', '', input_text)  # Remove punctuation
    words = nltk.word_tokenize(input_text)
    words = [lemmatizer.lemmatize(word) for word in words]
    return words


# Function to find the best matching intent
def get_intent(user_input):
    words = preprocess_input(user_input)
    for intent in data['intents']:
        for pattern in intent['patterns']:
            pattern_words = preprocess_input(pattern)
            if set(pattern_words) <= set(words):
                return intent
    return None


# Function to get a response based on the matched intent
def get_response(user_input):
    response = get_intent(user_input)
    if response:
        return random.choice(response['responses'])
    else:
        return "I'm here to support you. Please feel free to share your thoughts."


'''from transformers import pipeline

# Load a pre-trained text generation model
chat_model = pipeline('text-generation', model='gpt2')


def get_response(user_input):
    try:
        response = chat_model(user_input, max_length=100, num_return_sequences=1)
        return response[0]["generated_text"]
    except Exception as e:
        return "I'm here to support you. Please feel free to share your thoughts."'''
