from flask import Flask, render_template, request, redirect, url_for, flash
from model import db, User, add_user, authenticate_user, get_open_orders, close_order

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

# מתפעל
@app.route('/operator')
def operator():
    orders = get_open_orders()
    return render_template('operator.html', orders=orders)

@app.route('/operator/close-order/<int:order_id>', methods=['POST'])
def close_order_route(order_id):
    close_order(order_id)  # זו הפונקציה מהמודל
    flash(f'Order {order_id} has been closed.', 'success')
    return redirect(url_for('operator'))

# לקוח
@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/customer/place-order', methods=['POST'])
def place_order():
    customer_name = request.form['customer_name']
    order_items = request.form['order_items']
    # שמירת ההזמנה בבסיס הנתונים
    flash('Your order has been placed successfully!', 'success')
    return redirect(url_for('customer'))

@app.route('/customer/review', methods=['POST'])
def submit_review():
    review_text = request.form['review_text']
    rating = request.form['rating']
    review_photo = request.files.get('review_photo')
    # שמירת הביקורת בבסיס הנתונים
    flash('Your review has been submitted!', 'success')
    return redirect(url_for('customer'))

if __name__ == '__main__':
    app.run(debug=True)
