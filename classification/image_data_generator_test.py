import unittest
import os
import shutil
from PIL import Image
import json
from image_data_generator import file_name, sample, image_info_gen

class TestImageDataGenerator(unittest.TestCase):

  def test_sample(self):
    expected_sample_results = [('1', 'malignant'), ('2', 'malignant'),
                               ('1', 'benign'), ('2', 'benign')]
    actual_sample_results = []
    for _ in range(100):
      actual_sample_results.append(sample('test_data/train'))
    self.assertEqual(set(expected_sample_results), set(actual_sample_results))

  def test_file_name(self):
    self.assertEqual(file_name('path/to/file.txt'), 'file')
    self.assertEqual(file_name('file.txt'), 'file')

  @staticmethod
  def create_json(path):
    j = {'a': 1, 'b': 2, 'c': 3}
    with open(path, 'w') as f:
      json.dump(j, f)

  def test_create_json(self):
    test_path = 'temp.json'
    self.create_json(test_path)
    self.assertTrue(os.path.exists(test_path))
    os.remove(test_path)

  @staticmethod
  def create_image(path, dims=(150, 150)):
    img = Image.new('RGB', dims)
    img.save(path)

  def setUp(self):

    # Construct fake validation/training folders
    os.makedirs('test_data')
    os.makedirs('test_data/train')
    os.makedirs('test_data/validation')
    os.makedirs('test_data/train/malignant')
    os.makedirs('test_data/train/benign')
    os.makedirs('test_data/validation/malignant')
    os.makedirs('test_data/validation/benign')

    # Construct fake images and jsons
    for image_set in ['train', 'validation']:
      for image_class in ['malignant', 'benign']:
        for data_point in ['1', '2']:
          path = '/'.join(['test_data', image_set, image_class, data_point])
          self.create_image(path + '.jpg')
          self.create_json(path + '.json')

  def tearDown(self):
    shutil.rmtree('test_data')

if __name__ == "__main__":
  unittest.main()
