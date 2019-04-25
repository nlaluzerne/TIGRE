# -*- coding: utf-8 -*-
# =============================================================================
# Created by: Natalie LaLuzerne
# =============================================================================
#import pylab as plt
import os
import numpy as np
import csv
from scipy import stats

class location:
    LEFT = -1
    RIGHT = 1
    NONE = 0

dirname = r"C:\Users\nlalu\Documents\EECS_581\All_Crops"

filenames = os.listdir(dirname)

frontFaceID = "BA-fc"

filenames = [file for file in filenames if frontFaceID in file]

testfilenames = ["CasSal240909A2BA-fc.csv", "FloFra080409A2BA-fc.csv", "GalMar040810A2BA-fc.csv", "GarCyn071012A2BA-fc.csv"]

minSlopeThreshold = -0.006495790
maxSlopeThreshold = 0.007409563

slopeList = [[] for _ in range(len(filenames))]

locationList = [[] for _ in range(len(filenames))]

imageDiagnosis = []
# =============================================================================
#   Read in files  
#   Loop through files to get all front-facing matrices
# =============================================================================
itr = 0
for file in filenames:
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
    bins = np.array([[x if x >= (minAvg - (2 * std)) else 0 for x in y] for y in bins])
    
# =============================================================================
#     Analyze row by row each of the temperature profiles
# =============================================================================  
    for row in reversed(range(bins.shape[0])):
        currentRow = np.array(bins[row])
        
        Y = [i for i in currentRow if i != 0]
        X = [i for i in range(len(Y))]
        
        slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
        slopeList[itr].append(slope)
        
        if(slope > maxSlopeThreshold):
            locationList[itr].append(location.RIGHT)
        elif(slope < minSlopeThreshold):
            locationList[itr].append(location.LEFT)
        else:
            locationList[itr].append(location.NONE)
        
# =============================================================================
#     cropBins = [bins[a] for a in range(len(locationList[itr])) if locationList[itr][a] != 0]
#     
#     plt.figure()
#     plt.plot(locationList[itr])
#     
#     plt.figure()
#     plt.imshow(cropBins, cmap='jet', vmin=28, vmax=36)
# =============================================================================
    SUM = np.sum(locationList[itr])
    if(SUM > 0):
        imageDiagnosis.append([file, "RIGHT"])
    elif(SUM < 0):
        imageDiagnosis.append([file, "LEFT"])
    else:
        imageDiagnosis.append([file, "NONE"])
    
    itr += 1
    
with open( r'C:\Users\nlalu\Documents\EECS_581\diagnoses.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(imageDiagnosis)

