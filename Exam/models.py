from django.db import models

# Create your models here.
from django.db import models

class Questions(models.Model):
    qid = models.IntegerField(primary_key=True)
    qtext = models.CharField(max_length=250)
    op1 = models.CharField(max_length=250)
    op2 = models.CharField(max_length=250)
    op3 = models.CharField(max_length=250)
    op4 = models.CharField(max_length=250)
    correct_ans = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)

class StudentInfo(models.Model):
    username = models.CharField(max_length=250, primary_key=True)
    password = models.CharField(max_length=250)
    mobno = models.BigIntegerField()


class Student(models.Model):
    sid = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=100)
    semail = models.EmailField(unique=True)
    spassword = models.CharField(max_length=50) # In a real app, use hashing!
    sdepartment = models.CharField(max_length=100)

    def __cl__str__(self):
        return self.sname


