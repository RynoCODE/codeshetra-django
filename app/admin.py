from django.contrib import admin
from . models import RoomMember, UserProfile, credit
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(credit)