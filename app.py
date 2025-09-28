from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# ساخت جدول در شروع برنامه
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
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    if request.method == 'POST':
        # دریافت امن مقدار username
        username = request.json.get('username')
        if not username:  # اعتبارسنجی وجود username
            conn.close()
            return jsonify({"error": "Username is required"}), 400
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
