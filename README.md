# Wine-Chatbot
This repository contains a Flask-based chatbot application that utilizes natural language processing and translation services to provide answers related to wine-related queries. The chatbot supports multiple languages and includes text-to-speech functionality for enhanced user interaction.

# Features
1. Multilingual Support: 
   The chatbot supports 10 languages including English, Spanish, French, German, Italian, Dutch, Portuguese, Russian, Chinese, and Hindi.
2. Question Answering: 
   Utilizes a Transformer-based model for question answering from a predefined corpus.
3. Translation: 
   Supports translation of user queries and responses into different languages.
4. Text-to-Speech:
   Provides audio responses using Google Text-to-Speech API based on user language selection.
5. Dynamic Web Interface:
   Frontend interface built with HTML, CSS, and Bootstrap for a responsive and interactive user experience.

## Installation
# Clone the repository:
  1. In bash: git clone https://github.com/your_username/your_repository.git
  2. cd your_repository

# Install dependencies:
1. pip install -r requirements.txt

# Run the Flask application:
1. python main.py
 Open your web browser and go to http://localhost:5000 to interact with the chatbot.

# Files
There are three file are:
1. main.py: Backend server using Flask, integrates Transformer models, Google Translate, and Google Text-to-Speech API.
2. index.html: Frontend interface for the chatbot using HTML, CSS, and Bootstrap.
   # Note:
     First we create the New Folder name as template and then create the HTML file name as index.html. 
4. Sample Question Answers.json: JSON file containing sample question-answer pairs used for answering user queries.
