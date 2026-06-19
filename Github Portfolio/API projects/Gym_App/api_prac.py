from flask import Flask
from workout_loggerv2 import load_workouts

app = Flask(__name__)

@app.route('/workouts')
def get_workouts():
    workouts=load_workouts()
    return workouts

if __name__ == '__main__':
    app.run(debug=True)
