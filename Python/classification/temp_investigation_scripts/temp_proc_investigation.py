# -*- coding: utf-8 -*-
# =============================================================================
# Created by: Natalie LaLuzerne
# =============================================================================
import pylab as plt
import os
import numpy as np
import csv
from scipy import stats
from itertools import zip_longest

dirname = r"C:\Users\nlalu\Documents\EECS_581\Cancer_Free"

filenames = os.listdir(dirname)

frontFaceID = "BA-f"

filenames = [file for file in filenames if frontFaceID in file]

testfilenames = ["PenGua110113A2BA-fc.csv"]

fitThreshold = 0.006

slopeList = [[] for _ in range(len(filenames))]

minModel = []

maxModel = []

outlierList = []
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
# =============================================================================
#         plt.figure(figsize=(15,7))
#         plt.subplot(1,2,1)
#         plt.imshow(bins, cmap='jet', vmin=28, vmax=36)
#         plt.colorbar()
# =============================================================================
        
        currentRow = np.array(bins[row])
# =============================================================================
#         rowLine = np.array([row for i in range(len(currentRow))])
#         plt.plot(rowLine, 'k')
#         
#         plt.subplot(1,2,2)
#         plt.plot(currentRow)
# =============================================================================
        
        Y = [i for i in currentRow if i != 0]
        
        X = [i for i in range(len(Y))]
        
        slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
        
        if slope > fitThreshold or slope < -fitThreshold:
            outlierList.append(itr)
            break
        
        slopeList[itr].append(slope)
        
    itr += 1
    
for x in outlierList:
    slopeList[x] = np.nan

slopeList = [x for x in slopeList if not np.isnan(x).any()]

transposeSlopeList = [*zip_longest(*slopeList)]

transposeSlopeList = [list(a) for a in transposeSlopeList]

transposeSlopeList = [[c for c in a if c != None] for a in transposeSlopeList]

freeFit = [np.mean(b) for b in transposeSlopeList]

minFit = [m - fitThreshold for m in freeFit]

max_minFitVal = np.min(minFit[:-50])

minModel = [max_minFitVal for _ in range(375)]

maxFit = [m + fitThreshold for m in freeFit]

max_maxFitVal = np.max(maxFit)

maxModel = [max_maxFitVal for _ in range(375)]

print("Min = " +  str(max_minFitVal))
print("Max = " +  str(max_maxFitVal))
        
plt.figure(figsize=(10,7))

###############################################################################

dirname = r"C:\Users\nlalu\Documents\EECS_581\Cancer_Right"

filenames = os.listdir(dirname)

frontFaceID = "BA-f"

filenames = [file for file in filenames if frontFaceID in file]

testfilenames = ["PenGua110113A2BA-fc.csv"]

slopeList = [[] for _ in range(len(filenames))]

outlierList = []
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
        
    itr += 1
    
for p in range(len(slopeList)):
    plt.plot(slopeList[p], c='r')
    
###############################################################################

dirname = r"C:\Users\nlalu\Documents\EECS_581\Cancer_Left"

filenames = os.listdir(dirname)

frontFaceID = "BA-f"

filenames = [file for file in filenames if frontFaceID in file]

testfilenames = ["PenGua110113A2BA-fc.csv"]

slopeList = [[] for _ in range(len(filenames))]

outlierList = []
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
        
    itr += 1
    
for p in range(len(slopeList)):
    plt.plot(slopeList[p], c='g')
    
###############################################################################

dirname = r"C:\Users\nlalu\Documents\EECS_581\Cancer_Free"

filenames = os.listdir(dirname)

frontFaceID = "BA-f"

filenames = [file for file in filenames if frontFaceID in file]

testfilenames = ["PenGua110113A2BA-fc.csv"]

slopeList = [[] for _ in range(len(filenames))]

outlierList = []
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
        
    itr += 1
    
for p in range(len(slopeList)):
    plt.plot(slopeList[p], c='b')
plt.plot(freeFit, c='k')
plt.plot(minFit, c='k')
plt.plot(maxFit, c='k')
plt.plot(minModel, c='y')
plt.plot(maxModel, c='y')
plt.title("Slopes")
plt.xlabel("Row Number (bottom of image is Row 0)")
plt.ylabel("Slope")
