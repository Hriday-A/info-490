# Register the models in students/admin.py

# IMPORTANT: We are doing this to make these models visible in the admin panel.

# Next steps: Now after registering these in the admin.py, re-run:
# python manage.py runserver

# You should be now able to see the tables in the admin panel

# ======================================================


from django.contrib import admin
from .models import Section, Student, Enrollment

admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Enrollment)