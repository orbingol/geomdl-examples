#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""

import os
from geomdl import exchange
from geomdl import multi
from geomdl.visualization import VisPlotly as vis


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Read a directory containing mesh files
data = exchange.import_smesh('data')

# Generate a surface container for visualization
multi_mesh = multi.SurfaceContainer(data)
multi_mesh.sample_size = 5

# Draw the control point grid and the evaluated surface
vis_config = vis.VisConfig(ctrlpts=False, legend=False)
vis_comp = vis.VisSurface(vis_config)
multi_mesh.vis = vis_comp
multi_mesh.render()

# Save surfaces as a .obj file
exchange.export_obj(multi_mesh, "multisurface01.obj")

# Good to have something here to put a breakpoint
pass
