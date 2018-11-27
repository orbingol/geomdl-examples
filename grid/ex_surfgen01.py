#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under the MIT License
    Developed by Onur Rauf Bingol (c) 2018

    This example illustrates the following operations:

    * Generating a control points grid
    * Generating a B-Spline surface and using the generated grid as its control points input
    * Splitting the B-Spline surface
    * Plotting the split surface using Plotly
"""


from geomdl import BSpline
from geomdl import CPGen
from geomdl import utilities
from geomdl import operations
from geomdl.visualization import VisPlotly

# Generate a control points grid
surfgrid = CPGen.Grid(50, 100)

# This will generate a 32x32 grid
surfgrid.generate(32, 32)

# Generate bumps on the grid
surfgrid.bumps(num_bumps=4, all_positive=True, bump_height=45, base_extent=4, base_adjust=1)

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set degrees
surf.degree_u = 3
surf.degree_v = 3

# Get the control points from the generated grid
surf.ctrlpts2d = surfgrid.grid

# Set knot vectors
surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, surf.ctrlpts_size_u)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, surf.ctrlpts_size_v)

# Split the surface at v = 0.35
split_surf = operations.split_surface_v(surf, 0.35)

# Set sample size of the split surface
split_surf.sample_size = 25

# Generate the visualization component and its configuration
vis_config = VisPlotly.VisConfig(ctrlpts=False, legend=False)
vis_comp = VisPlotly.VisSurface(vis_config)

# Set visualization component of the split surface
split_surf.vis = vis_comp

# Plot the split surface
split_surf.render()

# Good to have something here to put a breakpoint
pass
