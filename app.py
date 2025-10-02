from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# مسیر اصلی سایت - صفحه طلایی/بنفش
@app.route('/')
def home():
    return render_template('index.html')

# مسیر سرو کردن sitemap.xml
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml')

# اختیاری برای گوگل - سرو robots.txt
@app.route('/robots.txt')
def robots():
    return send_from_directory('.', 'robots.txt')

if __name__ == "__main__":
    # اتومات اجرا می‌کنه Render - برای لوکال تست
    app.run(host='0.0.0.0', port=5000)
