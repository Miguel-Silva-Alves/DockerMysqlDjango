from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    department = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.first_name
