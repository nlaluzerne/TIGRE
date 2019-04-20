import os
from feature_extract import all_f
from sklearn.svm import SVC
import numpy as np

def file_lines(file_name):
    with open(file_name) as f:
        return [line[:-1] for line in f]

N = file_lines('patientAssignments/patients_nocancer.txt')
Y = file_lines('patientAssignments/patients_cancer.txt')

N_mat = [all_f(patient + 'A2BA-f.jpg', patient + 'A2BA-fc.jpg') for patient in N]
Y_mat = [all_f(patient + 'A2BA-f.jpg', patient + 'A2BA-fc.jpg') for patient in Y]
N_labels = [0] * len(N_mat)
Y_labels = [1] * len(Y_mat)

X = np.array(N_mat + Y_mat)
y = np.array(N_labels + Y_labels)

model = SVC()
model.fit(X, y)
