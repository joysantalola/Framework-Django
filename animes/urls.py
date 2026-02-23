from django.urls import path
from . import views

urlpatterns = [
    path('', views.llista_animes, name='llista_animes'),
    path('afegir/', views.afegir_anime, name='afegir_anime'),
    path('editar/<int:pk>/', views.editar_anime, name='editar_anime'),
    path('afegir_personatge/', views.afegir_personatge, name='afegir_personatge'),
    path('eliminar/<int:pk>/', views.eliminar_anime, name='eliminar_anime'),
]
#Oleguer
