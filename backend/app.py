#!/usr/bin/python
from flask import Flask, jsonify, request
import os
import dibi

CONST_DB_DILENAME: str = "database.db"

API_REG_ID = os.getenv('REACT_APP_API_REG_ID')
API_REG_NAME = os.getenv('REACT_APP_API_REG_NAME')

API_REG_GET = os.getenv('REACT_APP_API_REG_GET')
API_REG_GET_ID = os.getenv('REACT_APP_API_REG_GET_ID')+API_REG_ID
API_REG_GET_BY_NAME = os.getenv('REACT_APP_API_REG_GET_BY_NAME')+API_REG_NAME
API_REG_ADD = os.getenv('REACT_APP_API_REG_ADD')
API_REG_UPDATE_ID = os.getenv('REACT_APP_API_REG_UPDATE_ID')+API_REG_ID
API_REG_DELETE_ID = os.getenv('REACT_APP_API_REG_DELETE_ID')+API_REG_ID
API_REG_DELETE_ALL = os.getenv('REACT_APP_API_REG_DELETE_ALL')


app = Flask(__name__)
db = dibi.Database(CONST_DB_DILENAME)
db.create_registration_table()


@app.route(API_REG_GET, methods=['GET'])
def api_get_registartions():
    return jsonify(db.get_registrations())


@app.route(API_REG_GET_ID, methods=['GET'])
def api_get_registartion(registration_id):
    return jsonify(db.get_registration_by_id(registration_id))


@app.route(API_REG_GET_BY_NAME, methods=['GET'])
def api_get_registartions_by_name(name):
    return jsonify(db.get_registartions_by_name(name))


@app.route(API_REG_ADD,  methods=['POST'])
def api_add_registartion():
    registartion = request.get_json()
    return jsonify(db.insert_registration(registartion))


@app.route(API_REG_UPDATE_ID,  methods=['PUT'])
def api_update_registartion(registration_id):
    registartion = request.get_json()
    return jsonify(db.update_registration(registartion, registration_id))


@app.route(API_REG_DELETE_ID,  methods=['DELETE'])
def api_delete_registartion(registration_id):
    return jsonify(db.delete_registration(registration_id))


@app.route(API_REG_DELETE_ALL,  methods=['DELETE'])
def api_delete_all_rows():
    return jsonify(db.delete_all())


if __name__ == "__main__":
    app.run()
