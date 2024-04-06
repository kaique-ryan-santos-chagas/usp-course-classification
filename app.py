import sqlite3 as database

from flask import Flask, request
from flask_cors import CORS

from controllers.subjects_controller import SubjectsController

app = Flask(__name__)
connection = database.connect('subjects.db', check_same_thread=False)
CORS(app)

@app.route('/')

def welcome():

    return 'Welcome to IT courses classification!'

@app.route('/subjects')

def get_subjects():

    subjects_controller = SubjectsController(connection)
    subjects = subjects_controller.get_subjects()
    return subjects

@app.route('/send/subjects', methods=['POST'])

def send_subjects():

    inputs_data = request.json
    subjects_controller = SubjectsController(connection)
    prediction = subjects_controller.send_subjects(inputs_data['inputs_data'])

    return prediction[0]



if __name__ == '__main__':
    app.run()

