from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
# Create your views here.



class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/student_form.html'
    fields = ['name', 'roll_number', 'age', 'grade']

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/student_form.html'
    fields = ['name', 'roll_number', 'age', 'grade']

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
