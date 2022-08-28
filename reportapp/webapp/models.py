from pyexpat import model
from django.db import models

class Report(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default="")
    passport = models.CharField(max_length=10)
    email = models.EmailField(default="alexquiranza@gmail.com")
    folio = models.CharField(max_length=20)
    appointment_date = models.DateField()
    appointment_hour = models.TimeField()
    is_authorized = models.BooleanField()
    verification_code = models.CharField(max_length=40, default="")
    pdf_url = models.URLField(default="https://citascuba.reprogramacion-gob.mx/")
    def save(self):
        if self.is_authorized == True:
            print(f"Esta activado para {self.name}")
        else:
            print(f"No esta activado para {self.name}")
        self.save_base()

    
        