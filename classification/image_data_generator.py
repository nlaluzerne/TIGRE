import os
import random
from PIL import Image
import numpy as np

def read_json(filename):
  with open(filename, 'r') as f:
    return json.load(f)

def dict_to_array(dictionary):
  return np.array([dictionary[key] for key in sorted(dictionary.keys())])

def file_name(path):
  return os.path.splitext(os.path.basename(path))[0]

def sample(path):
  file_class_pairs = []

  # Malignant files
  files = list(os.listdir('/'.join([path, 'malignant'])))
  class_name = ['malignant'] * len(files)
  file_class_pairs += list(zip(files, class_name))

  # Benign files
  files = list(os.listdir('/'.join([path, 'benign'])))
  class_name = ['benign'] * len(files)
  file_class_pairs += list(zip(files, class_name))

  f, c = random.choice(file_class_pairs)
  return file_name(f), c

def image_info_gen(path):
  while True:
    name, c = sample(path)

    example_path = '/'.join([path, c, name])

    img = Image.open('{}.jpg'.format(example_path))
    img = img.resize((100, 100))
    img = np.array(img)

    preprocess = read_json('{}.json'.format(example_path))
    preprocess = dict_to_array(preprocess)

    if c == 'benign':
      y = 0
    else:
      y = 1

    yield [np.array([img]), np.array([preprocess])], np.array([y])
