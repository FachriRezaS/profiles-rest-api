from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserProfileManager(BaseUserManager):
    """Manager for UserProfile objects"""
    def create_user(self, email, name, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError("Email must be provided.")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """Create and save a new superuser"""
        user = self.create_user(email, name, password)
        
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        """Returns the short name"""
        return self.name
    
    def get_short_name(self):
        """Returns the short name"""
        return self.name
    
    def __str__(self):
        """Returns the email address of the user"""
        return self.email

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

