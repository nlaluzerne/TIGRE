# -*- coding: utf-8 -*-
# =============================================================================
# Created by: Natalie LaLuzerne
# =============================================================================
import pylab as plt
import os
import numpy as np
import csv

dirname = r"C:\Users\nlalu\Documents\EECS_581\All_Crops"

dirname2 = r"C:\Users\nlalu\Documents\EECS_581\Heat_Maps"

filenames = os.listdir(dirname)

frontFaceID = "BA-f"

filenames = [file for file in filenames if frontFaceID in file]

testfilenames = ["AlaCoi101209A2BA-f.csv"]
thresh = 1
# =============================================================================
#   Read in files  
#   Loop through files to get all front-facing matrices
# =============================================================================
for file in testfilenames:
    with open(dirname + "\\" + file) as f:
        bins = list(csv.reader(f))
                
    bins = np.array(bins, dtype=float)
    
    # =========================================================================
    # Apply background filter
    # =========================================================================
    
    rowAvg = [np.mean(bins[rw]) for rw in range(bins.shape[0])]
    
    minAvg = min(rowAvg)
    
    idx = rowAvg.index(minAvg)
    
    std = np.std(bins[idx])
    
    bins = np.array([[x if x >= (minAvg - (thresh*std)) else 0 for x in y] for y in bins])
    
    bins[bins == 0] = np.nan
    
    # =========================================================================
    # generate Heat Map
    # =========================================================================
    
    plt.figure()
    plt.imshow(bins, cmap='seismic')
    plt.colorbar()
    plt.title(file)
    plt.savefig(dirname2 + "\\" + file[:-4] + ".jpg")
    plt.close()
