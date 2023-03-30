from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def natal(request):
    Dia = datetime.now()
    EhNatal = True if Dia.month == 12 and Dia.day == 25 else False
    Natal = {
        'natal': EhNatal
    }
    return render(request, 'natal.html', Natal)

def tiradentes(request):
    Dia = datetime.now()
    EhTiradentes = True if Dia.month == 4 and Dia.day == 21 else False
    Tiradentes = {
        'tiradentes': EhTiradentes
    }    
    return render(request, 'tiradentes.html', Tiradentes)


