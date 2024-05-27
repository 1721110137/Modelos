import base64

def imagen_a_base64(ruta_imagen):
    with open(ruta_imagen, "rb") as imagen:
        imagen_bytes = imagen.read()
        imagen_base64 = base64.b64encode(imagen_bytes)
        return imagen_base64.decode('utf-8')

# Uso del código
ruta_imagen = 'assets/smile.png'  # Cambia esta ruta a la ruta de tu imagen
base64_string = imagen_a_base64(ruta_imagen)
print(base64_string)
