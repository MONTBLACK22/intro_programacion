nombre = input("Ingresa tu nombre: ")

x = int(input("Ingresa tu año de nacimiento: "))

y = 2024-x

a = "los Niños de la Posguerra."




if y > 94:
    print('Hola',nombre,"envejeces como el vino..")
elif y >= 76:
    print('Hola',nombre,"tienes",y,"años y perteneces a los Niños de la Posguerra.")
elif y >= 56:
     print('Hola',nombre,"tienes",y,"años y perteneces a los Baby Boomer.")
elif y >= 44:
     print('Hola',nombre,"tienes",y,"años y perteneces a la Generación X.")
elif y >= 31:
     print('Hola',nombre,"tienes",y,"años y perteneces a los Milennials.")
elif y >= 14:
     print('Hola',nombre,"tienes",y,"años y perteneces a la Generazión Z.")
elif y >= 0:
     print('Hola',nombre,"tienes",y,"años y perteneces a la Generazión Alfa.")
else:
    print('Hola',nombre,"¿eres del futuro?")