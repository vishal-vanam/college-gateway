from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mains_rank = models.IntegerField()
    advanced_rank = models.IntegerField(default=100000)


class College(models.Model):
    c_name = models.CharField(max_length=100)
    c_locality = models.CharField(max_length=100)
    c_state = models.CharField(max_length=100)
    c_country = models.CharField(max_length=100)
    c_pincode = models.IntegerField()
    c_link = models.CharField(max_length=100)
    c_value = models.IntegerField(default=0)

    def __str__(self):
        return self.c_name

class Department(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, default=1)
    d_name = models.CharField(max_length=100)
    op_rank = models.IntegerField(validators=[MinValueValidator(1)])
    cl_rank = models.IntegerField(validators=[MaxValueValidator(250000)])

    def __str__(self):
        return self.d_name
