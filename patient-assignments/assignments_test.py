import unittest
import assignments
import pandas as pd

class TestAssignments(unittest.TestCase):

  def test_distinct_assignments(self):
    self.assertTrue(assignments.distinct({'a': [1, 2], 'b': [1, 2]}))

  def test_non_distinct_assignments(self):
    self.assertFalse(assignments.distinct({'a': [1, 1], 'b': [1, 2]}))

  def test_partition(self):
    test_things = [1, 2]
    test_count = 1
    expected_partition = [[1, 2]]
    actual_partition = assignments.partition(test_things, test_count)
    self.assertEqual(expected_partition, actual_partition)

    test_things = [1, 2]
    test_count = 2
    expected_partition = [[1], [2]]
    actual_partition = assignments.partition(test_things, test_count)
    self.assertEqual(expected_partition, actual_partition)

    test_things = [1, 2, 3, 4]
    test_count = 2
    expected_partition = [[1, 2], [3, 4]]
    actual_partition = assignments.partition(test_things, test_count)
    self.assertEqual(expected_partition, actual_partition)

    test_things = [1, 2, 3, 4]
    test_count = 3
    expected_partition = [[1], [2], [3, 4]]
    actual_partition = assignments.partition(test_things, test_count)
    self.assertEqual(expected_partition, actual_partition)

  def test_assign_1_per(self):
    people = ['tom', 'jerry']
    things = ['cat', 'mouse', 'frog', 'chicken']
    result = assignments.assign(people, things)
    self.assertEqual({'tom': ['cat', 'mouse'], 'jerry': ['frog', 'chicken']}, result)

  def test_assign_2_per(self):
    people = ['tom', 'jerry']
    things = ['cat', 'mouse', 'frog', 'chicken']
    result = assignments.assign(people, things)
    result = assignments.augment_assignment(result)
    self.assertEqual({'tom': things, 'jerry': things[2:] + things[:2]}, result)

  def test_dict_to_df(self):
    test_dict = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
    expected_df = pd.DataFrame({'letter': ['a', 'a', 'b', 'b', 'c', 'c'], 'number': list(range(1, 7))})
    actual_df = assignments.dict_to_df(test_dict, key_name='letter', values_name='number')
    pd.testing.assert_frame_equal(expected_df, actual_df)

if __name__ == '__main__':
  unittest.main()

