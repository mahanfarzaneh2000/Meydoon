from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from PIL import Image
import os
import uuid

# This is a class for managing our custom user authentication
class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, user_name, phone_number, password, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(_('SuperUser must be assigned to is_staff'))
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError(_('SuperUser must be assigned to is_superuser'))

        return self.create_user(email,user_name,phone_number,password,**other_fields)

    def create_user(self, email, user_name, phone_number, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        # TODO: Check for valid phone number
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, phone_number=phone_number, **other_fields)
        user.set_password(password)
        user.save()
        return user


# This class created to add and replace some features
# of default django user model
class User(AbstractBaseUser,PermissionsMixin):
    email = models.CharField(max_length=80,unique=True)
    user_name = models.CharField(max_length=80,unique=True)
    first_name = models.CharField(max_length=80,blank=True,null=True)
    last_name = models.CharField(max_length=80,blank=True,null=True)
    phone_number = models.CharField(max_length=15,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_vertified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    vertified_at = models.DateTimeField(blank=True,null=True)
    premiumed_at = models.DateTimeField(blank=True,null=True)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','user_name']

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('profile_pics', filename)

# Addition to user model for more inforamtion about user
class Profile(models.Model):
    user = models.OneToOneField('users.User', on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to=get_file_path,default='profile_pics/default.jpg',blank=True,null=True) #save profile pic at pics folder
    national_id = models.CharField(max_length=20,null=True,blank=True)
    bank_number = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=400, null=True, blank=True)
    bio = models.CharField(max_length=256,null=True,blank=True)
    degree = models.IntegerField(blank=True,null=True)
    degree_profanity = models.IntegerField(blank=True,null=True)
    birthday = models.DateField(blank=True,null=True)

    def __str__(self):
        return f'{self.user.user_name} Profile'
    
    # RESET the default picture and resize uploaded images
    def save(self,*args, **kwargs):
        if not self.profile_pic:
            self.profile_pic = 'profile_pics/default.jpg'
        super().save(*args, **kwargs)
        if self.profile_pic and not 'default.jpg' in self.profile_pic.path:
            img = Image.open(self.profile_pic.path)

            if img.height>512 or img.width>512:
                output_size=(512,512)
                img.thumbnail(output_size)
                img.save(self.profile_pic.path)

            