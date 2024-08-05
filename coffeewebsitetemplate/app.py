from flask import Flask, render_template, url_for

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return render_template('index.html')

# Menu route
@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)