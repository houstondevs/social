from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from datetime import date, timedelta, datetime
from django.urls import reverse



class Profile(models.Model):
    def content_file_name(instance, filename):
        name, ext = filename.split('.')
        file_path = 'profile_images/{uname}/{name}.{ext}'.format(uname=instance.user.username, name=name, ext=ext) 
        return file_path
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=content_file_name,default='profile_images/default.jpg', blank=True, null=True)
    city = models.CharField(max_length=30, default="Не указан", blank=True, null=True)
    bio = models.TextField(max_length=500,default="Не указана", blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    age = models.IntegerField(default=0)

    @property
    def set_age(self):
        return int((datetime.now().date() - self.birth_date).days / 365.25)

    def save(self, *args, **kwargs):
        if self.birth_date is not None:
            self.age = self.set_age
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile_url', kwargs={'pk':self.pk})
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

