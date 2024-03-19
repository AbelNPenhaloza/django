from django.urls import path
from .views import saludo_view
from .views import crear_usuario

urlpatterns =[
    path('saludo/', saludo_view),
]

urlpatterns =[
    path('', crear_usuario),
]
