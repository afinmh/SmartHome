import requests
import random
import time

api_url = "http://127.0.0.1:8000/update_status/"

def update_data(group_name, data):
    try:
        response = requests.post(f"{api_url}{group_name}/", json=data)
        if response.status_code == 200:
            result = response.json()
            if result.get("success"):
                print(f"Berhasil mengupdate {group_name}: {data}")
            else:
                print(f"Gagal mengupdate {group_name}: {result.get('message')}")
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Exception: {str(e)}")

def generate_random_data(group_name):
    """Generate random data with slight variation for each group."""
    if group_name == "contoh":
        return {"Jarak": round(random.uniform(0.0, 50.0), 2)}  # Contoh menghasilkan data di antara 0-50
    elif group_name == "kelompok_1":
        return {"Jarak": round(random.uniform(10.0, 60.0), 2)}  # Kelompok 1 menghasilkan data di antara 10-60
    elif group_name == "kelompok_2":
        return {"Jarak": round(random.uniform(20.0, 70.0), 2)}  # Kelompok 2 menghasilkan data di antara 20-70
    elif group_name == "kelompok_3":
        return {"Jarak": round(random.uniform(30.0, 80.0), 2)}  # Kelompok 3 menghasilkan data di antara 30-80
    elif group_name == "kelompok_4":
        return {"Jarak": round(random.uniform(40.0, 90.0), 2)}  # Kelompok 4 menghasilkan data di antara 40-90
    elif group_name == "kelompok_5":
        return {"Jarak": round(random.uniform(50.0, 100.0), 2)}  # Kelompok 5 menghasilkan data di antara 50-100
    elif group_name == "kelompok_6":
        return {"Jarak": round(random.uniform(60.0, 110.0), 2)}  # Kelompok 6 menghasilkan data di antara 60-110

groups = ["contoh", "kelompok_1", "kelompok_2", "kelompok_3", "kelompok_4", "kelompok_5", "kelompok_6"]

while True:
    for group_name in groups:
        data = generate_random_data(group_name)
        update_data(group_name, data)
    
    time.sleep(1)
