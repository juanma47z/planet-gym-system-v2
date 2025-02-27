from django.db import models

class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    occupation = models.CharField(max_length=100)
    start_date = models.DateField()
    bloog_group = models.CharField(max_length=3)
    observations = models.TextField(blank=True, null=True)
    id_socio = models.IntegerField()
    teacher = models.BooleanField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"