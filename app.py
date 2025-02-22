import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
app.config['SECRET_KEY'] = 'Deepubhai'
app.config['SECURITY_PASSWORD_SALT'] = 'Deepu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)


with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Validate required fields
    if not username or not email or not password:
        return jsonify({'message': 'Username, email, and password are required.'}), 400

    # Check if a user with the given username or email already exists
    if User.query.filter(or_(User.username == username, User.email == email)).first():
        return jsonify({'message': 'Username or email already exists.'}), 400

    # Create a new user
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        return jsonify({'message': 'Login successful.'}), 200
    else:
        return jsonify({'message': 'Invalid username or password.'}), 401

if __name__ == '__main__':
    app.run(debug=True)