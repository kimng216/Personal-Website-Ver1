import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Main page

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use the PORT from Heroku
    app.run(debug=True, host="0.0.0.0", port=port)