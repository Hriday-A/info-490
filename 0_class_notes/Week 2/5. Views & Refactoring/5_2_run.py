# Paste in illinois/urls.py (master settings)

# Now, we are importing all the urls from 'students/urls' or 'students.urls'
# which are related to only its features here at once.

# ================================================

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
]