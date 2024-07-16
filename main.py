from flask import Flask, request, jsonify, render_template
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
from gtts import gTTS
from googletrans import Translator
from fuzzywuzzy import fuzz
import json
import os
import re

app = Flask(__name__)

# Load the corpus
with open('Sample Question Answers.json', 'r') as file:
    corpus = json.load(file)

# Initialize QA pipeline
tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased-distilled-squad')
model = AutoModelForQuestionAnswering.from_pretrained('distilbert-base-uncased-distilled-squad')
qa_pipeline = pipeline('question-answering', model=model, tokenizer=tokenizer)

# Supported languages with corresponding TTS voices
supported_languages = {
    'en': {'name': 'English', 'voice': 'en'},
    'es': {'name': 'Spanish', 'voice': 'es'},
    'fr': {'name': 'French', 'voice': 'fr'},
    'de': {'name': 'German', 'voice': 'de'},
    'it': {'name': 'Italian', 'voice': 'it'},
    'nl': {'name': 'Dutch', 'voice': 'nl'},
    'pt': {'name': 'Portuguese', 'voice': 'pt'},
    'ru': {'name': 'Russian', 'voice': 'ru'},
    'zh': {'name': 'Chinese', 'voice': 'zh-CN'},
    'hi': {'name': 'Hindi', 'voice': 'hi'}
}

# Store conversation history
conversation_history = []

# Initialize Translator
translator = Translator()

# Helper function to translate text
def translate_text(text, target_lang):
    translated = translator.translate(text, dest=target_lang)
    return translated.text

# Helper function to find the best answer from the corpus using fuzzy matching
def find_best_answer(question, language='en'):
    best_answer = ""
    best_score = float('-inf')
    for entry in corpus:
        context = entry.get(f'answer_{language}', entry['answer'])
        question_score = fuzz.partial_ratio(question.lower(), entry['question'].lower())
        if question_score > best_score:
            best_answer = context
            best_score = question_score
    return best_answer

# Helper function to handle follow-up questions
def handle_follow_up_question(question, language='en'):
    if not conversation_history:
        return "I'm sorry, I don't have any previous context to refer to."

    last_user_question = conversation_history[-1]['user']

    # Use regular expressions to identify references to previous questions
    match = re.search(r'(?:tell me|what about|more about)\s+(.*)', question.lower())
    if match:
        keyword = match.group(1).strip()
        for entry in reversed(conversation_history):
            if keyword in entry['user'].lower():
                return find_best_answer(keyword, language)

    # If no direct match, default to the last user question
    return find_best_answer(last_user_question, language)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        if not data or 'message' not in data:
            return jsonify({'answer': 'Error: Invalid request format. Missing "message" in JSON.'})

        user_input = data['message']
        language = data.get('language', 'en')
        print(f"User input: {user_input}, Language: {language}")

        if language not in supported_languages:
            return jsonify({'answer': f"Sorry, language '{language}' is not supported."})

        # Manage conversation history
        conversation_history.append({'user': user_input, 'language': language})

        # Translate user input if not in English
        if language != 'en':
            user_input = translate_text(user_input, 'en')

        # Handle follow-up questions based on context
        if any(word in user_input.lower() for word in ['tell me', 'what about', 'more about']):
            answer = handle_follow_up_question(user_input, language)
        else:
            answer = find_best_answer(user_input, language)

        if not answer:
            answer = 'Please contact the business directly for more information.'

        conversation_history.append({'bot': answer, 'language': language})

        # Translate answer back to user's language if necessary
        if language != 'en':
            answer = translate_text(answer, language)

        # Generate TTS if answer is not empty
        tts_url = ""
        if answer.strip():
            tts = gTTS(text=answer, lang=supported_languages[language]['voice'])
            tts_file = f"static/answer_{len(conversation_history)}.mp3"
            tts.save(tts_file)
            tts_url = f"/{tts_file}"

        return jsonify({'answer': answer, 'tts_url': tts_url})

    except KeyError as ke:
        return jsonify({'answer': f'KeyError: {str(ke)}. Please check your request format.'})

    except Exception as e:
        return jsonify({'answer': f'Error: {str(e)}'})

if __name__ == "__main__":
    if not os.path.exists('static'):
        os.mkdir('static')
    app.run(debug=True)
