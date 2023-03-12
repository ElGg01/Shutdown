from os import system

minutos = int(input("Introduce los minutos para apagar la PC: "))
segundos = minutos * 60

system("shutdown -s -t " + str(segundos))

print("El sistema se apagara en: " + str(minutos) + " minutos")