N=int(input("Inserte numero de baterias de SAI: "))
V=int(input("Inserte voltaje de las baterias: "))
A=int(input("Inserte los Amperios Hora de las baterias: "))
E=float(input("Inserte Eficiencia del SAI: "))
Va=int(input("Volti-Amperios del SAI:"))
def ups(N,V,A,E,VA):
    resultado=((N*V*A*E)/VA)*60
    return resultado
print(ups(N,V,A,E,Va))

