from django.http import  HttpResponseRedirect
from django.shortcuts import render
from webapp.models import Report
from webapp.forms import ValidationForm,ReportForm,LoginForm
from webapp.functions.verificationCode import gen_folio_code,gen_verification_code
from django.contrib import messages #import messages
from webapp.functions.mail_function import send_mail
from webapp.functions.generateText_function import generateText
def index(request):
    exist_account=False
    exist_email = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            for i in Report.objects.values_list():
                if i[4] == request.POST.get('email') and i[8]==True:
                    print('Existe el correo y esta aprobado')
                    exist_account=True
                    messages.success(request,f'Hola {i[1]} {i[2]} su cita ha sido aprobada, por favor revise su correo.')
                elif i[4] == request.POST.get('email') and i[8]==False:
                    print('Existe el correo y NO ESTÁ APROBADO')
                    exist_email=True
                    messages.warning(request,f'Hola {i[1]} {i[2]} su cita aún no ha sido aprobada.')
                elif exist_account == False and exist_email == False :
                    messages.error(request,'No existe una cuenta asociada con los datos ingresados.')
    else:
        form = LoginForm()
    return render(request,'index.html', {'form':form})

def activacion(request):
    if request.method=="POST":
        form = ValidationForm(request.POST)
        if form.is_valid():
            if Report.objects.filter(verification_code=request.POST.get('code')):
                print("existe el dato")
                messages.success(request,'Se ha comprobado su código de verificación, recibirá su cita en su correo cuando esté aprobada')
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