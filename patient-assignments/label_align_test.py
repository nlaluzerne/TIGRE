import unittest
import pandas as pd
from label_align import align

class TestLabelAlign(unittest.TestCase):

    def test_align(self):
        test_labels = pd.DataFrame()
        test_labels['name'] = ['Bob', 'Jane']
        test_labels['patient_id'] = ['sample_id', 'sample_id']
        test_labels['L'] = ['Y', 'N']
        test_labels['R'] = ['N', 'Y']

        expected_aligned = pd.DataFrame()
        expected_aligned['name_1'] = ['Bob']
        expected_aligned['name_2'] = ['Jane']
        expected_aligned['patient_id'] = ['sample_id']
        expected_aligned['L_1'] = ['Y']
        expected_aligned['L_2'] = ['N']
        expected_aligned['R_1'] = ['N']
        expected_aligned['R_2'] = ['Y']

        actual_aligned = align(test_labels)
        pd.testing.assert_frame_equal(expected_aligned, actual_aligned)

if __name__ == '__main__':
    unittest.main()
