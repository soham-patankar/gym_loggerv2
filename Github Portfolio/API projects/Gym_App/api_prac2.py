# TASK 1 — imports
from flask import Flask, request, jsonify# You need: Flask, request, jsonify from flask
from workout_loggerv2 import load_workouts, save_workouts# Also import load_workouts and save_workouts from workout_logger_v2

# TASK 2 — create the Flask app
app = Flask(__name__)# Same as before: app = Flask(__name__)

@app.route('/workouts',methods=['GET'])# TASK 3 — GET /workouts
def get_workouts():# - Load workouts using load_workouts()
    workouts=load_workouts()# - Return them
    return workouts

@app.route('/workout',methods=['POST'])# TASK 4 — POST /workout
def add_workouts():
   new_workout=request.get_json()# - Read the incoming data using request.get_json()
   workouts=load_workouts()# - Load existing workouts
   workouts.append(new_workout)# - Append the new one
   save_workouts(workouts)# - Save
   return {"message": "Workout added"}# - Return {"message": "Workout added"}

@app.route('/workout/<int:wid>', methods=['DELETE'])# TASK 5 — DELETE /workout/<int:wid>
def delete_workouts(wid):# - Load workouts
    workouts=load_workouts()
    workouts[:]=[w for w in workouts if w['id']!=wid]# - Filter out the one with matching id (you already know how)
    save_workouts(workouts)# - Save
    return {"message": f"Workout {wid} deleted"}# - Return {"message": f"Workout {wid} deleted"}

# TASK 6 — run the app
if __name__ == '__main__':
    app.run(debug=True)