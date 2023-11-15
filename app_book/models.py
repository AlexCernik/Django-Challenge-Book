from django.db import models
from app_user.models import User

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    title = models.CharField(max_length=256, verbose_name='Título')
    author = models.CharField(max_length=256, verbose_name='Autor')
    year_publication = models.DateField(verbose_name='Año de publicación')

    class Meta:
        verbose_name = 'Libro'

    def __str__(self):
        return self.title