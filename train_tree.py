import sqlite3 as database 

from sklearn import tree
from joblib import dump

connection = database.connect('subjects.db')

subjects_data_engenharia = connection.execute('SELECT engenharia_computacao FROM subjects_courses')
subjects_data_sistemas = connection.execute('SELECT sistemas_informacao FROM subjects_courses')
subjects_data_ciencia = connection.execute('SELECT ciencia_computacao FROM subjects_courses')

data_engenharia = subjects_data_engenharia.fetchall()
data_sistemas = subjects_data_sistemas.fetchall()
data_ciencia = subjects_data_ciencia.fetchall()

subjects_engenharia = [int(subject[0]) for subject in data_engenharia]
subjects_sistemas = [int(subject[0]) for subject in data_sistemas]
subjects_ciencia = [int(subject[0]) for subject in data_ciencia]

connection.close()

decision_tree = tree.DecisionTreeClassifier()
labels = ['Engenharia da Computação', 'Sistemas de Informação', 'Ciência da Computação']
data = [subjects_engenharia, subjects_sistemas, subjects_ciencia]

decision_tree.fit(data, labels)
dump(decision_tree, 'courses_classification.joblib')



