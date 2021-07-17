from django.urls import path

from.views import contacto, galeria,home, manualidades

urlpatterns = [
    path('',home,name="home"),
    path('contacto/',contacto,name="contacto"),
    path('manualidades/',manualidades,name="manualidades"),
    path('galeria/',galeria,name="galeria"),


    

]
