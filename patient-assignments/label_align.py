import pandas as pd
from collections import defaultdict

def align(df):
    out_dict = defaultdict(list)
    for patient_name, group in df.groupby('patient_id'):
        out_dict['patient_id'].append(patient_name)
        L_1, L_2 = group['L']
        R_1, R_2 = group['R']
        name_1, name_2 = group['name']
        out_dict['L_1'].append(L_1)
        out_dict['L_2'].append(L_2)
        out_dict['R_1'].append(R_1)
        out_dict['R_2'].append(R_2)
        out_dict['name_1'].append(name_1)
        out_dict['name_2'].append(name_2)
    return pd.DataFrame(out_dict).reset_index(drop=True)
