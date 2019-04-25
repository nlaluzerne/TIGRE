# -*- coding: utf-8 -*-
# =============================================================================
# Created by: Natalie LaLuzerne
# =============================================================================
import numpy as np
from scipy import stats

# =============================================================================
#   location defines the datatype to represent the location of the tumor 
# =============================================================================
class location:
    LEFT = -1
    RIGHT = 1
    NONE = 0
  
# =============================================================================
#   slope thresholds. derived from temperature_processing_investigation
#   slope falls under minSlopeThreshold: tumor on left
#   slope exceeds maxSlopeThreshold: tumor in right
#   slope within bounds of both thresholds: no tumor
# =============================================================================
minSlopeThreshold = -0.006495790
maxSlopeThreshold = 0.007409563
    
def temp_proc(bins):
    
    # =========================================================================
    #   initialize tumor location storage structure
    # =========================================================================
    locationList = []
    
    # =========================================================================
    #   Apply background filter
    # =========================================================================
    rowAvg = [np.mean(bins[rw]) for rw in range(bins.shape[0])]
    minAvg = min(rowAvg)
    idx = rowAvg.index(minAvg)
    std = np.std(bins[idx])  
    bins = np.array([[x if x >= (minAvg - (2 * std)) else 0 for x in y] for y in bins])
    
    # =========================================================================
    #   Analyze row by row each of the temperature profiles
    # ========================================================================= 
    for row in reversed(range(bins.shape[0])):
        # =====================================================================
        #   get the current row to analyze 
        # =====================================================================
        currentRow = np.array(bins[row])
        
        # =====================================================================
        #   calculate x and y coordinates of each temperature for y = mx + b
        # =====================================================================
        Y = [i for i in currentRow if i != 0]
        X = [i for i in range(len(Y))]
        
        # =====================================================================
        #   calculate slope
        # =====================================================================
        slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
        
        # =====================================================================
        #   compare slope to thresholds and store location estimate
        # =====================================================================
        if(slope > maxSlopeThreshold):
            locationList.append(location.RIGHT)
        elif(slope < minSlopeThreshold):
            locationList.append(location.LEFT)
        else:
            locationList.append(location.NONE)
     
    # =========================================================================
    #   sum the location values in the list, return diagnosis
    #   sum > 0: majority of slopes were positive, tumor on right
    #   sum < 0: majority of slopes were negative, tumor on left
    #   sum = 0: slopes were balanced, no tumor
    # =========================================================================
    SUM = np.sum(locationList)
    if(SUM > 0):
        return("RIGHT")
    elif(SUM < 0):
        return("LEFT")
    else:
        return("NONE")