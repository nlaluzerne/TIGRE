import pandas as pd

def distinct(assignments):
  for person, assignment in assignments.items():
    if len(assignment) != len(set(assignment)):
      return False
  return True

def partition(things, count):
  avg = len(things) / count
  out = []
  last = 0.0
  while last < len(things):
    out.append(things[int(last):int(last + avg)])
    last += avg
  return out
 
def assign(people, things):
  partitions = partition(things, len(people))
  return dict(zip(people, partitions))

def rotate(l, n):
  return l[n:] + l[:n]

def augment_assignment(a):
  people = list(a.keys())
  people_rotated = rotate(people, 1)
  people_pairs = zip(people, people_rotated)
  return dict((person, a[person] + a[person_r]) for (person, person_r) in people_pairs)
 
def dict_to_df(dictionary, key_name, values_name):
  dict_key_value_pairs = []
  for key, values in dictionary.items():
    for value in values:
      dict_key_value_pairs.append((key, value))
  keys, values = zip(*dict_key_value_pairs)
  out_df = pd.DataFrame()
  out_df[key_name] = keys
  out_df[values_name] = values
  return out_df.sort_values(key_name).reset_index(drop=True)
