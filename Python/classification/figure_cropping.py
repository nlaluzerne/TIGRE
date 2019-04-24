# -*- coding: utf-8 -*-
# =============================================================================
# Created by: Natalie LaLuzerne
# =============================================================================
import numpy as np
import csv
import os

def fig_crop(dirname, filename, left, right, top, bottom):

    # =========================================================================
    # convert arguments to correct types
    # =========================================================================
    dirname = str(dirname)
    filename = str(filename)
    left = int(left)
    right = int(right)
    top = int(top)
    bottom = int(bottom)
    
    # =========================================================================
    # check to make sure directory exists
    # =========================================================================
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    
    # =========================================================================
    # read in file
    # =========================================================================
    with open(dirname + "\\" + filename) as f:
        bins = list(csv.reader(f))
                
    bins = np.array(bins, dtype=float)
    
    # =========================================================================
    # Crop Matrices to area of interest
    # =========================================================================
    
    # crops horizontally (rows)
    bins = bins[top:bottom, :]
    
    # crops vertically (columns)
    bins = bins[:, left:right]
    
    # =========================================================================
    # Write cropped data to a csv
    # =========================================================================
    crop_filename = filename[:-4] + "_crop" + ".csv"
    
    with open( os.path.join( dirname, crop_filename ), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(bins)
      
    # =========================================================================
    # return directory name and file name of cropped csv
    # =========================================================================
    return( dirname, crop_filename)