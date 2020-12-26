from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self,email,password=None):
        if not email:
            raise ValueError('У пользоваля должна быть почта')
        user=self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user



    def create_superuser(self,email,password):
        if password is None:
            raise TypeError('Суперпользователь должен иметь пароль')
        user=self.create_user(email,password)
        user.is_superuser=True
        user.is_staff=True
        user.asve()




class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(verbose_name='Почта',
                            max_length=100,
                            unique=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


    class Meta:

        db_table='login'

