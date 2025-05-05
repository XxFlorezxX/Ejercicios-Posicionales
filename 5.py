monto = float(input("Ingrese el monto total de su compra: $"))
if monto >= 200:
    descuento = monto * 0.20
elif monto >= 100:
    descuento = monto * 0.10
else:
    descuento = 0
monto_final = monto - descuento
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Monto final a pagar: ${monto_final:.2f}")
