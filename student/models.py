# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Detail(models.Model):
	first_name = models.CharField(max_length = 150)
	last_name = models.CharField(max_length = 150)
	middle_name = models.CharField(max_length = 150)
	age = models.IntegerField()
	birthday = models.DateTimeField()
	course = models.ManyToManyField("Course",related_name="Detail")
	#course = models.CharField(max_length = 150)
	
	def __str__(self):
		#return self.first_name
		return "{} Course {}".format(self.first_name,self.list_course())
		
	def list_course(self):
		return ",".join([course.course_name for course in self.course.all()])
		
	def save(self,*args,**kwargs):

		super(Detail,self).save(*args,**kwargs)


class Faculty(models.Model):
	first_name = models.CharField(max_length = 150)
	last_name = models.CharField(max_length = 150)
	middle_name = models.CharField(max_length = 150)
	position = models.CharField(max_length = 150)
	bio = models.TextField(max_length = 500)
	
	
	def __str__(self):
		return self.first_name
		
		
	def save(self,*args,**kwargs):

		super(Faculty,self).save(*args,**kwargs)
		
class Course(models.Model):
	course_name = models.CharField(max_length=150)
	description = models.TextField(max_length=550)
	subject = models.ManyToManyField("Subject",related_name="Courses")
	
	def __str__(self):
		return self.course_name
		 
class Subject(models.Model):
	subject_name = models.CharField(max_length=150)
	description = models.TextField(max_length=550)
	
	def __str__(self):
		return self.subject_name
		
# Create your models here.
