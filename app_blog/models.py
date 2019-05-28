from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'pk':self.pk})

