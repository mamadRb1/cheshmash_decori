import os
import datetime
import sqlite3
from flask import Flask, render_template, Response

app = Flask(__name__)

# صفحه اصلی سایت
@app.route('/')
def home():
    return render_template('index.html')

# گرفتن لیست صفحات فروشگاه از دیتابیس
@app.route('/pages', methods=['GET'])
def manage_pages():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM pages')
    rows = c.fetchall()
    conn.close()
    return {'pages': rows}

# سایت‌مپ داینامیک
@app.route('/sitemap.xml')
def sitemap():
    # صفحات ثابت
    static_pages = [
        {'loc': '/', 'priority': '1.0'},
        {'loc': '/shop', 'priority': '0.8'},
        {'loc': '/about', 'priority': '0.6'},
        {'loc': '/contact', 'priority': '0.6'}
    ]

    # محصولات/صفحات از دیتابیس
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT slug FROM pages')  # فرض: جدول pages ستون slug دارد
    product_rows = c.fetchall()
    conn.close()

    products = [{'loc': f'/product/{slug}', 'priority': '0.7'} for (slug,) in product_rows]

    pages = static_pages + products
    today = datetime.date.today().isoformat()

    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for page in pages:
        xml.append('  <url>')
        xml.append(f'    <loc>https://cheshmashdecori.ir{page["loc"]}</loc>')
        xml.append(f'    <lastmod>{today}</lastmod>')
        xml.append(f'    <priority>{page["priority"]}</priority>')
        xml.append('  </url>')

    xml.append('</urlset>')

    return Response('\n'.join(xml), mimetype='application/xml')

if __name__ == "__main__":
    app.run()
