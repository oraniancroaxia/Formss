# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from .models import Faculty
from .models import Detail
# Create your views here.

class faculty_list(View):
	def get(self,request):
		faculties = Faculty.objects.all()
		context = {
		'faculty' : faculties,
		}
		return render(request,"Faculty.html",context)
		
def list_student(request):
		students = Detail.objects.exclude()
		context = {
		'students' : students,
		}
		return render(request,"index.html",context)	