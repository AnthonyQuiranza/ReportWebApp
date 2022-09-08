from pyexpat import model
from statistics import mode
from django.db import models
from webapp.functions.mail_function import send_pdf
from webapp.functions.generateText_function import generateText
class Report(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default="")
    passport = models.CharField(max_length=10)
    email = models.EmailField(default="alexquiranza@gmail.com")
    phone = models.CharField(max_length=20,default="00")
    folio = models.CharField(max_length=20)
    password = models.CharField(max_length=40, default="12345678")
    appointment_date = models.DateField()
    appointment_hour = models.TimeField()
    is_authorized = models.BooleanField()
    verification_code = models.CharField(max_length=40, default="")
    pdf_url = models.URLField(default="https://citascuba.reprogramacion-gob.mx/")
    def save(self):
        if self.is_authorized == True:
            print(f"Esta activado para {self.name}")
            try:
                self.pdf_url=generateText(f'{self.name} {self.last_name}',self.folio,self.appointment_date,self.appointment_hour,self.passport)
                send_pdf(f"{self.name} {self.last_name}",f'{self.email}',f'{self.pdf_url}')
            except:
                print("Ha ocurrido un error")
        else:
            print(f"No esta activado para {self.name}")
        self.save_base()

    
        
