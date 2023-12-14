precios = {'A': 270, 'B': 340, 'C': 390}
monedas = []
while True:
    producto = input("Seleccione el producto (A, B o C): ")
    if producto in precios:
        precio = precios[producto]
        break
    else:
        print("Producto inválido. Intente de nuevo.")
while True:
    moneda = int(input("Ingrese una moneda (10, 50 o 100): "))
    if moneda in [10, 50, 100]:
        monedas.append(moneda)
        total = sum(monedas)
        if total >= precio:
            break
    else:
        print("Moneda inválida. Intente de nuevo.")
monedasVuelto = sorted([100, 50, 10], reverse=True)
print("\nMonedas de vuelto:")
total -= precio
for moneda in monedasVuelto:
    while total >= moneda:
        print(f"Moneda de ${moneda}")
        total -= moneda