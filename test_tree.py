import random

from joblib import load

inputs = []

for count in range(63):

    input = random.randint(0, 1)
    inputs.append(input)

decision_tree = load('courses_classification.joblib')

course_prediction = decision_tree.predict([inputs])
print(course_prediction)