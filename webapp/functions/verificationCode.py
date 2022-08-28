import random
import string
## Genera rápidamente letras y números aleatorios
code_str = string.ascii_letters + string.digits
 ## Imprime letras y números generados aleatoriamente
 ## Imprime 4 letras o números aleatorios
def gen_verification_code(len=40):
         ## Tome 4 letras y números aleatorios generados aleatoriamente y empalme en un código de inserción de 4 dígitos
    return ''.join(random.sample(code_str,len))
def gen_folio_code():
     return random.randint(100000000000000000,999999999999999999)