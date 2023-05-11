from django.shortcuts import render

def calcular(request):
    if request.method == 'POST':
        cant_serv = int(request.POST.get('servidor'))
        serv=cant_serv*1000
        cant_switch = int(request.POST.get('switch'))
        switches=cant_switch*500
        cant_ventiladores = int(request.POST.get('ventiladores'))
        ventiladores=cant_ventiladores*1000
        Fact = 0.8
        
        resultado = (serv+switches+ventiladores)* Fact

        return render(request, 'resultado.html', {'resultado': resultado})

    return render(request, 'calcular.html')