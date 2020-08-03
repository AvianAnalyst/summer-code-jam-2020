from django.db import models


# Create your models here.
class Chatbot(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"name={self.name}"
