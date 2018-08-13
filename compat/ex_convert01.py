#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018

    Demonstration of the compatibility module
"""

from geomdl import NURBS
from geomdl import utilities as utils
from geomdl import compatibility as compat

from geomdl.visualization import VisMPL


#
# The initial surface exported from your CAD software
#

# Control points in u-row order
p_size_u = 4
p_size_v = 3
p_ctrlpts = [[0, 0, 0], [1, 0, 6], [2, 0, 0], [3, 0, 0],
             [0, 1, 0], [1, 1, 0], [2, 1, 0], [3, 1, -3],
             [0, 2, -3], [1, 2, 0], [2, 2, 3], [3, 2, 0]]

# Weights of the control points
p_weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Degrees
p_degree_u = 3
p_degree_v = 2

#
# Prepare data for import
#

t_ctrlptsw = compat.combine_ctrlpts_weights(p_ctrlpts, p_weights)
n_ctrlptsw = compat.flip_ctrlpts_u(t_ctrlptsw, p_size_u, p_size_v)

# Since we have no information on knot vectors, let's auto-generate them
n_knotvector_u = utils.generate_knot_vector(p_degree_u, p_size_u)
n_knotvector_v = utils.generate_knot_vector(p_degree_v, p_size_v)


#
# Import surface to NURBS-Python
#

surf = NURBS.Surface()
surf.degree_u = p_degree_u
surf.degree_v = p_degree_v
surf.ctrlpts_size_u = p_size_u
surf.ctrlpts_size_v = p_size_v
surf.ctrlptsw = n_ctrlptsw
surf.knotvector_u = n_knotvector_u
surf.knotvector_v = n_knotvector_v

# Set evaluation delta
surf.delta = 0.05

# Set visualization component
vis_comp = VisMPL.VisSurfTriangle()
surf.vis = vis_comp

# Render the surface
surf.render()
