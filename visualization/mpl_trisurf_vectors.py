# -*- coding: utf-8 -*-

"""
    Visualization Examples for the NURBS-Python Package
    Released under The MIT License
    Developed by Onur Rauf Bingol (c) 2018

    Creates a triangulated surface and plots tangent and normal vectors

    Colors: https://xkcd.com/color/rgb/
"""

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl import exchange
from geomdl import operations

import numpy as np
import matplotlib
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set degrees
surf.degree_u = 3
surf.degree_v = 3

# Set control points
surf.set_ctrlpts(*exchange.import_txt("../surface/ex_surface02.cpt", two_dimensional=True))

surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, 6)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, 6)

# Set evaluation delta
surf.delta = 0.05

# Evaluate surface
surf.evaluate()

# Evaluate surface tangent and normal vectors
uv_vals = [[0.1, 0.1], [0.65, 0.25], [0.9, 0.7], [0.2, 0.9]]
surftans = [[] for _ in range(len(uv_vals))]
surfnorms = [[] for _ in range(len(uv_vals))]

for idx, uv in enumerate(uv_vals):
    surftans[idx] = operations.tangent(surf, uv, normalize=True)
    surfnorms[idx] = operations.normal(surf, uv, normalize=True)

# Prepare points for plotting
surfpts = np.array(surf.evalpts)
tangent_vectors = np.array(surftans)
normal_vectors = np.array(surfnorms)

# Start plotting of the surface and the control points grid
fig = plt.figure(figsize=(10.67, 8), dpi=96)
ax = Axes3D(fig)

# Plot surface points
ax.plot_trisurf(surfpts[:, 0], surfpts[:, 1], surfpts[:, 2], color='xkcd:gold', alpha=0.5)

# Plot tangent vectors (u-dir)
ax.quiver(tangent_vectors[:, 0, 0], tangent_vectors[:, 0, 1], tangent_vectors[:, 0, 2],
          tangent_vectors[:, 1, 0], tangent_vectors[:, 1, 1], tangent_vectors[:, 1, 2],
          color='xkcd:bright blue', length=5)

# Plot tangent vectors (v-dir)
ax.quiver(tangent_vectors[:, 0, 0], tangent_vectors[:, 0, 1], tangent_vectors[:, 0, 2],
          tangent_vectors[:, 2, 0], tangent_vectors[:, 2, 1], tangent_vectors[:, 2, 2],
          color='xkcd:neon green', length=5)

# Plot normal vectors
ax.quiver(normal_vectors[:, 0, 0], normal_vectors[:, 0, 1], normal_vectors[:, 0, 2],
          normal_vectors[:, 1, 0], normal_vectors[:, 1, 1], normal_vectors[:, 1, 2],
          color='xkcd:bright red', length=3)

# Add legend to 3D plot, @ref: https://stackoverflow.com/a/20505720
surface_prx = matplotlib.lines.Line2D([0], [0], linestyle='none', color='xkcd:gold', marker='^')
tanu_prx = matplotlib.lines.Line2D([0], [0], linestyle='none', color='xkcd:bright blue', marker='>')
tanv_prx = matplotlib.lines.Line2D([0], [0], linestyle='none', color='xkcd:neon green', marker='>')
normal_prx = matplotlib.lines.Line2D([0], [0], linestyle='none', color='xkcd:bright red', marker='>')
ax.legend([surface_prx, tanu_prx, tanv_prx, normal_prx],
          ['Surface Plot', 'Tangent Vectors (u-dir)', 'Tangent Vectors (v-dir)', 'Normal Vectors'],
          numpoints=1)

# Rotate the axes and update the plot
for angle in range(0, 360, 10):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)

# Display the final 3D plot
plt.show()
