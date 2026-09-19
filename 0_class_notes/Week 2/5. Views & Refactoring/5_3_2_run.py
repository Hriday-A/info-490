# Paste in: students/urls.py

from django.urls import path, include

# Step 1: Import the StudentList class
from students.views import StudentListView

# Step 2: define the url
# Check slides of week 2 to see the purpose of 'name'.
# You don't have to worry about changing url everywhere if I decide to change from 'student/' to 'student_new_url'
# This is because we're using the 'name' parameter in 'path()' function which takes care of it for me.

urlpatterns = [
    path('student/',
         StudentListView.as_view(),
         name='student-list-url'),
]
