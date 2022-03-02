from xml.dom.minidom import CharacterData


print("Ola, mundo")
print("Olá, José Henrique")
print(1+2)

hrs = int(input("Digite que horas são:"))
print("São ",hrs, " horas.")
min = int(input("Digite quantos minutos são:"))
print("São {} minutos".format(min))

num = int(input("Digite um número: "))
if num == 0:
    print("Você digitou 0!")
elif num < 0:
    print("Você digitou um número menor que zero!")
else:
    print("Você digitou um número maior que zero!")


