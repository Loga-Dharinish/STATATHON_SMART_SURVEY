
from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime
from logic.question_model import get_next_question

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    user_id = data['user_id']
    question_id = data['question_id']
    question_text = data['question_text']
    answer = data['answer']

    conn = sqlite3.connect('survey.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO survey_responses (user_id, question_id, question_text, answer, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, question_id, question_text, answer, datetime.now()))
    conn.commit()
    conn.close()

    next_question = get_next_question(question_id, answer)
    return jsonify(next_question)

if __name__ == '__main__':
    app.run(debug=True)
