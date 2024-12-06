import requests
import json
import random
import time

# URL endpoint API Django
url = "http://localhost:8000/update_status"  # Ganti dengan URL API Anda

# Header untuk request
headers = {"Content-Type": "application/json"}

# Opsi untuk data random
pintu_options = ["Lock", "Unlock"]
lampu_options = ["On", "Off"]

# Fungsi untuk mengirim data random
def send_random_data():
    while True:
        for _ in range(10):  # Mengirimkan 10 kali per detik
            # Buat data acak
            gas_value = random.randint(0, 1023)  # Nilai gas acak antara 0-1023
            suhu_value = round(random.uniform(10.0, 30.0), 2)  # Suhu acak antara 10-30 derajat Celsius
            
            # Tentukan status kipas berdasarkan suhu
            kipas_status = "On" if suhu_value > 20 else "Off"  # Kipas On jika suhu > 20
            hujan_status = "Hujan" if suhu_value < 15 else "Tidak",
            
            data = {
                "Suhu": suhu_value,  # Suhu acak
                "Gas": gas_value,  # Nilai gas acak antara 0-1023
                "Gas_Indikasi": "Bersih" if gas_value <= 700 else "Kotor",  # Tentukan indikasi gas
                "Hujan": hujan_status,
                "Pintu": random.choice(pintu_options),  # Status pintu acak (Lock/Unlock)
                "Kipas": kipas_status,  # Status kipas (On/Off)
                "Lampu": random.choice(lampu_options),  # Status lampu acak (On/Off)
                "Buzzer": "Off" if gas_value <= 700 else "On"
            }

            try:
                # Kirim request POST ke API Django
                response = requests.post(url, headers=headers, data=json.dumps(data))
                print(f"Data sent: {data}")
                print(f"Response: {response.status_code}, {response.json()}")
            except Exception as e:
                print(f"Error: {e}")
            
            # Tunggu sebentar agar totalnya mencapai 10 kali dalam satu detik
            time.sleep(0.1)  # Delay 0.1 detik untuk 10 kali per detik

# Jalankan fungsi
if __name__ == "__main__":
    send_random_data()
