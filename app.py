from flask import Flask, render_template, send_from_directory, jsonify
import os
import sqlite3

app = Flask(__name__)

# صفحه اصلی سایت
@app.route('/')
def home():
    return render_template('index.html')

# مسیر برای گرفتن لیست صفحات (مدیریت صفحات فروشگاه)
@app.route('/pages', methods=['GET'])
def manage_pages():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM pages')
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)

# سرو کردن sitemap.xml از روت دامنه
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')

if __name__ == '__main__':
    app.run()
