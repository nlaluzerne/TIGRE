import os
import random
import assignments
import pandas as pd

all_patients = list(os.listdir('Volunteers, fpf-files')) + list(os.listdir('MdC, cancer_fpf-files'))
all_team_members = ['Andrew', 'Carter', 'Hunter', 'Natalie', 'Niels']
random.shuffle(all_patients)
random.shuffle(all_team_members)

single = assignments.assign(all_team_members, all_patients)
double = assignments.augment_assignment(single)

if assignments.distinct(double):
  print('Assignments are distinct')

ass_df = assignments.dict_to_df(double, 'name', 'patient_id')

ass_df.to_csv('assignments.csv', index=False)
