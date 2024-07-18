from django.db import models

# Create your models here.

#create blog category models
class Category(models.Model):
    id              =models.AutoField(primary_key=True)
    name            =models.CharField(max_length=200)
    description     =models.TextField()
    is_published    =models.BooleanField(default=True)
    created_on      =models.DateTimeField(auto_now=True)