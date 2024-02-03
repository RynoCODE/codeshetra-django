from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField

# Create your models here.

class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class credit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
class interview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    # assigned_user = models.CharField(max_length=200, default="None")
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_user', null=True, blank=True)
    done = models.BooleanField(default=False)
    room_id = models.CharField(max_length=200, default="None")
    def __str__(self):
        return self.user.username
# class Order(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     amount = models.IntegerField(_("Amount"), default=0)
#     status = models.CharField(_("Status"), max_length=50, default="Pending")
#     order_id = models.CharField(_("Order ID"), max_length=50, default="Pending")