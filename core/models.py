from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employer"
    )
    company_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class Candidate(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="cadidate"
    )
    phone_no=models.CharField(max_length=10)
    skills=models.CharField(max_length=50)

    def __str__(self):
        return self.user.name

class Job(models.Model):
    employer=models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="jobs"
    )

    title=models.CharField(max_length=50)
    description=models.TextField(max_length=150)
    location=models.CharField(max_length=60)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Application(models.Model):
    candidate=models.ForeignKey(Candidate,on_delete=models.CASCADE,related_name="applications")
    Job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name="applications")
    status=models.CharField(max_length=30,default="applied")
    applied_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Job.title} - {self.User.name}"