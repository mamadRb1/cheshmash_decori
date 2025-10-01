from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# ساخت جدول اگر وجود ندارد
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS pages (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)')
conn.commit()
conn.close()

# صفحه اصلی سایت (PWA)
@app.route('/')
def home():
    return render_template('index.html')

# مدیریت صفحات (GET برای گرفتن لیست صفحات)
@app.route('/pages', methods=['GET'])
def manage_pages():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM pages')
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)

# اضافه کردن صفحه جدید (POST)
@app.route('/pages', methods=['POST'])
def add_page():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('INSERT INTO pages (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "صفحه با موفقیت اضافه شد!"})

# اجرای سرور لوکال (برای تست)
     import os

     if __name__ == "__main__":
         port = int(os.environ.get("PORT", 5000))
         app.run(host="0.0.0.0", port=port)

