# Paste in: students/views.py

# We are creating a function that will return a string when called.

# ====================================================================================

from django.http import HttpResponse

def home(request):
   return HttpResponse("Hello from the students app!")