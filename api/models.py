# models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone

class UsuarioManager(BaseUserManager):
    def get_by_natural_key(self, rut_user):
        return self.get(rut_user=rut_user)

    def create_user(self, rut_user, dv_user, email=None, password=None, **extra_fields):
        if not rut_user or not dv_user:
            raise ValueError("El RUT y el dígito verificador son obligatorios")
        user = self.model(rut_user=rut_user, dv_user=dv_user, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut_user, dv_user, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(rut_user, dv_user, email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=False, blank=True, null=True)
    rut_user = models.IntegerField(unique=True)
    dv_user = models.CharField(max_length=1)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'rut_user'
    REQUIRED_FIELDS = ['dv_user']

    objects = UsuarioManager()

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return f"{self.rut_user}-{self.dv_user}"
