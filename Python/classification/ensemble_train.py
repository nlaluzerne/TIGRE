import os
from feature_extract import all_f
from sklearn.svm import SVC
import numpy as np

N = os.listdir('Images_noBG/N')
Y = os.listdir('Images_noBG/Y')

N_mat = [all_f(patient + 'A2BA-f.jpg', patient + 'A2BA-fc.jpg') for patient in N]
Y_mat = [all_f(patient + 'A2BA-f.jpg', patient + 'A2BA-fc.jpg') for patient in Y]
N_labels = [0] * len(N_mat)
Y_labels = [1] * len(Y_mat)

X = np.array(N_mat + Y_mat)
y = np.array(N_labels + Y_labels)

model = SVC()
model.fit(X, y)
