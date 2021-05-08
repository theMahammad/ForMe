from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    address2 = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    cardType = db.Column(db.String(50), nullable=False)
    zip = db.Column(db.Integer, nullable=False)
    payment = db.Column(db.String(50))
    card_name = db.Column(db.String(50), nullable=False)  
    card_number = db.Column(db.Integer, nullable=False)
    expiration = db.Column(db.String(50), nullable=False)
    cvv = db.Column(db.Integer, nullable=False)


@app.route("/")
def index():
    addresses = Address.query.all()
    return render_template('index.html',addresses=addresses)

@app.route("/add",methods=['GET','POST'])
def add():
    if request.method=='POST':
        address = Address(
            f_name = request.form['f_name'],
            l_name = request.form['l_name'],
            username = request.form['username'],
            email = request.form['email'],
            address = request.form['address'],
            address2 = request.form['address2'],
            country = request.form['country'],
            state= request.form['state'],
            cardType =request.form['cardType']
            zip= request.form['zip'],
            payment = request.form['payment'],
            card_name = request.form['card_name'],
            card_number = request.form['card_number'],
            expiration = request.form['expiration'],
            cvv = request.form['cvv']
        )

        db.session.add(address)
        db.session.commit()
        return redirect('/')
    return render_template('add.html')

@app.route("/delete/<int:id>")
def delete(id):
    address=Address.query.get(id)
    db.session.delete(address)
    db.session.commit()
    return redirect('/')

@app.route("/update/<int:id>",methods = ['GET','POST'])
def update(id):
    address = Address.query.get(id)
    if request.method=='POST':
        address.f_name=request.form['f_name']
        address.l_name=request.form['l_name']
        address.username=request.form['username']
        address.address=request.form['address']
        db.session.commit()
        return redirect('/')
    return render_template('update.html',address=address)
# db.create_all()
if __name__=='__main__':
    app.run(debug=True)


    