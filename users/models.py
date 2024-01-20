from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


# User Manager
# User Manager
class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is Required")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser = True")

        return self.create_user(email, password, **extra_fields)




class Users(AbstractUser, models.Model):
    first_name = None
    last_name = None
    username = None
    last_login = None
    date_joined = None

    username = models.CharField(verbose_name=_('User Name'), max_length=100, db_column='username',unique = True)
    address = models.TextField(verbose_name=_('Address'), db_column='address')

    # General info
    email = models.EmailField(verbose_name=_('Email'), max_length=100, db_column="email", unique =True)
    password = models.CharField(verbose_name=_('Password'), max_length=128, db_column="password")
    number = models.CharField(verbose_name=_('Number'), max_length=20, db_column="number")
    profilePicture = models.ImageField(verbose_name=_('Profile Picture'), max_length=512, db_column="profile_picture",upload_to="profiles/")
    # User permissions
    is_active = models.BooleanField(verbose_name=_('Is Active'), default=True, db_column="is_active")
    is_staff = models.BooleanField(verbose_name=_('Is Staff'), default=False, db_column="is_staff")
    is_superuser = models.BooleanField(verbose_name=_('Is Superuser'), default=False, db_column="is_superuser")

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email","password"]
    # REQUIRED_FIELDS = ["firstName", "lastName", "password"]
    # REQUIRED_FIELDS = ["firstName", "lastName", "password"]

    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"
        verbose_name_plural = "user"
        managed = True
