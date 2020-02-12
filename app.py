
from flask import Flask, jsonify, request
app = Flask(__name__)
import os, psycopg2, requests


DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()


@app.route('/get_latest')
def index():

    cur.execute("SELECT * FROM text_output;")

    text_output = cur.fetchall()

    return jsonify(text_output[-1])

@app.route('/add_record', methods=['POST'])
def add():

    data = request.get_json()

    author = data.get('author')

    text = data.get('text')

    sql_statement = f"""INSERT INTO text_output (author, text) VALUES ('{author}', '{text}');"""


    cur.execute(sql_statement)

    return sql_statement

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)