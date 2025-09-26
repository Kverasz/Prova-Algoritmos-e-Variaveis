tempo = int(input("Quantos meses tem seu tempo de serviço?: "))
fgts = int(input("Qual o valor do FGTS?: "))

if tempo > 12:
    multa = (fgts*40)/100
    print(f"Sua multa ficou no valor de: {multa}")
else:
    print("A multa não é aplicável.")