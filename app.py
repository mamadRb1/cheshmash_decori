from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return "چشماش‌دکوری پنل فعال است"

@app.route('/pages', methods=['GET', 'POST'])
def manage_pages():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    if request.method == 'POST':
        username = request.json.get('username')
        c.execute('INSERT INTO pages (username) VALUES (?)', (username,))
        conn.commit()
    c.execute('SELECT * FROM pages')
    data = c.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
