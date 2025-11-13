evento = int(input("Informe em segundos o tempo do evento: "))

horas = evento // 3600
evento = evento % 3600

minutos = evento // 60
segundos = evento % 60


print(f"{horas}:{minutos}:{segundos}")