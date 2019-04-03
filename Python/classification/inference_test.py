import unittest
import inference
import numpy as np

class TestInference(unittest.TestCase):

    def test_model_input_size(self):
        self.assertEqual((256, 256, 3),
            inference.model_input_size(inference.loaded_model))

    def test_resize(self):
        test_img = np.random.rand(100, 100, 3)
        for size in [(100, 100, 3), (50, 50, 3)]:
            self.assertEqual(size, inference.resize(test_img, size).shape)

if __name__ == "__main__":
    unittest.main()
