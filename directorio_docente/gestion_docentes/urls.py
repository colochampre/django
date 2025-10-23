from django.urls import path
from .views import lista_docentes

urlpatterns = [
    path('', lista_docentes, name='lista'),
]