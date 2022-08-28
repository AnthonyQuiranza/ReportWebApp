import fitz as pymupdf
import os
from reportapp.settings import BASE_DIR
from webapp.functions.generateQR_function import generateQR

def generateText(Name,Folio,DateString,Hour,Passport):
    Folio = f'{Folio}'
    Hour = f'{Hour}'
    Hour = f'{Hour[:-3]} Hrs'
    pdf= './webapp/static/files/Visa.pdf'
    f= pymupdf.open(pdf)
    page = f.load_page(0)
    page.insert_font(fontname="Arial", fontfile="./webapp/static/files/fonts/arial.ttf")
    page.insert_font(fontname="Arial-bold", fontfile="./webapp/static/files/fonts/arial-bold.ttf")
    positionName= pymupdf.Point(90,131)
    page.insert_text(positionName,Name, fontsize=10, fontname = "Arial")
    positionFolio= pymupdf.Point(90,119)
    page.insert_text(positionFolio,Folio, fontsize=10, fontname = "Arial")
    positionName2= pymupdf.Point(180,255)
    page.insert_text(positionName2,Name, fontsize=9, fontname = "Arial")
    positionFolio2= pymupdf.Point(180,268)
    page.insert_text(positionFolio2,Folio, fontsize=9, fontname = "Arial-bold")
    positionDate= pymupdf.Point(180,280)
    page.insert_text(positionDate,f'{DateString}', fontsize=9, fontname = "Arial-bold")
    positionHour= pymupdf.Point(180,292)
    page.insert_text(positionHour,Hour, fontsize=9, fontname = "Arial-bold")
    positionPassport= pymupdf.Point(180,304)
    page.insert_text(positionPassport,Passport, fontsize=9, fontname = "Arial-bold")
    QR = generateQR(Name,Passport,Folio)
    QR.save(f"./webapp/static/files/qr/{Name}.png")
    page.insert_image(rect=(110, 583, 180, 651),filename=f"./webapp/static/files/qr/{Name}.png", keep_proportion=True, overlay=True)
    f.write()
    f.save(f"./webapp/static/files/documents/confirmacion_tramite _{Name}.pdf")
    url = f"http://127.0.0.1:8000/static/files/documents/confirmacion_tramite _{Name}.pdf"
    url= url.replace("","%")
    return url
    
