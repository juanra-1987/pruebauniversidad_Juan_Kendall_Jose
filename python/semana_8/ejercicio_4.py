import os

os.system ("cls")

lista = ["Ronald","Steven","Juan"]

for i in lista:
    print("usted comienza con una R",i.startswith("R"))
if i.startswith("Ronald"):
    print("Si comienzo con una R")
else:
    print("No comienzo con una R")