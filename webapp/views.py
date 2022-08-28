from datetime import datetime
from django.utils import timezone
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from webapp.models import Report
from webapp.forms import ValidationForm,ReportForm
from webapp.functions.verificationCode import gen_folio_code,gen_verification_code
from django.contrib import messages #import messages
from webapp.functions.mail_function import send_mail
from webapp.functions.generateText_function import generateText
def index(request):
    return render(request,'index.html')

def activacion(request):
    if request.method=="POST":
        form = ValidationForm(request.POST)
        if form.is_valid():
            if Report.objects.filter(verification_code=request.POST.get('code')):
                print("existe el dato")
                messages.success(request, 'Se ha comprobado su código de verificación, recibirá su cita en su correo cuando esté aprobada')
            else:
                print("No se encontro el dato")
                messages.error(request,"El código de verificación que ha ingresado es incorrecto, por favor verifique y vuelva a intentarlo.")
    else:
        form = ValidationForm()
    return render(request, 'activacion.html',{'form':form})

def registro_cuenta(request):
    
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.is_authorized = False
            
            post.folio = f'EP{gen_folio_code()}'
            post.verification_code = gen_verification_code()
            post.pdf_url=generateText(f'{post.name} {post.last_name}',post.folio,post.appointment_date,post.appointment_hour,post.passport)
            send_mail(f'{post.name} {post.last_name}',post.email,post.verification_code)
            post.save()
            return HttpResponseRedirect('/activacion')
    else:
        form = ReportForm()
    return render(request,'registro-cuenta.html',{'form': form})