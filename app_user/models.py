from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo email es requerido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Correo electrónico')
    first_name = models.CharField(max_length=70, verbose_name='Nombre/s')
    last_name = models.CharField(max_length=45, verbose_name='Apellido/s')
    is_staff = models.BooleanField(default=False, verbose_name='Estado de staff')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name')

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'

    def __str__(self):
        return self.email
