import numpy as np

class OVModel:
    def __init__(self, L, number_of_cars, c, a, dt):
        self.L = L
        self.number_of_cars = number_of_cars
        self.c = c
        self.a = a
        self.dt = dt
        self.cars_x = np.zeros(number_of_cars)
        self.cars_v = np.zeros(number_of_cars)
        self.init()

    def V(self, dx):
        return np.tanh(dx - self.c) + np.tanh(self.c)

    def init(self):
        dx = self.L / self.number_of_cars
        x = 0.0
        iv = self.V(dx)
        for i in range(self.number_of_cars):
            self.cars_x[i] = x
            self.cars_v[i] = iv
            x += dx
            x += (np.random.rand() - 0.5) * 0.01

    def step(self):
        for i in range(self.number_of_cars):
            if i != self.number_of_cars - 1:
                dx = self.cars_x[i + 1] - self.cars_x[i]
            else:
                dx = self.cars_x[0] - self.cars_x[i]
            if dx < 0.0: dx += self.L
            if dx > self.L: dx -= self.L

            self.cars_v[i] += self.a * (self.V(dx) - self.cars_v[i]) * self.dt
            self.cars_x[i] += self.cars_v[i] * self.dt
            if self.cars_x[i] > self.L:
                self.cars_x[i] -= self.L

    def get_positions(self):
        r = 0.4
        cx, cy = 0.5, 0.5
        theta = 2.0 * np.pi / self.L * self.cars_x
        x = r * np.cos(theta) + cx
        y = r * np.sin(theta) + cy
        return x, y
