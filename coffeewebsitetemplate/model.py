from flask_sqlalchemy import SQLAlchemy

# יצירת אובייקט SQLAlchemy
db = SQLAlchemy()

# מודל משתמשים
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(80), nullable=False)

# הוספת משתמשים
def add_user(username, password, role):
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        print(f"User '{username}' already exists.")
    else:
        new_user = User(username=username, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()

# אימות משתמשים
def authenticate_user(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        return user.role  # מחזיר את התפקיד של המשתמש (role)
    else:
        return None

# מתפעל
# model.py

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(80), nullable=False)
    items = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Open')

# פונקציה לקבלת הזמנות פתוחות
def get_open_orders():
    return Order.query.filter_by(status='Open').all()

# פונקציה לסגירת הזמנה
def close_order(order_id):
    order = Order.query.get(order_id)
    if order:
        order.status = 'Closed'
        db.session.commit()
