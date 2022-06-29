from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.contacts, name = 'contacts')
]