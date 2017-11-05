# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2017
"""
from geomdl import CPGen

# Generate a 50x100 rectangle
mygrid = CPGen.GridWeighted(50, 100)

# Split the width into 5 equal pieces and the height into 10 equal pieces
mygrid.generate(5, 10)

# Generate 4 bumps on the grid
mygrid.bumps(4)

# Add weight
mygrid.add_weight(2.3)

# Modify weight
mygrid.modify_weight(1.0)

# Save the file, by default as grid.txt
mygrid.save()

# Get the grid points for plotting
grid_data = mygrid.grid()

# Good to have something here to put a breakpoint
pass
