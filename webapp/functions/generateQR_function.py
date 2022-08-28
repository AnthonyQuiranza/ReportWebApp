import qrcode

def generateQR(Name,Passport,Folio):
    qr = qrcode.QRCode(border=0)
    qr.add_data(f"{Name} {Passport} {Folio}")
    qr.make()
    img = qr.make_image()
    return img
