from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Resident)
admin.site.register(Employee)
admin.site.register(Group)
admin.site.register(Permission)
admin.site.register(CommunityEvent)