#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""

import os
from geomdl import exchange
from geomdl.visualization import VisPlotly as vis


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Read a directory containing smesh files
multi_smesh = exchange.import_smesh('data')
multi_smesh.sample_size = 5

# Draw the control point grid and the evaluated surface
vis_config = vis.VisConfig(ctrlpts=False, legend=False)
vis_comp = vis.VisSurface(vis_config)
multi_smesh.vis = vis_comp
multi_smesh.render()

# Save MultiSurface as a .obj file
exchange.export_obj(multi_smesh, "multisurface01.obj")

# Good to have something here to put a breakpoint
pass
