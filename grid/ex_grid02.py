#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2017
"""
import os
from geomdl import CPGen

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Generate a 50x100 rectangle
mygrid = CPGen.GridWeighted(50, 100)

# Split the width into 5 equal pieces and the height into 10 equal pieces
mygrid.generate(15, 20)

# Generate 4 bumps on the grid
mygrid.bumps(num_bumps=4, bump_height=50)

# Add weight
mygrid.weight = 2.3

# Modify weight
mygrid.weight = 1.0

# Get the grid points for plotting
grid_data = mygrid.grid

# Good to have something here to put a breakpoint
pass
