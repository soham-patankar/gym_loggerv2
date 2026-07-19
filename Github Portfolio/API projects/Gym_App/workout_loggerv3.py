import sqlite3
from datetime import date
import requests

DATABASE= "workouts.db"

def init_db():
    connection= sqlite3.connect(DATABASE)
    cursor=connection.cursor()
    
    #WORKOUTS TABLE
    cursor.execute("""CREATE TABLE IF NOT EXISTS workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_name TEXT,
    workout_date TEXT
    )""")

    #EXERCISES TABLE
    cursor.execute("""CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_id INTEGER,
    exercise TEXT,
    sets INTEGER,
    reps INTEGER,
    weight REAL,
    FOREIGN KEY (workout_id) REFERENCES workouts(id)
    )""")


    connection.commit()
    connection.close()

def main_menu():
   init_db()
   while True:
    print("===MAIN MENU===")
    print("1.)---View Workout---")
    print("2.)---Add Workout---")
    print("3.)---Delete Workout---")
    print("4.)---HERE TO EXIT---")
    try: 
     choice=int(input("Enter the option: "))
     if choice==1:
        view_workouts()
     elif choice==2:
        add_workouts()
     elif choice==3:
        delete_workouts()
     elif choice==4:
        exit()   
    except ValueError:
       print("Enter an integer: ")   

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter an Integer: ")     

def fetch_exercises(muscle_group):
    API_KEY = "ehT3yOKKqPbW4afFzLhwOMoqu1KBb0WcoOpnR5Fj"
    url = f"https://api.api-ninjas.com/v1/exercises?muscle={muscle_group}"
    headers = {"X-Api-Key": API_KEY}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if not data:
            return None
        for i, exercise in enumerate(data):
            print(f"{i+1}. {exercise['name']}")
        choice = int(input("Pick a number: "))
        return data[choice - 1]["name"]
    else:
        print(f"API error: {response.status_code}")
        return None              

def add_workouts():
    connection= sqlite3.connect(DATABASE)
    cursor=connection.cursor()
    workout_name=str(input("Enter the name of workout: "))
    workout_date=str(input("Enter the workout date: "))
    if not workout_date:
       workout_date=str(date.today())
    cursor.execute("""INSERT INTO workouts(workout_name,workout_date) VALUES(?,?)""",(workout_name,workout_date))  
    workout_id=cursor.lastrowid 
    while True:   
      muscle_group=str(input("Enter the muscle group: ")).strip()
      exercise=fetch_exercises(muscle_group)
      if exercise is None:
        print("Please Enter Valid Muscle Group: ")
        continue
      sets=get_int("Enter the number of sets: ")
      reps=get_int("Enter the number of reps: ")
      weight=get_int("Enter the total weight lifted in kg: ")   
      cursor.execute("""INSERT INTO exercises(workout_id,exercise,sets,reps,weight) VALUES(?,?,?,?,?)""",(workout_id,exercise,sets,reps,weight))
      again=str(input("Do you want to add another exercise in the workout (Y/N)?"))
      if again.upper()=="N":
        break
    connection.commit()
    connection.close()


def view_workouts():
    connection=sqlite3.connect(DATABASE)
    cursor=connection.cursor()
    cursor.execute("""SELECT * from workouts""")
    results=cursor.fetchall()
    for row in results:
        print(f"[{row[0]}] {row[1]}")
    connection.close()    
    if results:
       wid=int(input("Enter the workout ID to be viewed"))
       if wid!=0:
          view_exercises(wid)

def view_exercises(workout_id):
    connection=sqlite3.connect(DATABASE)
    cursor=connection.cursor()
    cursor.execute("SELECT * from exercises WHERE workout_id=?",(workout_id,))
    reveal=cursor.fetchall()
    for row in reveal:
       print(f"[{row[0]}][{row[1]}]{row[2]} of {row[3]} sets for {row[4]} reps at {row[5]}kg")
    connection.close()   

def delete_workouts():
    connection=sqlite3.connect(DATABASE)    
    cursor=connection.cursor()
    while True:
      wid=get_int("Enter the ID to be deleted: ")
      cursor.execute("SELECT id from workouts WHERE id=?",(wid,))
      result=cursor.fetchone()
      if result is None:
        print("Please enter a valid ID: ")
      else:
        cursor.execute("DELETE from workouts WHERE id=?",(wid,))
        connection.commit()
        print(f"The workout {wid} has been deleted...")
        break     
    connection.close()

if __name__=="__main__":main_menu()