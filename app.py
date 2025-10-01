import datetime
import sqlite3
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sitemap.xml')
def sitemap():
    static_pages = [
        {'loc': '/',       'priority': '1.0'},
        {'loc': '/shop',   'priority': '0.8'},
        {'loc': '/about',  'priority': '0.5'},
        {'loc': '/contact','priority': '0.5'},
    ]
    today = datetime.date.today().isoformat()

    xml_parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemap.org/schemas/sitemap/0.9">'
    ]

    for page in static_pages:
        xml_parts.append(
            f"<url><loc>https://cheshmashdecori.ir{page['loc']}</loc>"
            f"<lastmod>{today}</lastmod>"
            f"<priority>{page['priority']}</priority></url>"
        )

    xml_parts.append('</urlset>')
    xml_str = "\n".join(xml_parts)
    return Response(xml_str, mimetype='application/xml')

@app.route('/debug/db')
def debug_db():
    try:
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        # لیست همه جدول‌ها
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cur.fetchall()

        # نمونه
