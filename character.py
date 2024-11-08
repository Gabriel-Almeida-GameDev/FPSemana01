x=0

while x==0:
    Dragao = [str(input("Nome da Personagem 1: ")), int(input("Vida da Personagem 1: ")), int(input("Nivel da Personagem 1: "))]
    Phoenix = [str(input("Nome da Personagem 2: ")), int(input("Vida da Personagem 2: ")), int(input("Nivel da Personagem 2: "))]
    Unicornio = [str(input("Nome da Personagem 3: ")), int(input("Vida da Personagem 3: ")), int(input("Nivel da Personagem 3: "))]
    break
else: print("invalid")

array = [
    [Dragao, Phoenix, Unicornio]
]

print (array)

if Dragao[2] > Phoenix[2] > Unicornio[2]:
    print(Dragao[0])
    print(Phoenix[0])
    print(Unicornio[0])

elif Dragao[2] > Unicornio[2] > Phoenix[2]:
    print(Dragao[0])
    print(Unicornio[0])
    print(Phoenix[0])

elif Phoenix[2] > Unicornio[2] > Dragao[2]:
    print(Phoenix[0])
    print(Unicornio[0])
    print(Dragao[0])

elif Phoenix[2] > Dragao[2] > Unicornio[2]:
    print(Phoenix[0])
    print(Dragao[0])
    print(Unicornio[0])

elif Unicornio[2] > Dragao[2] > Phoenix[2]:
    print(Unicornio[0])
    print(Dragao[0])
    print(Phoenix[0])

elif Unicornio[2] > Phoenix[2] > Dragao[2]:
    print(Unicornio[0])
    print(Phoenix[0])
    print(Dragao[0])

else:
    print("Some of these values are equal. Cannot compute.")