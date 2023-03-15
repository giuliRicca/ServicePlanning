from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Custom User Manager
class UserManager(BaseUserManager):
    use_in_migration = True

    # Create User Method (email, password)
    def _create_user(self, email, password, **extra_fields):
        # Check Fields for None values
        if not email:
            raise ValueError('Email must be provided')
        if not password:
            raise ValueError('Password must be provided')
        
        # Create user mdoel with the provided fields
        user = self.model(
            # Use method to normalize email before
            email = self.normalize_email(email),
            **extra_fields
        )
        # Set Password with method so password gets hashed
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    # Method for creating superusers
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have STAFF status')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have SUPERUSER status')

        return self._create_user(email, password, **extra_fields)



# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    # Email Field
    email = models.EmailField(db_index=True, unique=True, max_length=255)

    # User Permision classes
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'







