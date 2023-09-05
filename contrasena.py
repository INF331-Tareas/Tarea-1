import secrets
import string

def generador():

    print("Ingrese tamaño de la contraseña (entre 6 y 16): ")
    t = int(input())

    if(t <= 6 or t >= 16):

        return("Tamano no valido")
    
    else:
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation

        alphabet = letters + digits + special_chars

        tamano_contrasena = t

        contrasena = ''
        for i in range(tamano_contrasena):
            contrasena += ''.join(secrets.choice(alphabet))

        return(contrasena)
