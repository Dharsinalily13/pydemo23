from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'demo_secret_key'  # Change in production
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# Dummy data: User profiles (key: email, value: dict of fields)
users = {
    'admin@example.com': {
        'name': 'Admin User',
        'age': 30,
        'phone': '123-456-7890',
        'blood_group': 'O+',
        'address': '123 Main St',
        'password': 'password'  # Plain text for demo; hash in production
    }
}
alerts = []  # Dummy alerts list
resources = [
    {'id': 1, 'title': 'Emergency Kit Guide', 'category': 'Disaster', 'description': 'How to prepare an emergency kit.'},
    {'id': 2, 'title': 'Volunteer Training', 'category': 'Training', 'description': 'Online training for volunteers.'}
]
blog_posts = [
    {'id': 1, 'title': 'Helping in Disasters', 'content': 'Placeholder blog content...', 'comments': []}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sos', methods=['GET', 'POST'])
def sos():
    if request.method == 'POST':
        location = request.form.get('location')
        message = request.form.get('message')
        alerts.append({'location': location, 'message': message, 'user': session.get('user')})
        flash('SOS alert sent!')
        return redirect(url_for('home'))
    return render_template('sos.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email]['password'] == password:
            session['user'] = email
            return redirect(url_for('dashboard'))
        flash('Invalid email or password')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        if email in users:
            flash('Email already registered')
            return redirect(url_for('signup'))
        users[email] = {
            'name': request.form['name'],
            'age': int(request.form['age']),
            'phone': request.form['phone'],
            'blood_group': request.form['blood_group'],
            'address': request.form['address'],
            'password': request.form['password']  # Hash in production
        }
        session['user'] = email
        flash('Signup successful! Welcome.')
        return redirect(url_for('dashboard'))
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    user_profile = users.get(session['user'], {})
    user_alerts = [a for a in alerts if a.get('user') == session['user']]
    return render_template('dashboard.html', profile=user_profile, alerts=user_alerts)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/resources', methods=['GET', 'POST'])
def resources_page():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File uploaded!')
    category_filter = request.args.get('category', '')
    filtered = [r for r in resources if category_filter in r['category']] if category_filter else resources
    return render_template('resources.html', resources=filtered)

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=blog_posts)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/alerts')
def get_alerts():
    return jsonify(alerts)

if __name__ == '__main__':
    app.run(debug=True)