from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

status_data = {
    "contoh": {"Jarak": 0.0},
    "kelompok_1": {"Jarak": 0.0},
    "kelompok_2": {"Jarak": 0.0},
    "kelompok_3": {"Jarak": 0.0},
    "kelompok_4": {"Jarak": 0.0},
    "kelompok_5": {"Jarak": 0.0},
    "kelompok_6": {"Jarak": 0.0},
}

def index(request):
    return render(request, 'index.html', {"status": status_data})

def get_status(request, group):
    if group in status_data:
        return JsonResponse(status_data[group])
    return JsonResponse({"success": False, "message": f"Group {group} not found"}, status=404)

@csrf_exempt
def update_status(request, group):
    if request.method == "POST":
        if group in status_data:
            try:
                data = json.loads(request.body)
                status_data[group].update(data)
                return JsonResponse({"success": True, "message": f"Status of {group} updated"})
            except Exception as e:
                return JsonResponse({"success": False, "error": str(e)})
        return JsonResponse({"success": False, "message": f"Group {group} not found"}, status=404)
    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)
