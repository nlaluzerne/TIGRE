# -*- coding: utf-8 -*-
# =============================================================================
# Created by: Natalie LaLuzerne
# =============================================================================
import pylab as plt
import os
import numpy as np
import csv

dirname = r"C:\Users\nlalu\Documents\EECS_581\All_Crops"

dirname2 = r"C:\Users\nlalu\Documents\EECS_581"

filenames = os.listdir(dirname)

frontFaceID = "BA-f"

filenames = [file for file in filenames if frontFaceID in file]

classfilename = "classifications.csv"

testfilenames = ["CasSal240909A2BA-fc.csv"]

testclss = [['CasSal240909', 'N', 'Y']]

nmlAvgs = []
freeAvgs = []

with open(dirname2 + "\\" + classfilename) as f:
    clss = list(csv.reader(f))
    
clss = [lst for lst in clss for _ in (0, 1)]

# =============================================================================
#   Read in files  
#   Loop through files to get all front-facing matrices
# =============================================================================
it = 0
for file in filenames:
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
    
    bins = np.array([[x if x >= (minAvg - std) else 0 for x in y] for y in bins])
    
    bins[bins == 0] = np.nan
    
    # =========================================================================
    # Calculate average temeperature of left and right side
    # =========================================================================
     
    sides = np.array_split(bins,2,1)
     
    leftSide = sides[0]
    rightSide = sides[1]
     
    leftSideAvg = np.nanmean(leftSide)
    rightSideAvg = np.nanmean(rightSide)
    
    # =========================================================================
    # Normalize the averages
    # =========================================================================
    
    if clss[it][0] in file:
        if clss[it][1] == 'N' and clss[it][2] == 'Y':
            nAvg = rightSideAvg / leftSideAvg
            nmlAvgs.append(nAvg)
            freeAvgs.append(leftSideAvg)
               
        elif clss[it][1] =='Y' and clss[it][2] == 'N':
            nAvg = leftSideAvg / rightSideAvg
            nmlAvgs.append(nAvg)
            freeAvgs.append(rightSideAvg)
           
    it += 1
    
nmlAvg = np.nanmean(nmlAvgs)

nmlAvgLine = np.array([nmlAvg for _ in range(len(nmlAvgs))])

plt.figure()
plt.scatter(range(len(nmlAvgs)), nmlAvgs, c='b')
#plt.axis([0, 211, 5, 20])
plt.plot(nmlAvgLine, c='b')
plt.title("Normalized Avg Temp of Tumorous Vs. Non-Tumorous Breasts \n Avg temp = " + str(nmlAvg))
plt.xlabel("Sample #")
plt.ylabel("Normalized Avg Temperature of Tumorous Breasts (deg C)")

plt.figure()
plt.hist(nmlAvgs)
plt.title("Normalized Avg Temperature of Tumorous Breasts (deg C)")
plt.xlabel("Temperature")
plt.ylabel("Samples")

# =============================================================================
#     plt.figure()
#     plt.imshow(bins, cmap='jet')
#     plt.colorbar()
#     plt.title(file)
#     
#     plt.figure()
#     plt.imshow(leftSide, cmap='jet')
#     plt.colorbar()
#     plt.title(file)
#     
#     plt.figure()
#     plt.imshow(rightSide, cmap='jet')
#     plt.colorbar()
#     plt.title(file)
#     
#     print("left side avg = " + str(leftSideAvg))
#     print("right side avg = " + str(rightSideAvg))
# =============================================================================
    
    

    