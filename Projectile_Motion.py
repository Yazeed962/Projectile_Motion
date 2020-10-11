

# RUN RECURSIVELY UNTIL Y = 0

import json
from math import radians
from Projectile.util import projectile_calculations




with open("Projectile\\data.json") as f:
    data = json.load(f)


simulation = projectile_calculations(data["Y_INITIAL"], data["V_INITIAL"], data["DELTA_T"], data["MASS"], data["DIAMETER"], data["C"], data["THETA"])

results = simulation.run()


print(results)
