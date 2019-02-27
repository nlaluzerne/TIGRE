import unittest
import os
import shutil
from PIL import Image
import json
import numpy as np
from image_data_generator import file_name, sample, image_info_gen, directory_contents, category_to_number
from image_data_generator import img_preprocc_gen

class TestImageDataGenerator(unittest.TestCase):

  def test_category_to_number(self):
    test_categories = ['apple', 'orange', 'banana']
    f = lambda x: category_to_number(test_categories, x)
    self.assertEqual(f('apple'), 0)
    self.assertEqual(f('banana'), 1)
    self.assertEqual(f('orange'), 2)

  def test_directory_contents(self):
    test_directory = 'test_data'
    expected_contents = ['train', 'validation']
    actual_contents = directory_contents(test_directory)
    self.assertCountEqual(expected_contents, actual_contents)

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

  def test_img_preprocc_gen(self):
    for batch_size, resize_dims in [(32, (100, 100)), (1, (1, 1))]:
      test_f = lambda x: np.array([1])
      test_gen = img_preprocc_gen('test_data/train', test_f,
        batch_size=batch_size, resize_dims=resize_dims)
      (example_imgs, example_pres), example_ys = next(test_gen)
      self.assertEqual(example_imgs.shape[0], batch_size)
      self.assertEqual(example_pres.shape[0], batch_size)
      self.assertEqual(example_ys.shape[0], batch_size)

      np.testing.assert_array_equal(np.array([[1]] * batch_size), example_pres)

      expected_imgs_shape = (batch_size,) + resize_dims + (3,)
      actual_imgs_shape = example_imgs.shape

      self.assertEqual(expected_imgs_shape, actual_imgs_shape)

  def setUp(self):
    # Construct fake images and jsons
    for image_set in ['train', 'validation']:
      for image_class in ['malignant', 'benign']:
        # Create folder
        os.makedirs('/'.join(['test_data', image_set, image_class]))
        for data_point in ['1', '2']:
          path = '/'.join(['test_data', image_set, image_class, data_point])
          self.create_image(path + '.jpg')
          self.create_json(path + '.json')

  def tearDown(self):
    shutil.rmtree('test_data')

if __name__ == "__main__":
  unittest.main()
