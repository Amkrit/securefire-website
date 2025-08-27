
Securefire demo website (static frontend + simple Flask backend)
---------------------------------------------------------------
How to run locally:

1. Create a virtual environment
   python -m venv venv
   source venv/bin/activate   (Linux/Mac) or venv\Scripts\activate (Windows)

2. Install requirements:
   pip install -r requirements.txt

3. Run the app:
   python app.py

4. Open http://127.0.0.1:8501 in your browser.

Notes:
- Contact form submissions are saved to data/submissions.json
- PDFs are available under static/docs/
- This is a demo site for preview and internal use. Replace contact handling
  with proper email/sales CRM integration for production.
"# securefire-website" 
