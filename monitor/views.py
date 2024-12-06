from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

status_data = {
    "Suhu": 0.0,  # Suhu dalam derajat Celsius
    "Gas": 0,  # Nilai gas dalam rentang 0-1023
    "Gas_Indikasi": "Bersih",  # Indikasi gas
    "Hujan": "Tidak",  # Hujan bisa 'Ya' atau 'Tidak'
    "Pintu": "Lock",  # Pintu bisa 'Lock' atau 'Unlock'
    "Kipas": "Off",  # Kipas bisa 'On' atau 'Off'
    "Lampu": "Off",  # Lampu bisa 'On' atau 'Off'
    "Buzzer": "Off",  # Lampu bisa 'On' atau 'Off'
}

def index(request):
    return render(request, 'index.html', {"status": status_data})

def get_status(request):
    return JsonResponse(status_data)

@csrf_exempt
def update_status(request):
    global status_data
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            status_data.update(data)
            return JsonResponse({"success": True, "message": "Status updated"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "message": "Invalid request"})
