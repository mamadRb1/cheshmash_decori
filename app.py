import os
from flask import Flask, render_template

app = Flask(__name__)

# صفحه اصلی
@app.route('/')
def index():
    return render_template('index.html')

# دسته‌بندی Home
@app.route('/category-home')
def category_home():
    return render_template('category-home.html')

# دسته‌بندی دکوراتیو (آینده)
@app.route('/category-decorative')
def category_decorative():
    return render_template('category-decorative.html')

# صفحه محصول (آینده)
@app.route('/product')
def product():
    return render_template('product.html')

# اجرای برنامه روی پورت Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
