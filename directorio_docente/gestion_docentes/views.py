from django.shortcuts import render

def lista_docentes(request):
    return render(request, 'gestion_docentes/lista.html')