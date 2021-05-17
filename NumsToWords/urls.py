from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="welcome"),
    path('num_to_english/', views.convert, name="convert"),
    path('api/num_to_english/<number>', views.api_convert, name="convert"),
]