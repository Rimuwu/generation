# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class UserManager(BaseUserManager):
#     def create_user(self, login, password=None, **extra_fields):
#         if not login:
#             raise ValueError('The Login field must be set')
#         user = self.model(login=login, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, login, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(login, password, **extra_fields)

# class User(AbstractBaseUser):
#     userid = models.UUIDField(unique=True, default=models.UUIDField().default, editable=False)
#     login = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'login'
#     REQUIRED_FIELDS = ['name']

#     def __str__(self):
#         return self.login

