# -*- coding: utf-8 -*-
# =============================================================================
# Created by: Natalie LaLuzerne
# =============================================================================
import pylab as plt
import numpy as np
import csv
import os

# =============================================================================
# change these directories to point to where the existing files live and
# where the new ones will be written to
# =============================================================================
read_dirname = r"C:\Users\nlalu\Documents\EECS_581\Temps_Cancer"
write_dirname = r"C:\Users\nlalu\Documents\EECS_581\Temps_Cancer_Crop"

if not os.path.exists(write_dirname):
    os.makedirs(write_dirname)

# =============================================================================
# Change this to the file you want to crop
# =============================================================================
filename = "CasSal240909A2BA-fc.csv"

# =============================================================================
# read in file
# =============================================================================
with open(read_dirname + "\\" + filename) as f:
    bins = list(csv.reader(f))
            
bins = np.array(bins, dtype=float)

# =============================================================================
# Crop Matrices to area of interest
# =============================================================================

# crops horizontally (rows)
bins = bins[85:230, :]

# crops vertically (columns)
bins = bins[:, 48:275]

plt.figure()
plt.imshow(bins, vmin=25, vmax=38, cmap='jet')
plt.colorbar()
plt.title(filename)

# =============================================================================
# Write cropped data to a csv
# =============================================================================
with open( os.path.join( write_dirname, filename ), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(bins)
    
    
 