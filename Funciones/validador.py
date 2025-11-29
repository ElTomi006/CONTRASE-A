caracteres = "!-*/_.,+"
numeros = "1234567890"



def _validación_de_caracteres(contraseñA: str) -> bool:
    numeros_ = any(c in numeros for c in contraseñA)
    caracteres_ = any(c in caracteres for c in contraseñA)
    letras_ = any(c.isalpha() for c in contraseñA)
    if numeros_ and caracteres_ and letras_: 
        return True
    
def _validacion_de_correo(Correo: str) -> bool:
    return "@gmail" in Correo and ".com" in Correo
        


   
       
      
    
    