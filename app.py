from flask import Flask, request, render_template, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'VARIABLE_STORED_ON_VAULT'

# DB simulée
users_db = {
    "admin": generate_password_hash("adminpassword")
}

# Route d'authentification
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users_db and check_password_hash(users_db[username], password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Login échoué", 403
    return render_template('login.html')

# Route protégée
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"Bienvenue {session['username']} ! Cette page est protégée !"
    return redirect(url_for('login'))

# Route de déco
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
