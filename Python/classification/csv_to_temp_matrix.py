# -*- coding: utf-8 -*-
# =============================================================================
# Created by: Natalie LaLuzerne
# =============================================================================
import csv
import numpy as np

def convert_csv(filepath):
    with open(filepath) as f:
        bins = list(csv.reader(f))
                
    bins = np.array(bins, dtype=float)
    
    return(bins)