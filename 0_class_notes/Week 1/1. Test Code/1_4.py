# Paste in: illinois/urls.py

# We are connecting urls for all the applications that we have created (including the existing admin feature).
# ====================================================================================

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('students.urls')),  # ← add this line
]