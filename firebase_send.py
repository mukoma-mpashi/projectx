import firebase_admin
from firebase_admin import credentials, db
import random
import time


cred = credentials.Certificate("account.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://school-project-bf6af-default-rtdb.firebaseio.com/'
})


ref = db.reference('/system')


def initialize_database_structure():
    initial_structure = {
        "mode": "grid",
        "grid": {
            "voltage": 0.0,
            "current": 0.0,
            "power": 0.0,
            "unitsConsumed": 0.0
        },
        "solar": {
            "voltage": 0.0,
            "current": 0.0,
            "power": 0.0,
            "unitsConsumed": 0.0
        }
    }
    ref.set(initial_structure)
    print("Initialized database structure.")


def simulate_data_upload():
    while True:
        
        grid_data = {
            "voltage": round(random.uniform(210, 230), 2),
            "current": round(random.uniform(5, 10), 2),
            "power": round(random.uniform(1000, 2200), 2),
            "unitsConsumed": round(random.uniform(50, 200), 2)
        }
        
        solar_data = {
            "voltage": round(random.uniform(15, 20), 2),
            "current": round(random.uniform(1, 5), 2),
            "power": round(random.uniform(100, 500), 2),
            "unitsConsumed": round(random.uniform(10, 50), 2)
        }
    
        ref.update({
            "grid": grid_data,
            "solar": solar_data
        })

        print(f"Updated database with grid data: {grid_data}")
        print(f"Updated database with solar data: {solar_data}")

        # Wait for 5 seconds before sending the next batch of data
        time.sleep(5)

if __name__ == "__main__":
    initialize_database_structure()
    simulate_data_upload()
