from django.http import JsonResponse, HttpResponse  # Added HttpResponse import
from rest_framework.decorators import api_view
from .models import FAQ  # Import the FAQ model

# Home view - to check if the API is working
def home(request):
    return HttpResponse("Welcome to the FAQ API!")

# API view to get FAQs with support for multiple languages (default: English)
@api_view(['GET'])
def get_faqs(request):
    lang = request.GET.get('lang', 'en')  # Default to English if no language is provided
    faqs = FAQ.objects.all()  # Get all FAQ objects from the database

    faq_list = [
        {
            "question": getattr(faq, f'question_{lang}', faq.question),  # Get translated question based on language
            "answer": faq.answer  # Assuming the answer is in English, you can add translation logic if required
        }
        for faq in faqs
    ]
    
    return JsonResponse(faq_list, safe=False)
