from flask import jsonify
from joblib import load


class SubjectsController:

    def __init__(self, connection):
        self.connection = connection

    def get_subjects(self):

        connection = self.connection

        subjects_data = connection.execute('SELECT subject_name FROM subjects_courses')
        subjects = subjects_data.fetchall()

        subjects = [str(subject[0]) for subject in subjects]

        return jsonify(subjects)
    
    def send_subjects(self, subjects):

        decision_tree = load('courses_classification.joblib')
        prediction = decision_tree.predict([subjects])

        return prediction


