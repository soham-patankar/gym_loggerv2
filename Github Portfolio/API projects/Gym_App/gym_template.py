import json
import os
from datetime import date
import requests 

DATA_FILE = "workouts.json"


def load_workouts():# TASK 1 — load_workouts()
    if not os.path.exists(DATA_FILE):# This function should:
       print("No workouts logged yet") # - Check if the file DATA_FILE exists (use os.path.exists)
       return []# - If it doesn't exist, return an empty list []
    else:
       with open(DATA_FILE,"r") as f: # - If it does, open the file and return the contents using json.load()
            return json.load(f)

def save_workouts(workouts):# TASK 2 — save_workouts(workouts)
    with open(DATA_FILE,"w") as f:# This function should:
         json.dump(workouts,f,indent=2)# - Open DATA_FILE in write mode
# - Write the workouts list to it using json.dump()
# - Add indent=2 so the file is readable

def fetch_exercises(muscle_group):
    API_KEY = "eV1kaA1DnfPeMjuwxqu2LIclcIX1KYvSw9GMs22c"  # replace with your actual key
    url = f"https://api.api-ninjas.com/v1/exercises?muscle={muscle_group}"
    headers = {"X-Api-Key": API_KEY}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        if not data:
            print("No exercises found for that muscle group.")
            return None
        
        for i, exercise in enumerate(data):
            print(f"{i+1}. {exercise['name']}")
        
        choice = int(input("Pick a number: "))
        return data[choice - 1]["name"]
    else:
        print(f"API error: {response.status_code}")
        return None
    

def add_workouts(workouts):# TASK 3 — add_workout(workouts)
    workout_date=str(input("Enter the date of the workout ").strip())# This function should:
    if not workout_date:# - Ask the user for: date, exercise name, sets, reps, weight
       workout_date=str(date.today())# - If date is blank, use str(date.today()) instead
    muscle_group=input("Enter the muscle you want to train \nChest/Shoulders/Triceps/Lats/Biceps/Forearms/Quadriceps/Hamstrings/Calves: \n").strip()# - Build a dict with keys: id, date, exercise, sets, reps, weight
    exercise=fetch_exercises(muscle_group)
    sets=int(input("Enter the number of sets "))# - id = len(workouts) + 1
    reps=int(input("Enter the number of reps "))# - Append the dict to workouts
    weight=float(input("Enter the total weight (kg) "))# - Call save_workouts() to persist it
    id=len(workouts)+1# - Print a confirmation message
    workout={
           "id":id,
           "workout_date":workout_date,
           "exercise":exercise,
           "sets":sets,
           "reps":reps,
           "weight":weight
    }
    workouts.append(workout)
    save_workouts(workouts)
    print("Workout added successfully")

def view_workouts(workouts):# TASK 4 — view_workouts(workouts)
    if len(workouts)<1:# This function should:
       print("No workouts has been logged yet")# - If workouts is empty, print "No workouts logged yet." and return
    else:# - Otherwise loop through workouts and print each one
       for w in workouts:# - Format: [id]  date  |  exercise  |  SetsxReps @ weightkg
           print(f'{w["id"]} {w["exercise"]} {w["sets"]} sets for {w["reps"]} reps @ {w["weight"]}kg on {w["workout_date"]}')

def delete_workouts(workouts):# TASK 5 — delete_workout(workouts)
    view_workouts(workouts)# This function should:
    wid=int(input("Enter the Id to delete the specific workout "))# - Call view_workouts() so the user can see the IDs
    workouts[:] = [w for w in workouts if w["id"] != wid]# - Ask the user which ID to delete
    save_workouts(workouts)# - Remove that workout from the list (hint: list comprehension)
    print("The workout has been deleted successfully")# - Call save_workouts() to persist the change
# - Print a confirmation


def main_menu():# TASK 6 — main()
    workouts=load_workouts()# This function should:
    while True:# - Call load_workouts() once and store the result
        print("--Select the option--")# - Show a menu in a while True loop: Add / View / Delete / Quit
        print("1. Add workout")# - Call the right function based on the user's choice
        print("2.View workout")# - Break the loop when the user picks Quit
        print("3.Delete workout")
        print("4.Exit")
        choice=int(input("Enter the option: "))    
        if  choice==1:
            add_workouts(workouts)
        elif choice==2:
            view_workouts(workouts)
        elif choice==3:
            delete_workouts(workouts)
        elif choice==4:
            break
        else:
            print("Wrong Input")               

if __name__=="__main__":# TASK 7 — entry point
   main_menu()# Only call main() if this file is being run directly
# (not imported by another file)

    
