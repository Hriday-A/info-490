# Paste in: students/urls.py

# We are creating a function that will connect a url to the function from students/views.py
# ====================================================================================


from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),]