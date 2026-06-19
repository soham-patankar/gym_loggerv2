import json
import os
import requests
from datetime import date

DATAFILE="workouts.json"

def load_workouts():
    if not os.path.exists(DATAFILE):
        print("No workout logged yet")
        return []
    else:
        with open(DATAFILE,'r') as f:
            return json.load(f)

workouts=load_workouts()
print(workouts)            