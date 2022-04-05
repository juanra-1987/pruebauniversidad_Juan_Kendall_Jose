import os
os.system("cls")


paises = {
"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", 
"Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", 
"Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", 
"Venezuela": "Caracas", "España": "Madrid"
}

pais = str(input (" digite el país:   ")).title()


if pais in paises:
    print (f"la capital del país {pais}", "es  ",paises[pais])
else:
    print ("El país digitado no esta dentro de la lista")

# if pais == paises.values():
#     print (f"la capital del país {pais} es:", paises[pais])

# if pais in paises:
#     print(paises.get(pais))