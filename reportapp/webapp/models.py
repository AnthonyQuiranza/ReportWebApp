from django.db import models

class Report(models.Model):
    name = models.CharField(max_length=100)
    passport = models.CharField(max_length=10)
    folio = models.CharField(max_length=20)
    appointment_date = models.DateField(auto_now=True)
    appointment_hour = models.DateTimeField()
    is_authorized = models.BooleanField()

