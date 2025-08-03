
import sqlite3

conn = sqlite3.connect('survey.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS survey_responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        question_id TEXT,
        question_text TEXT,
        answer TEXT,
        timestamp TEXT
    )
''')
conn.commit()
conn.close()
