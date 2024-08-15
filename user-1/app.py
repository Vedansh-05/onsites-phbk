from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:1234@main-db:3306/user-db'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

@app.route('/contacts', methods=['GET'])
def get_contacts():
    user_id = request.args.get('user_id')
    contacts = Contact.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': c.id, 'name': c.name, 'phone_number': c.phone_number} for c in contacts])

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.json
    new_contact = Contact(
        name=data['name'],
        phone_number=data['phone_number'],
        user_id=data['user_id']
    )
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({'message': 'Contact added successfully', 'id': new_contact.id}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5001)