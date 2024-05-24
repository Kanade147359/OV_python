# python_ov_model/app.py

from flask import Flask, render_template, jsonify 
import numpy as np

app = Flask(__name__)

L = 40.0
number_of_cars = 20
cars_x = np.zeros(number_of_cars)
cars_v = np.zeros(number_of_cars)
c = 2.0
a = 1.0
dt = 0.005

def V(dx):
    return np.tanh(dx - c) + np.tanh(c)

def init():
    global cars_x, cars_v
    dx = L / number_of_cars
    x = 0.0
    iv = V(dx)
    for i in range(number_of_cars):
        cars_x[i] = x
        cars_v[i] = iv
        x += dx
        x += (np.random.rand() - 0.5) * 0.01

def step():
    global cars_x, cars_v
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

@app.route('/')
def index():
    init()
    return render_template('index.html')

@app.route('/step')
def update_step():
    step()
    return jsonify(cars_x=cars_x.tolist(), cars_v=cars_v.tolist())

if __name__ == '__main__':
    app.run(debug=True)
