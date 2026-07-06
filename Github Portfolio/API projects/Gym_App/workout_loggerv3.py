import sqlite3
from datetime import date
from workout_loggerv2 import fetch_exercises

DATABASE= "workouts.db"

def init_db():
    connection= sqlite3.connect(DATABASE)
    cursor=connection.cursor()
    cursor.execute("""
          CREATE TABLE IF NOT EXISTS workouts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workout_date TEXT,
            exercise TEXT,
            sets INTEGER,
            reps INTEGER,
            weight REAL
          )       
    """)
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

def add_workouts():
    connection= sqlite3.connect(DATABASE)
    cursor=connection.cursor()
    workout_date=str(input("Enter the workout date: "))
    if not workout_date:
       workout_date=str(date.today())
    while True:   
      muscle_group=str(input("Enter the muscle group: ")).strip()
      exercise=fetch_exercises(muscle_group)
      if exercise is not None:
         break
      print("Please recheck and enter muscle name correctly")
    sets=get_int("Enter the number of sets: ")
    reps=get_int("Enter the number of reps: ")
    weight=get_int("Enter the total weight lifted in kg: ")   
    cursor.execute("""INSERT INTO workouts(workout_date,exercise,sets,reps,weight) VALUES(?,?,?,?,?)""",(workout_date,exercise,sets,reps,weight))
    connection.commit()
    connection.close()


def view_workouts():
    connection=sqlite3.connect(DATABASE)
    cursor=connection.cursor()
    cursor.execute("""SELECT * from workouts""")
    results=cursor.fetchall()
    for row in results:
        print(f"[{row[0]}] {row[2]} | {row[3]}x{row[4]} @ {row[5]}kg on {row[1]}")
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