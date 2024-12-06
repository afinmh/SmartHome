from django.apps import AppConfig
import threading
import time
from django.db import OperationalError

class YourAppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monitor'

    def save_status_to_db(self):
        from .models import SmartHomeStatus
        from .views import status_data

        while True:
            try:

                SmartHomeStatus.objects.create(
                    suhu=status_data["Suhu"],
                    gas=status_data["Gas"],
                    gas_indikasi=status_data["Gas_Indikasi"],
                    hujan=status_data["Hujan"],
                    pintu=status_data["Pintu"],
                    kipas=status_data["Kipas"],
                    lampu=status_data["Lampu"],
                    buzzer=status_data["Buzzer"]
                )
                print("Data saved to database")
            except OperationalError as e:
                print(f"Database not ready: {e}")
            except Exception as e:
                print(f"Error saving to database: {e}")

            time.sleep(10)

    def ready(self):
        thread = threading.Thread(target=self.save_status_to_db, daemon=True)
        thread.start()
