from django.db import models

# Create your models here.


class Students(models.Model):
    name=models.CharField(max_length=20)
    dob=models.CharField(max_length=15)
    mobile=models.CharField(max_length=25)
    email=models.CharField(max_length=15)
    gender=models.CharField(max_length=8)

    def __str__(self):
        temp="{0.name} {0.dob} {0.mobile} {0.email} {0.gender}"
        return temp.format(self)

