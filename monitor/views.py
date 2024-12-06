from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Data status yang di-update secara real-time
status_data = {
    "Suhu": 25.0,  # Suhu dalam derajat Celsius
    "Gas": 500,  # Nilai gas dalam rentang 0-1023
    "Gas_Indikasi": "Bersih",  # Indikasi gas
    "Hujan": "Tidak",  # Hujan bisa 'Ya' atau 'Tidak'
    "Pintu": "Lock",  # Pintu bisa 'Lock' atau 'Unlock'
    "Kipas": "Off",  # Kipas bisa 'On' atau 'Off'
    "Lampu": "Off",  # Lampu bisa 'On' atau 'Off'
    "Buzzer": "Off",  # Lampu bisa 'On' atau 'Off'
}

# Fungsi untuk menentukan indikasi gas berdasarkan nilai
def get_gas_indication(gas_value):
    if gas_value <= 700:
        return "Bersih"
    else:
        return "Kotor"

# Halaman utama
def index(request):
    return render(request, 'index.html', {"status": status_data})

# API untuk memberikan data real-time
def get_status(request):
    # Perbarui indikasi gas setiap kali status diminta
    status_data["Gas_Indikasi"] = get_gas_indication(status_data["Gas"])
    return JsonResponse(status_data)

@csrf_exempt
def update_status(request):
    global status_data
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            
            # Memperbarui data status berdasarkan input
            if "Gas" in data:
                # Jika ada update untuk gas, tentukan indikasi gas yang baru
                gas_value = data["Gas"]
                status_data["Gas_Indikasi"] = get_gas_indication(gas_value)
            
            status_data.update(data)
            return JsonResponse({"success": True, "message": "Status updated"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "message": "Invalid request"})
