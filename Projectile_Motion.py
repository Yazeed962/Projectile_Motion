"""
Data: 
angle = pi/4
Drag coefficient = .30
Initial velocity = 15 m/s
mass = 2 kg
radius = .2 meter
initial hight = 0
DENSITY = 1.225
"""

# RECURSIVELY UNTIL Y = 0

import json
from math import sin, cos, pi, radians
from Projectile.util import projectile_calculations




with open("Projectile\\data.json") as f:
    data = json.load(f)

THETA= radians(data["THETA"])
V_INITIAL = data["V_INITIAL"]
MASS = data["MASS"]
DIAMETER = data["DIAMETER"]
DENSITY = data["DENSITY"]
Y_INITIAL = data["Y_INITIAL"]
DELTA_T = data["DELTA_T"]
C = data["C"]

ob = projectile_calculations(Y_INITIAL, V_INITIAL, DELTA_T, MASS, DIAMETER, C, THETA)

X = ob.run()


print(X)
