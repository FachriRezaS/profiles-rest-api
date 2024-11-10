from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserProfileManager(BaseUserManager):
    """Manager for UserProfile objects"""
    def create_user(self, username, email, first_name, last_name, password=None):
        """create a new user profile"""
        if not username:
            raise ValueError("Username must be provided.")
        if not email:
            raise ValueError("Email must be provided.")
        if not first_name:
            raise ValueError("First name must be provided.")
        if not last_name:
            raise ValueError("Last name must be provided.")

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, email, first_name, last_name, password):
        """Create and save a new superuser"""
        user = self.create_user(username, email, first_name, last_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system."""
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        """Returns the full name"""
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        """Returns the short name"""
        return self.first_name
    
    def get_email_address(self):
        """Returns the email address of the user"""
        return self.email
    
    def __str__(self):
        """Returns the string representation of the user"""
        return self.username

# class UserProfileAddress(models.Model):
#     """Database model for user addresses"""
#     id = models.AutoField(primary_key=True)
#     user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     street_address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=10)

#     def __str__(self):
#         """Returns the string representation of the user address"""
#         return f"{self.street_address}, {self.city}, {self.state} {self.zip_code}"

