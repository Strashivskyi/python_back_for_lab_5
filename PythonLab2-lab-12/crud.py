import copy
import json
import logging
from os import abort

from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "postgres+psycopg2://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"]
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Bank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_number = db.Column(db.Integer, unique=False)
    credit_number = db.Column(db.Integer, unique=False)
    name = db.Column(db.String(64), unique=False)

    def __init__(self, name=None, client_number=0, credit_number=0):
        self.name = name
        self.client_number = client_number
        self.credit_number = credit_number


class BankSchema(ma.Schema):
    class Meta:
        fields = ('name', 'client_number', 'credit_number')


bank_schema = BankSchema()
banks_schema = BankSchema(many=True)


@app.route("/bank", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def add_bank():
    name = request.json['name']
    client_number = request.json['client_number']
    credit_number = request.json['credit_number']

    bank = Bank(name, client_number, credit_number)

    db.session.add(bank)
    db.session.commit()
    response = bank_schema.jsonify(bank)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/bank", methods=["GET"])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def get_banks():
    all_banks = Bank.query.all()
    result = banks_schema.dump(all_banks)
    response = jsonify({'banks': result})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/bank/<id>", methods=["GET"])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def get_bank(id):
    bank = Bank.query.get(id)
    if not bank:
        abort(404)
    response = bank_schema.jsonify(bank)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/bank/<id>", methods=["PUT"])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def update_bank(id):
    bank = Bank.query.get(id)
    if not bank:
        abort(404)
    old_bank = copy.deepcopy(bank)
    bank.name = request.json['name']
    bank.client_number = request.json['client_number']
    bank.credit_number = request.json['credit_number']
    db.session.commit()
    response = bank_schema.jsonify(old_bank)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/bank/<id>", methods=["DELETE"])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def delete_bank(id):
    bank = Bank.query.get(id)
    if not bank:
        abort(404)
    db.session.delete(bank)
    db.session.commit()
    response = bank_schema.jsonify(bank)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
#     response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE, HEAD')
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     print(response.headers)
#     return response


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
