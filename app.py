from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# ساخت جدول اگر وجود نداشت
def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS pages (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT)')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return "چشماش‌دکوری پنل فعال است"

@app.route('/pages', methods=['GET', 'POST'])
def manage_pages():
    init_db()  # ساخت جدول قبل از هر کاری
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    if request.method == 'POST':
        data = request.get_json()
        if not data or 'username' not in data:
            conn.close()
            return jsonify({"error": "Username is required"}), 400
        username = data['username']
        c.execute('INSERT INTO pages (username) VALUES (?)', (username,))
        conn.commit()
        conn.close()
        return jsonify({"message": "User created successfully", "username": username}), 201

    # متد GET
    c.execute('SELECT * FROM pages')
    data = c.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
