import sys 
from math import sin, cos, pi, radians
from tail_recursion import recurse, tail_recursive





class projectile_calculations:
    
    # sys.setrecursionlimit(1000000000)
    trip_time = 0
    x_max = 0
    y_vals = list()
    def __init__(self, y_initial, velocity, delta_t, mass, diameter, C, theta):
        
        self.g = -9.81
        self.rho = 1.225
        self.y_initial = y_initial
        self.C = C
        self.velocity = velocity
        self.delta_t = delta_t
        self.mass = mass
        self.area = pi * (diameter / 2) ** 2
        self.theta = radians(theta)
        self.v_y = self.velocity * sin(theta)
        self.v_x = self.velocity * cos(theta)



    def drag(self, rho, C, diameter, velocity):
        area = pi * (diameter / 2) ** 2
        return rho * C * area * velocity**2 / 2

    def acceleration_p(self, acceleration, drag, v_p, velocity, mass):
        return acceleration - ((drag * v_p / velocity ) / mass)


    @tail_recursive
    def integration(
        self, position, velocity, acceleration, delta_t, mass, rho, area, C, v_y, time, y_vals
        ):
        if position >= 0:
            drag_force = self.drag(rho, C, area, velocity)
            a_y = self.acceleration_p(acceleration, drag_force, v_y, velocity, mass)
            v_new = v_y + a_y * delta_t
            v_avg = (v_y + v_new) / 2
            p_new = (position + v_avg * delta_t)    
            y_vals.append(p_new)
            v_tot_new = velocity - drag_force / mass * delta_t
            time += delta_t
            recurse(self, p_new, v_tot_new, acceleration, delta_t, mass, rho, area, C, v_new, time, y_vals)
        else:

            return time




    @tail_recursive
    def x_position(
        self, position, velocity, delta_t, mass, rho, area, C, v_x, time, counter
    ):
        if counter <= time :
            drag_force = self.drag(rho, C, area, velocity)
            a_x = self.acceleration_p(0, drag_force, v_x, velocity, mass)
            v_new = v_x + a_x * delta_t
            v_avg = (v_x + v_new) / 2
            p_new = (position + v_avg * delta_t)
            v_tot_new = velocity - drag_force / mass * delta_t
            counter += delta_t
            recurse(self, p_new, v_tot_new, delta_t, mass, rho, area, C, v_new, time, counter)

        else:
            return position


    def run(self):
        self.trip_time = projectile_calculations.integration(
             self, self.y_initial, self.velocity, self.g, self.delta_t, self.mass, self.rho, self.area, self.C, self.v_y, 0, projectile_calculations.y_vals)
        self.x_max = projectile_calculations.x_position(
             self, 0, self.velocity, self.delta_t, self.mass, self.rho, self.area, self.C, self.v_x, self.trip_time, 0)
        self.y_max = max(projectile_calculations.y_vals)

        return f" The trip time is {self.trip_time}, The range is {self.x_max}, The maximum hight is {self.y_max}"
        
        
        