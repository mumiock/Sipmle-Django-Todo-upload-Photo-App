from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.



class User(AbstractUser):
    @property
    def is_user(self):
        if hasattr(self, 'Userinfo'):
            return True
        return False




class Userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    usn = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200)


    def _str_(self):
        return '%s : %s' % (self.usn, self.name)

class Task(models.Model):
    usn = models.ForeignKey(Userinfo, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Photo(models.Model):
    usn = models.ForeignKey(Userinfo, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return '%s' % (self.image)




