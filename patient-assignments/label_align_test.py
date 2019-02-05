import unittest
import pandas as pd
from label_align import align

class TestLabelAlign(unittest.TestCase):

    def test_align(self):
        test_labels = pd.DataFrame()
        test_labels['name'] = ['Bob', 'Jane', 'Jane', 'Paul']
        test_labels['patient_id'] = ['sample_id_1', 'sample_id_1',
            'sample_id_2', 'sample_id_2']
        test_labels['L'] = ['Y', 'N', 'N', 'Y']
        test_labels['R'] = ['N', 'Y', 'Y', 'N']

        expected_aligned = pd.DataFrame()
        expected_aligned['name_1'] = ['Bob', 'Jane']
        expected_aligned['name_2'] = ['Jane', 'Paul']
        expected_aligned['patient_id'] = ['sample_id_1', 'sample_id_2']
        expected_aligned['L_1'] = ['Y', 'N']
        expected_aligned['L_2'] = ['N', 'Y']
        expected_aligned['R_1'] = ['N', 'Y']
        expected_aligned['R_2'] = ['Y', 'N']
        expected_aligned = expected_aligned[['L_1', 'L_2', 'R_1', 'R_2',
            'name_1', 'name_2', 'patient_id']]

        actual_aligned = align(test_labels)
        pd.testing.assert_frame_equal(expected_aligned, actual_aligned)

if __name__ == '__main__':
    unittest.main()
