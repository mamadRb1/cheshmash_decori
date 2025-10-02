from flask import Flask, render_template, redirect

app = Flask(__name__)

# صفحه اصلی
@app.route("/")
def home():
    # قالب اصلی رو اینجا اجرا کن
    return render_template("index.html")

# مسیرهای اضافی → ریدایرکت دائمی به صفحه اصلی
@app.route("/product")
def product():
    return redirect("/", code=301)

@app.route("/decorative")
def decorative():
    return redirect("/", code=301)

@app.route("/category-home")
def category_home():
    return redirect("/", code=301)

@app.route("/c")
def c():
    return redirect("/", code=301)

# اگر مسیر ناشناخته‌ای وارد شد
@app.errorhandler(404)
def page_not_found(e):
    return redirect("/", code=301)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
