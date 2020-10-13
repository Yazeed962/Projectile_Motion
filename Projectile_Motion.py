

# RUN RECURSIVELY UNTIL Y = 0

import json
from Projectile.util import projectile_calculations



def main():
    with open("Projectile\\data.json") as f:
        data = json.load(f)


    simulation = projectile_calculations(data["Y_INITIAL"], data["V_INITIAL"], data["DELTA_T"], data["MASS"], data["DIAMETER"], data["C"], data["THETA"])

    time, x_max, y_max = simulation.run()

    results = {
        "time":time,
        "x_max":x_max,
        "y_max":y_max
    }

    with open('results.json', 'w') as res:
        json.dump(results, res)

    print(f"""The trip time is {time} seconds
    The range is {x_max} meters
    The maximum hight is {y_max} meters""")

    if __name__ == '__main__':
        main()
