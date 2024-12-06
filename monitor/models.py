from django.db import models

class SmartHomeStatus(models.Model):
    suhu = models.IntegerField()
    hujan = models.CharField(max_length=20)
    kipas = models.CharField(max_length=20)
    pintu = models.CharField(max_length=20)
    gas = models.IntegerField()
    gas_indikasi = models.CharField(max_length=20)
    lampu = models.CharField(max_length=20)
    buzzer = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Suhu: {self.suhu}, Gas: {self.gas}, Timestamp: {self.timestamp}"
