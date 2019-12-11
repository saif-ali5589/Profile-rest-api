from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
#these two module import to customize default django admin page


class UserProfileManager(BaseUserManager):
    """Manager for new user profile"""


    def createuser(self,email,name,password=None):
        """create new user profile"""
        if not email:
            raise ValueError("user must have an email address")

        email = self.normalize_email(email)
        user = self.model(eamil=email,name=name)

        user.set_password(password)
        #password should we saved as a hash table
        user.save(using=self._db)

    def create_superuser(self):
        """craeting a super user """
        user =  createuser(email,name,password)
        user.is_superuser = True
        uuser.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    ''''Data base for user system'''
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELD = ['name']

    def get_full_name(self):
        """return full name"""
        return self.name

    def get_short_name(self):
        """return short name"""
        return self.name

    def __str__(self):
        """str represantaion of user it is used to reurn a object as a str"""
        return self.email
