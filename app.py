from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

# صفحه اصلی سایت (PWA)
@app.route('/')
def home():
    return render_template('index.html')

# برای گرفتن لیست صفحات مدیریت صفحات (GET)
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

    return jsonify({"message": "صفحه با موفقیت اضافه شد"})
    
