from django.contrib import admin
from account.models import User
# Register your models here.
from .models import Articles


admin.site.register(Articles)
admin.site.register(User)



