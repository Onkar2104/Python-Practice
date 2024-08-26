# # from django.db import models
# # from django.contrib.auth.models import AbstractUser
# # # Create your models here.

# # class CustomUser(AbstractUser):
# #     username = None
    
# #     phone_number = models.CharField(max_length=100, unique=True)
# #     email = models.EmailField(unique=True)
# #     user_bio = models.CharField(max_length=50)
# #     user_profile_image = models.ImageField(upload_to="profile")

# #     USERNAME_FIELD = 'phone_number'
# #     REQUIRED_FIELDS = []

# # users/models.py
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models
# from django.utils import timezone
# from django.utils.translation import gettext_lazy as _

# class CustomUserManager(BaseUserManager):
#     def create_user(self, phone_number, email, password=None, **extra_fields):
#         if not phone_number:
#             raise ValueError(_('The Phone number field must be set'))
#         if not email:
#             raise ValueError(_('The Email field must be set'))
        
#         email = self.normalize_email(email)
#         phone_number = self.normalize_phone_number(phone_number)
        
#         user = self.model(phone_number=phone_number, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, phone_number, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(phone_number, email, password, **extra_fields)

#     def normalize_phone_number(self, phone_number):
#         # Normalize the phone number if necessary
#         return phone_number

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     phone_number = models.CharField(unique=True, max_length=15)
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     # Add any additional fields here
#     birthdate = models.DateField(null=True, blank=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = ['email']

#     def __str__(self):
#         return self.phone_number

#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}".strip()

#     def get_short_name(self):
#         return self.first_name
