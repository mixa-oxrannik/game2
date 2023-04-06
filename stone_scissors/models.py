from django.db import models

class Choice(models.Model):
    CHOICES = (
        ('Камень', 'Камень'),
        ('Ножницы', 'Ножницы'),
        ('Бумага', 'Бумага'),
    )
    choice = models.CharField(max_length=10, choices=CHOICES)

    def __str__(self):
        return self.choice

