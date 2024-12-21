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

def generate_random_data():
    return {"Jarak": round(random.uniform(0.0, 100.0), 2)}

group_name = "kelompok_3"
while True:
    data = generate_random_data()
    update_data(group_name, data)
    time.sleep(1)
