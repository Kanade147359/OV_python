
import numpy as np

L = 40.0
C = 2.0

def V(dx):
    return np.tanh(dx - C) + np.tanh(C)

def init(number_of_cars, cars_x, cars_v):
    dx = L / number_of_cars
    x = 0.0
    iv = V(dx)
    for i in range(number_of_cars):
        cars_x[i] = x
        cars_v[i] = iv
        x += dx
        x += (np.random.rand() - 0.5) * 0.01

def step(number_of_cars, a , dt, cars_x, cars_v):
    for i in range(number_of_cars):
        if i != number_of_cars - 1:
            dx = cars_x[i + 1] - cars_x[i]
        else:
            dx = cars_x[0] - cars_x[i]
        if dx < 0.0:
            dx += L
        if dx > L:
            dx -= L

        cars_v[i] += a * (V(dx) - cars_v[i]) * dt
        cars_x[i] += cars_v[i] * dt
        if cars_x[i] > L:
            cars_x[i] -= L
        
def show_cars(t,number_of_cars,cars_x):
    for i in range(number_of_cars):
        print(f"{t} {cars_x[i]}")
        
def main():
    number_of_cars = 20
    cars_x = np.zeros(number_of_cars)
    cars_v = np.zeros(number_of_cars)
    a = 1.0
    dt = 0.005

    init(number_of_cars, cars_x, cars_v)

    for i in range(100000):
        t = i * dt
        step(number_of_cars, a, dt, cars_x, cars_v)
        show_cars(t, number_of_cars, cars_x)

    

if __name__ == '__main__':
    main()
