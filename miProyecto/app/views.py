from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app/home.html')

def manualidades(request):
    return render(request,'app/manualidades.html')

def contacto(request):
    return render(request,'app/contacto.html')


def galeria(request):
    return render(request,'app/galeria.html')

