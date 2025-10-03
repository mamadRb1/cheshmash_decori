from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="fa">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>چشماش دکوری</title>
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
        <h1>🎉 به چشماش دکوری خوش اومدی 🎉</h1>
        <p>فروشگاه اکسسوری و دکور با بهترین کیفیت</p>
        
        <!-- دکمه محصولات -->
        <a class="btn" href="/products">🛍 مشاهده محصولات</a>

        <!-- دکمه واتساپ -->
        <a class="btn" href="https://wa.me/989927152884" target="_blank">💬 چت در واتساپ</a>

        <!-- دکمه نصب -->
        <button class="btn" id="installBtn" style="display:none;">📲 نصب اپ</button>

        <script>
            let deferredPrompt;
            window.addEventListener('beforeinstallprompt', (e) => {
                e.preventDefault();
                deferredPrompt = e;
                document.getElementById('installBtn').style.display = 'inline-block';
            });

            document.getElementById('installBtn').addEventListener('click', async () => {
                if (deferredPrompt) {
                    deferredPrompt.prompt();
                    const { outcome } = await deferredPrompt.userChoice;
                    console.log('Install choice:', outcome);
                    deferredPrompt = null;
                }
            });
        </script>
    </body>
    </html>
    """

@app.route('/products')
def products():
    return """
    <html lang="fa">
    <head>
        <meta charset="UTF-8">
        <title>محصولات</title>
        <link href="https://fonts.googleapis.com/css2?family=Vazir&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Vazir', sans-serif;
                background-color: #2c084e;
                color: #d4af37;
                text-align: center;
                padding: 50px;
            }
            h1 {
                font-size: 2rem;
            }
        </style>
    </head>
    <body>
        <h1>🛍 لیست محصولات</h1>
        <p>اینجا محصولات رو می‌ذاریم...</p>
        <a href="/" style="color:#d4af37;">⬅ بازگشت</a>
    </body>
    </html>
    """
