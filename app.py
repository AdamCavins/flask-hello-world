from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Adam Cavins in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://adam_cavins_lab_10_db_user:yY9X9efnGytwU6GxsaOIG3tT3mtIOlhB@dpg-d45r2sripnbc738rpt80-a/adam_cavins_lab_10_db")
    conn.close()
    return "Database Connection Successful"