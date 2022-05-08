from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=50)
    photo = models.FileField(blank=True, upload_to='Teachers_photo')
    approved = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.fname} {self.lname}"

class Student(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=50)
    photo = models.FileField(blank=True, upload_to='Students_photo')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.fname} {self.lname}"

class Course(models.Model):
    Ch = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    )
    name = models.CharField(max_length=250)
    narxi = models.IntegerField()
    photo = models.FileField(upload_to='Course_photo')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    daraja = models.CharField(max_length=15, choices=Ch)
    def str(self):
        return self.name

class Content(models.Model):
    nomi = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nomi

class Video(models.Model):
    video = models.FileField(upload_to='Course_video')
    duration = models.DurationField()
    data = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    content = models.ForeignKey(Content, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    video = models.ForeignKey(Video,  on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student,  on_delete=models.SET_NULL, null=True)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(default='a')
    def __str__(self):
        return self.comment

class Royxat(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.student} {self.course.name}"


