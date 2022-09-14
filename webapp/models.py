from pyexpat import model
from statistics import mode
from django.db import models
from webapp.functions.mail_function import send_pdf
from webapp.functions.generateText_function import generateText
from webapp.functions.verificationCode import gen_folio_code
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
        dia = self.appointment_date.day
        mes = self.appointment_date.month
        anio = f'{self.appointment_date.year}'
        hora = f'{self.appointment_hour}'
        print(hora)
        print(f'La hora es:{hora[0:2]} ')
        print(f'Los minutos son: {hora[3:5]}')
        folio= f'EP{dia}{mes}{anio[2:4]}{hora[0:2]}{hora[3:5]}{gen_folio_code()}'
        if self.is_authorized == True:
            print(f"Esta activado para {self.name}")
            self.folio = folio
            try:
                self.pdf_url=generateText(f'{self.name} {self.last_name}',folio,self.appointment_date,self.appointment_hour,self.passport)
                send_pdf(f"{self.name} {self.last_name}",f'{self.email}',f'{self.pdf_url}')
            except:
                print("Ha ocurrido un error")
        else:
            print(f"No esta activado para {self.name}")
        self.save_base()

    
        
