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
#     Apply background filter
# =============================================================================
    
    rowAvg = [np.mean(bins[rw]) for rw in range(bins.shape[0])]
    
    minAvg = min(rowAvg)
    
    idx = rowAvg.index(minAvg)
    
    std = np.std(bins[idx])
    
    bins = np.array([[x if x >= (minAvg - std) else 0 for x in y] for y in bins])
    
# =============================================================================
#     Analyze row by row each of the temperature profiles
# =============================================================================
    
    for row in reversed(range(bins.shape[0])):
        plt.figure(figsize=(15,7))
        plt.subplot(1,2,1)
        plt.imshow(bins, vmin=25, vmax=38, cmap='jet')
        plt.colorbar()
        
        currentRow = np.array(bins[row])
        rowLine = np.array([row for i in range(len(currentRow))])
        plt.plot(rowLine, 'k')
        
        plt.subplot(1,2,2)
        plt.plot(currentRow)
        
        
    
    