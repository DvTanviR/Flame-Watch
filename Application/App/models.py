from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
