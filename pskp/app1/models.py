from django.db import models

# Create your models here.
class student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=15,null=False)
    dob=models.DateField(null=False)
    email=models.EmailField(null=False)
