from flask import Flask, send_from_directory

app = Flask(__name__)

# صفحه اصلی
@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="fa">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>چشماش دکوری</title>
        <link rel="manifest" href="/manifest.json">
        <script>
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('/service-worker.js');
        }
        </script>
        <link href="https://fonts.googleapis.com/css2?family=Vazir&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Vazir', sans-serif;
                background-color: #2c084e;
                color: #d4af37;
                margin: 0;
                text-align: center;
                padding: 50px;
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.2rem;
            }
            .btn {
                display: inline-block;
                margin: 15px;
                padding: 10px 20px;
                background-color: #d4af37;
                color: #2c084e;
                text-decoration: none;
                border-radius: 7px;
                font-weight: bold;
                transition: 0.3s;
            }
            .btn:hover {
                background-color: #b8962e;
            }
        </style>
    </head>
    <body>
        <h1>🎉 خوش اومدی به چشماش دکوری 🎉</h1>
        <p>بهترین دکورها و اکسسوری‌ها اینجا هست</p>

        <!-- دکمه محصولات -->
        <a class="btn" href="/products">مشاهده محصولات</a>

        <!-- واتساپ -->
        <a class="btn" href="https://wa.me/09927152884" target="_blank">چت در واتساپ</a>

        <!-- نصب PWA -->
        <button class="btn" onclick="installPWA()">📲 نصب اپلیکیشن</button>

        <script>
        let deferredPrompt;
        window.addEventListener('beforeinstallprompt', (e) => {
            e.preventDefault();
            deferredPrompt = e;
        });

        function installPWA() {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                deferredPrompt.userChoice.then((choiceResult) => {
                    deferredPrompt = null;
                });
            }
        }
        </script>
    </body>
    </html>
    """

# روت خدمت manifest.json
@app.route('/manifest.json')
def manifest():
    return send_from_directory('.', 'manifest.json')

# روت خدمت service-worker.js
@app.route('/service-worker.js')
def sw():
    return send_from_directory('.', 'service-worker.js')

# مثال مسیر محصولات
@app.route('/products')
def products():
    return "<h2>لیست محصولات اینجا میاد...</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




