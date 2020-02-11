
from flask import Flask, jsonify
app = Flask(__name__)
import os, psycopg2, requests


DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()


@app.route('/get_latest')
def index():

    cur.execute("SELECT * FROM text_output;")

    text_output = cur.fetchone()    

    return jsonify(text_output)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)