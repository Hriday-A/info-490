# Paste in: students/urls.py

# So, we are now organizing it and making it more efficient to organize url patterns.
# This file will contain only the URLs related to any function defined in students/views.py

# ======================================================

from django.urls import path, include

# Step 1: We import the student_list_view() function's output from students/views.py
from students.views import student_list_view

# Now, we link that output to the url associated with it.
urlpatterns = [
    path('students/', student_list_view),
]