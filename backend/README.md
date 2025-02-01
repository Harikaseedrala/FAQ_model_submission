#1.Requirements:-
a.Set up your database:-python manage.py migrate
b.Run the server:-python manage.py runserver
server should be running at http://127.0.0.1:8000/.

#2.API Usage:-
a.Fetch FAQs in English (default language):http://127.0.0.1:8000/api/faqs/
b.Fetch FAQs in Hindi:http://127.0.0.1:8000/api/faqs/?lang=hi
Fetch FAQs in Bengali:http://127.0.0.1:8000/api/faqs/?lang=bn
