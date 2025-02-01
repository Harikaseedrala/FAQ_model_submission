# faq/tests.py
from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        # Create some FAQs for testing
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework.",
            question_hi="डjango क्या है?",
            answer_hi="Django एक उच्च-स्तरीय Python वेब फ्रेमवर्क है।",
            question_bn="ডjango কি?",
            answer_bn="Django একটি উচ্চ-স্তরের Python ওয়েব ফ্রেমওয়ার্ক।"
        )

    def test_faq_translation(self):
        # Test default English translation
        translated = self.faq.get_translated(lang='en')
        self.assertEqual(translated['question'], "What is Django?")
        self.assertEqual(translated['answer'], "Django is a high-level Python web framework.")

        # Test Hindi translation
        translated_hi = self.faq.get_translated(lang='hi')
        self.assertEqual(translated_hi['question'], "डjango क्या है?")
        self.assertEqual(translated_hi['answer'], "Django एक उच्च-स्तरीय Python वेब फ्रेमवर्क है।")
        
        # Test Bengali translation
        translated_bn = self.faq.get_translated(lang='bn')
        self.assertEqual(translated_bn['question'], "ডjango কি?")
        self.assertEqual(translated_bn['answer'], "Django একটি উচ্চ-স্তরের Python ওয়েব ফ্রেমওয়ার্ক।")
