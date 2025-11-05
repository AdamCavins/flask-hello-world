import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Adam Cavins in 3308'

@app.route('/db_test')
def db_text():
    conn = psycopg2.connect("postgresql://lab_10_postgres_example_user:6B9Mk6jzeAc7heFuPwWaga9xq7PEnsVw@dpg-d45qa6s9c44c73c9iefg-a/lab_10_postgres_example")
    conn.close()
    return "Database Connection Successful"