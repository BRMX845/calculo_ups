from django.shortcuts import render

def calcular(request):
    if request.method == 'POST':
        cant_serv = int(request.POST.get('servidor'))
        serv=cant_serv*1000
        cant_switch = int(request.POST.get('switch'))
        switches=cant_switch*500
        cant_ventiladores = int(request.POST.get('ventiladores'))
        ventiladores=cant_ventiladores*1000
        cant_racks= int(request.POST.get('racks'))
        racks=cant_racks*1000
        cant_dmz = int(request.POST.get('dmz'))
        dmz=cant_dmz*1000
        cant_router = int(request.POST.get('router'))
        routers=cant_router*20
        cant_modem = int(request.POST.get('Modem'))
        modems=cant_modem*15
        cant_pbx = int(request.POST.get('pbx'))
        pbx=cant_pbx*150
        cant_monitores = int(request.POST.get('monitores'))
        monitores=cant_monitores*100
        cant_access= int(request.POST.get('access'))
        wifis=cant_access*15
        cant_computadoras = int(request.POST.get('computadoras'))
        pcs=cant_computadoras*250
        cant_sensor = int(request.POST.get('sensor'))
        sensores=cant_sensor*0.10
        cant_nas = int(request.POST.get('nas'))
        nas=cant_nas*150
        cant_puertas = int(request.POST.get('puertas'))
        puertas=cant_puertas*150

        Fact = 0.8
        
        res = (serv+switches+ventiladores+racks+dmz+routers+modems+pbx+monitores+wifis+pcs+sensores+nas+puertas)* Fact
        resultado=round(res,2)
        ups_eje=""
        url=""
        if resultado >=1000 and resultado<2000:
            ups_eje="puede usar un 220V - Winner Pro 2k"
            url="https://www.alibaba.com/product-detail/New-Product-2Kva-1-6Kw-2000Va_1600822274763.html?spm=a2700.7735675.0.0.21a7c7Ouc7OuPO&s=p"
        elif resultado >=2000 and resultado<3000:
            ups_eje="puede usar un 220V - Winner Pro 3k"
            url="https://www.alibaba.com/product-detail/New-Product-2Kva-1-6Kw-2000Va_1600822274763.html?spm=a2700.7735675.0.0.21a7c7Ouc7OuPO&s=p"
        
        return render(request, 'calcular.html', {'resultado': resultado,'ejemplo':ups_eje,'compra':url})

    return render(request, 'calcular.html')