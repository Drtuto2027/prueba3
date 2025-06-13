#definimos un diccionario
persona={"nombre": "lucia", "edad":29,"ciudad":"cali"}
#iteramos sobre las claves y valores del diccionario
for clave,valor in persona.items():
    print(f"{clave.capitalize()}:{valor}")