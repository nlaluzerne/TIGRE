import os
import random
from PIL import Image
import json
import numpy as np

# TODO(cmaxcy):
# - Add ability for batch size and image resize to be specified
# - Add tests for image_info_gen
# - Consider wrapping all in class

def read_json(filename):
  with open(filename, 'r') as f:
    return json.load(f)

def dict_to_array(dictionary):
  return np.array([dictionary[key] for key in sorted(dictionary.keys())])

def file_name(path):
  return os.path.splitext(os.path.basename(path))[0]

def directory_contents(path):
  return os.listdir(path)

def sample(path):

  classes = directory_contents(path)
  class_sample = random.choice(classes)

  files = directory_contents('/'.join([path, class_sample]))
  file_sample = file_name(random.choice(files))

  return file_sample, class_sample

def category_to_number(categories, category):
  return sorted(categories).index(category)

def image_info_gen(path):
  while True:
    classes = directory_contents(path)
    example, clas = sample(path)

    example_path = '/'.join([path, clas, example])

    img = Image.open('{}.jpg'.format(example_path))
    img = img.resize((100, 100))
    img = np.array(img)

    preprocess = read_json('{}.json'.format(example_path))
    preprocess = dict_to_array(preprocess)

    y = category_to_number(classes, clas)

    yield [np.array([img]), np.array([preprocess])], np.array([y])

def img_preprocc_gen(path, f, batch_size=32, resize_dims=(100, 100)):
    while True:
        imgs = []
        pres = []
        ys = []
        for _ in range(batch_size):
            classes = directory_contents(path)
            example, clas = sample(path)

            example_path = '/'.join([path, clas, example])

            with Image.open('{}.jpg'.format(example_path)) as img:
                img_array = np.array(img.resize(resize_dims))

            pre = f(img_array)
            y = category_to_number(classes, clas)

            imgs.append(img_array)
            pres.append(pre)
            ys.append(y)

        yield (np.array(imgs), np.array(pres)), np.array(ys)
