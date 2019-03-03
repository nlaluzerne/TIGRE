# -*- coding: utf-8 -*-
# =============================================================================
# Created by: Natalie LaLuzerne
# =============================================================================
import pylab as plt
import os
import numpy as np
import csv

dirname = r"C:\Users\nlalu\Documents\EECS_581\Temps_Cancer"

filenames = os.listdir(dirname)

frontFaceID = "BA-f"

filenames = [file for file in filenames if frontFaceID in file]

testfilenames = ["CasSal240909A2BA-fc.csv"]

# =============================================================================
#   Read in files  
#   Loop through files to get all front-facing matrices
# =============================================================================

for file in testfilenames:
    with open(dirname + "\\" + file) as f:
        bins = list(csv.reader(f))
                
    bins = np.array(bins, dtype=float)
    
    # =============================================================================
    # Apply background filter
    # =============================================================================
    
    rowAvg = [np.mean(bins[rw]) for rw in range(bins.shape[0])]
    
    minAvg = min(rowAvg)
    
    idx = rowAvg.index(minAvg)
    
    std = np.std(bins[idx])
    
    bins = np.array([[x if x >= (minAvg - std) else 0 for x in y] for y in bins])
    
    
    bins[bins == 0] = np.nan
     
    sides = np.split(bins,2,1)
     
    leftSide = sides[0]
    rightSide = sides[1]
     
    leftSideAvg = np.nanmean(leftSide)
    rightSideAvg = np.nanmean(rightSide)
 
    plt.figure()
    plt.imshow(bins, vmin=25, vmax=38, cmap='jet')
    plt.colorbar()
    plt.title(file)
    
    for row in reversed(range(bins.shape[0])):
        currentRow = np.array(bins[row])
        
        w = len(currentRow) // 2
        
        left = w - 1
        
        if(w % 2 == 0):
            right = w
        else:
            right = w + 1

    