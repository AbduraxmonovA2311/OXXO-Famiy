from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=10, default='Yaxshi')  # <-- shu joy muhim
    message = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.rating})"
