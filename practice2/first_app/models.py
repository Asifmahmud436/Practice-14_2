from django.db import models

class Practice_2(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    date_of_birth = models.DateTimeField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.IntegerField()
    thought_on_life = models.TextField()

    def __str__(self):
        return self.name

