#variable tipo fotante
saldo=100.0
#sumulamos un ciclo de retiros de saldo para que el saldo sea menor que 10
while saldo>10:
    retiro=15.0
    saldo-=retiro
    print(f"sea retirado{retiro}, saldo actual:{saldo}")