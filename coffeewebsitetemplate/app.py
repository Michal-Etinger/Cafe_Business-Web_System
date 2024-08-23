


from flask import Flask, render_template, request, redirect, url_for, flash
from model import db, User, add_user, authenticate_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# חיבור SQLAlchemy לאפליקציה
db.init_app(app)

# יצירת טבלת המשתמשים והוספת משתמשים ראשוניים
with app.app_context():
    db.create_all()
    add_user('admin', 'adminpass', 'admin')
    add_user('customer', 'customerpass', 'customer')
    add_user('operator', 'operatorpass', 'operator')

# דף ה-login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        role = authenticate_user(username, password)
        if role:
            flash(f'Success! Logged in as {role}', 'success')
            
            if role == 'admin':
                return redirect(url_for('admin'))
            elif role == 'customer':
                return redirect(url_for('customer'))
            elif role == 'operator':
                return redirect(url_for('operator'))
        else:
            flash('Login failed. Please check your username and password.', 'danger')

    return render_template('login.html')



# Index route
@app.route('/')
def index():
    return render_template('index.html')

# Menu route
@app.route('/menu')
def menu():
    return render_template('menu.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Admin route
@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
