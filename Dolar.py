n = int(input("Ingrese el número de días: "))
if n <= 0:
     print("sin ningun dia, no habra alzas")
else:
    precioDolares = []
    for i in range(n):
        precioDolar = float(input(f"Ingrese el precio del dólar dia: {i+1}: "))
        precioDolares.append(precioDolar)
    alzas = []
    for i in range(n-1):
        alza = precioDolares[i+1] - precioDolares[i]
        alzas.append(alza)
    mayorAlza = max(alzas)
print(f"La mayor alza fue de {mayorAlza}.")
if mayorAlza == 0:
    print(f"No hubo alzas")