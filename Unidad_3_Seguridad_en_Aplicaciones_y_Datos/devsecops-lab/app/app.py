from flask import Flask, request, jsonify
import sqlite3
import subprocess

app = Flask(__name__)

# VULNERABILIDAD 1: Credencial hardcodeada
DB_PASSWORD = 'SuperSecret123!'
SECRET_KEY = 'hardcoded-secret-key-never-do-this'

def get_db():
    return sqlite3.connect('users.db')

# VULNERABILIDAD 2: SQL Injection
@app.route('/user')
def get_user():
    username = request.args.get('username')
    db = get_db()
    cursor = db.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return jsonify(cursor.fetchall())

# VULNERABILIDAD 3: Command Injection
@app.route('/ping')
def ping():
    host = request.args.get('host')
    result = subprocess.run(f'ping -c 1 {host}', shell=True,
                            capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)  # VULNERABILIDAD 4: debug en produccion
