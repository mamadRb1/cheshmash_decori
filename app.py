from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# ساخت جدول اگر وجود ندارد
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS pages (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL)')
conn.commit()
conn.close()

@app.route('/')
def home():
    return "چشماش‌دکوری پنل فعال است"

@app.route('/pages', methods=['GET', 'POST'])
def manage_pages():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    if request.method == 'POST':
        username = request.json.get('username')
        if not username:
            conn.close()
            return jsonify({"error": "Username is required"}), 400
        c.execute('INSERT INTO pages (username) VALUES (?)', (username,))
        conn.commit()
        conn.close()
        return jsonify({"message": "User created successfully", "username": username}), 201

    # GET
    c.execute('SELECT id, username FROM pages')
    data = [{"id": row[0], "username": row[1]} for row in c.fetchall()]
    conn.close()
    return jsonify(data), 200

@app.route('/pages/<int:page_id>', methods=['PUT'])
def update_page(page_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    username = request.json.get('username')
    if not username:
        conn.close()
        return jsonify({"error": "Username is required"}), 400

    # چک کن ببین رکورد وجود دارد یا نه
    c.execute('SELECT id FROM pages WHERE id=?', (page_id,))
    if not c.fetchone():
        conn.close()
        return jsonify({"error": "Record not found"}), 404

    c.execute('UPDATE pages SET username=? WHERE id=?', (username, page_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "User updated successfully", "id": page_id, "username": username}), 200

@app.route('/pages/<int:page_id>', methods=['DELETE'])
def delete_page(page_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute('SELECT id FROM pages WHERE id=?', (page_id,))
    if not c.fetchone():
        conn.close()
        return jsonify({"error": "Record not found"}), 404

    c.execute('DELETE FROM pages WHERE id=?', (page_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "User deleted successfully", "id": page_id}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
