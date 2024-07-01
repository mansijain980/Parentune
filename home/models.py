from django.db import models


# Create your models here.
class Parent(models.Model):
    Parent_Type_Choices = [("first_time", "First-time Parent"),("experienced", "Experienced Parent")]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    parent_type = models.CharField(max_length=100, choices = Parent_Type_Choices)

class Child(models.Model):
    Gender_choices = [("male", "Male"),("female", "Female")]
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, choices=Gender_choices)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    age_group = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


