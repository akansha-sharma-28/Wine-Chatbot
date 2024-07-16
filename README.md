# Wine-Chatbot
Wine Chatbot
This repository contains a Flask-based chatbot application that utilizes natural language processing and translation services to provide answers related to wine-related queries. The chatbot supports multiple languages and includes text-to-speech functionality for enhanced user interaction.

Features
Multilingual Support: The chatbot supports 10 languages including English, Spanish, French, German, Italian, Dutch, Portuguese, Russian, Chinese, and Hindi.
Question Answering: Utilizes a Transformer-based model for question answering from a predefined corpus.
Translation: Supports translation of user queries and responses into different languages.
Text-to-Speech: Provides audio responses using Google Text-to-Speech API based on user language selection.
Dynamic Web Interface: Frontend interface built with HTML, CSS, and Bootstrap for a responsive and interactive user experience.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your_username/your_repository.git
cd your_repository
Install dependencies:
Copy code
pip install -r requirements.txt
Usage
Run the Flask application:
css
Copy code
python main.py
Open your web browser and go to http://localhost:5000 to interact with the chatbot.
Files
main.py: Backend server using Flask, integrates Transformer models, Google Translate, and Google Text-to-Speech API.
index.html: Frontend interface for the chatbot using HTML, CSS, and Bootstrap.
Sample Question Answers.json: JSON file containing sample question-answer pairs used for answering user queries.
