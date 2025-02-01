from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()  # Original question in English
    answer = RichTextField()  # Original answer in English

    # Translated fields for question and answer in different languages
    question_hi = models.TextField(blank=True, null=True)  # Question in Hindi
    answer_hi = RichTextField(blank=True, null=True)  # Answer in Hindi

    question_bn = models.TextField(blank=True, null=True)  # Question in Bengali
    answer_bn = RichTextField(blank=True, null=True)  # Answer in Bengali

    def save(self, *args, **kwargs):
        """Override the save method to automatically translate questions and answers."""
        translator = Translator()

        # Automatically translate question and answer if they are not provided
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, src='en', dest='hi').text

        if not self.question_bn:
            self.question_bn = translator.translate(self.question, src='en', dest='bn').text
        
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, src='en', dest='bn').text

        # Save the instance
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question

    def get_translated(self, lang='en'):
        """Get the translated question and answer based on the requested language."""
        translation = {
            'question': self.question,
            'answer': self.answer,
        }

        if lang == 'hi':
            translation['question'] = self.question_hi if self.question_hi else self.question
            translation['answer'] = self.answer_hi if self.answer_hi else self.answer
        elif lang == 'bn':
            translation['question'] = self.question_bn if self.question_bn else self.question
            translation['answer'] = self.answer_bn if self.answer_bn else self.answer

        return translation
