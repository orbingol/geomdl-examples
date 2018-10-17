# ex_curve02.m
# Tested on Octave 4.2.2 with nurbs 1.3.13

# Housekeeping
clear all;

# Load "nurbs" package (install it via "pkg install -forge nurbs")
pkg load nurbs

# Control points and knot vectors for a 3rd degree curve
ctrlpts = [05 10 20 35 45 50; 05 20 35 35 20 05];
kv = [0.0, 0.0, 0.0, 0.0, 0.333333, 0.666667, 1.0, 1.0, 1.0, 1.0];

# Generate the NURBS curve
crv = nrbmak(ctrlpts, kv);

# Compute the 1st and 2nd derivative curves
[ders1, ders2] = nrbderiv(crv);

# Evaluate the derivatives
t = 0.2;
[p1, dp1] = nrbdeval(crv, ders1, t);
[p2, dp2] = nrbdeval(crv, ders2, t);

# Normalize derivative vectors
dp1n = vecnorm(dp1);
dp2n = vecnorm(dp2);

# Display output
fprintf('1st derivative vector: %s\n', sprintf('%f ', dp1n))
fprintf('2nd derivative vector: %s\n', sprintf('%f ', dp2n))
