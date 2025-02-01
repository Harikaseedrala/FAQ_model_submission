from django.urls import path
from .views import home, get_faqs  # Import the home view and get_faqs

urlpatterns = [
    path('', home, name='home'),  # This will handle http://127.0.0.1:8000/
    path('faqs/', get_faqs, name='get_faqs'),  # This will handle the FAQ API at /api/faqs/
]
