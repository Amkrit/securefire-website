from flask import Flask, render_template, request, jsonify, send_from_directory
import json, os

app = Flask(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
SUBMISSIONS_FILE = os.path.join(DATA_DIR, 'submissions.json')

def save_submission(entry):
    all_entries = []
    if os.path.exists(SUBMISSIONS_FILE):
        try:
            with open(SUBMISSIONS_FILE, 'r', encoding='utf-8') as f:
                all_entries = json.load(f)
        except Exception:
            all_entries = []
    all_entries.append(entry)
    with open(SUBMISSIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_entries, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/contact', methods=['POST'])
def api_contact():
    data = request.get_json(force=True)
    entry = {
        'name': data.get('name'),
        'email': data.get('email'),
        'message': data.get('message')
    }
    save_submission(entry)
    return jsonify({'message': 'Thank you — your enquiry has been recorded.'})

if __name__ == '__main__':
    # ✅ safer defaults for Windows
    app.run(host='127.0.0.1', port=5000, debug=True)
