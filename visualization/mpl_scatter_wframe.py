# -*- coding: utf-8 -*-

"""
    Visualization Examples for the NURBS-Python Package
    Released under The MIT License
    Developed by Onur Rauf Bingol (c) 2017

    Tested with:
    * Python v3.6.2
    * NumPy v1.13.3
    * Matplotlib v2.1.0
"""
import os
import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Read surface and control points, @ref: https://stackoverflow.com/a/13550615
cpgrid = np.genfromtxt('../surface/ctrlpts03_orig.csv', delimiter=',', skip_header=1, names=['x', 'y', 'z'])
surf = np.genfromtxt('../surface/surfpts03_orig.csv', delimiter=',', skip_header=1, names=['x', 'y', 'z'])

# Start plotting of the surface and the control points grid
fig = plt.figure(figsize=(10.67, 8), dpi=96)
ax = Axes3D(fig)

# Control points as a scatter plot (use mode='linear' while saving CSV file)
ax.scatter(cpgrid['x'], cpgrid['y'], cpgrid['z'], color='blue', s=50, depthshade=True)

# Surface points as a wireframe plot (use mode='wireframe' while saving CSV file)
ax.plot(surf['x'], surf['y'], surf['z'], color='green')

# Set axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(0, 1)

# Add legend to 3D plot, @ref: https://stackoverflow.com/a/20505720
plot1_proxy = matplotlib.lines.Line2D([0], [0], linestyle='none', color='blue', marker='o')
plot2_proxy = matplotlib.lines.Line2D([0], [0], linestyle='none', color='green', marker='o')
ax.legend([plot1_proxy, plot2_proxy], ['Control Points Grid', 'Surface Plot'], numpoints=1)

# Display the 3D plot
plt.show()
