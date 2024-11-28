from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('pesquisa/', views.pesquisa, name='pesquisa'),
   path('pessoa/<int:id>', views.pessoa, name='pessoa'),
]
