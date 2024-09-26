from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import random
from database import init_db, insert_submission, get_submissions

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_quote = random.choice([
        "Life is what happens when you're busy making other plans.",
        "Get busy living or get busy dying.",
        "You have within you right now, everything you need to deal with whatever the world can throw at you."
    ])
    return render_template('index.html', time=current_time, quote=random_quote)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    
    # Insert submission into the database
    insert_submission(name, email, phone)
    
    return render_template('submit.html', name=name,email=email, phone=phone)

@app.route('/submissions')
def show_submissions():
    submissions = get_submissions()
    return render_template('submissions.html', submissions=submissions)

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
