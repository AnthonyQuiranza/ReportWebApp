from http.client import HTTPResponse
from django.utils import timezone
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from webapp.models import Report
from webapp.forms import *
from webapp.functions.verificationCode import *
from django.contrib import messages #import messages

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
            post.appointmen_date = timezone.now()
            post.is_authorized = False
            post.folio = f'EP{gen_folio_code()}'
            post.verification_code = gen_verification_code()
            post.save()
            return HttpResponseRedirect('/activacion')
    else:
        form = ReportForm()
    return render(request,'registro-cuenta.html',{'form': form})