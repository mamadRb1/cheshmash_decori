import datetime
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sitemap.xml')
def sitemap():
    static_pages = [
        {'loc': '/', 'priority': '1.0'},
        {'loc': '/shop', 'priority': '0.8'},
        {'loc': '/about', 'priority': '0.6'},
        {'loc': '/contact', 'priority': '0.6'}
    ]
    today = datetime.date.today().isoformat()

    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for page in static_pages:
        xml.append('  <url>')
        xml.append(f'    <loc>https://cheshmashdecori.ir{page["loc"]}</loc>')
        xml.append(f'    <lastmod>{today}</lastmod>')
        xml.append(f'    <priority>{page["priority"]}</priority>')
        xml.append('  </url>')

    xml.append('</urlset>')

    return Response('\n'.join(xml), mimetype='application/xml')

if __name__ == "__main__":
    app.run()
