from django.http import HttpResponse
from django.shortcuts import render
from students.models import Student
from .models import Student

def home(request):
   return HttpResponse("Hello from the students app!")

def student_list(request):
   students= Student.objects.all()
   context = {
      "students": students
   }
   return render(request,"students/student_list.html",context)