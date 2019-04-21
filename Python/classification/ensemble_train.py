import os
from feature_extract import all_f
from sklearn.svm import SVC
import numpy as np
import PIL
from getPatientIds import getPatients
import string
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def file_lines(file_name):
    with open(file_name) as f:
        return [line[:-1] for line in f]

def read_img(file_name):
    return np.asarray(PIL.Image.open(file_name))

N = file_lines('patientAssignments/patients_nocancer.txt')
Y = file_lines('patientAssignments/patients_cancer.txt')

ascii_chars = set([chr(i) for i in range(127)])

def strip(s):
    return ''.join([c for c in s if c in ascii_chars])

N = [strip(l) for l in N]
Y = [strip(l) for l in Y]

N_path = 'Images_noBG/N/'
Y_path = 'Images_noBG/Y/'
f_suffix = 'A2BA-f.jpg'
fc_suffix = 'A2BA-fc.jpg'

N_mat = [all_f(read_img(N_path + patient + f_suffix), read_img(N_path + patient + fc_suffix)) for patient in N]
Y_mat = [all_f(read_img(Y_path + patient + f_suffix), read_img(Y_path + patient + fc_suffix)) for patient in Y]
N_labels = [0] * len(N_mat)
Y_labels = [1] * len(Y_mat)

X = np.array(N_mat + Y_mat)
y = np.array(N_labels + Y_labels)

scaler = StandardScaler()

X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

model = SVC(C=10, gamma=.001, probability=True)
model.fit(X_train, y_train)

print(model.score(X_test, y_test))
