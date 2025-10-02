from flask import Flask, render_template

app = Flask(__name__)

# مسیر صفحه اصلی
@app.route('/')
def index():
    return render_template('index.html')

# مسیر دسته‌بندی دکور خانه
@app.route('/category-home')
def category_home():
    return render_template('category-home.html')

# مسیر دسته‌بندی دکور تزئینی
@app.route('/category-decorative')
def category_decorative():
    return render_template('category-decorative.html')

# مسیر محصول
@app.route('/product')
def product():
    return render_template('product.html')

if __name__ == '__main__':
    # برای اجرا محلی
    app.run(debug=True)
