from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)  # Nuevo campo

    def __str__(self):
        return self.username
