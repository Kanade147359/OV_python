from flask import Flask, render_template, jsonify
from model import OVModel

app = Flask(__name__)

L = 40.0
number_of_cars = 20
c = 2.0
a = 1.0
dt = 0.005
model = OVModel(L, number_of_cars, c, a, dt)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/step')
def step():
    model.step()
    x, y = model.get_positions()
    return jsonify({'x': x.tolist(), 'y': y.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
