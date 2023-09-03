from flask import Flask, render_template, request, jsonify
from helpers.water_jug_solver import WaterJugSolver

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        try:
            x = request.form.get('x', type=int)
            y = request.form.get('y', type=int)
            z = request.form.get('z', type=int)

            if x == None or y == None or z == None:
                raise TypeError()
            
            solverInstance = WaterJugSolver(x, y, z)
            solution = solverInstance.solver()
            return render_template('index.html', solution=solution)
        except TypeError as e:
            error = "Values sent must be integer"
            return render_template('index.html', error=error)
    else:
        return render_template('index.html', solution=None)
    
@app.route('/api', methods=['GET'])
def api():
    try:
        args = request.args
        x = args.get('x', type=int)
        y = args.get('y', type=int)
        z = args.get('z', type=int)
        if x == None or y == None or z == None:
            raise TypeError()
        solverInstance = WaterJugSolver(x, y, z)
        solution = solverInstance.solver()
        if len(solution) == 0:
            solution = "No Solution."
        return jsonify(
            parameters={
                "x": x,
                "y": y,
                "z": z
            },
            solution=solution
        )
    except TypeError as e:
        error = "Values sent must be integer"
        return jsonify(
            error=error
        )