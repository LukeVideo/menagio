from django.contrib import admin
from .models import Task, Place, Menagio

# Register your models here.

# use default admin vue
admin.site.register(Task)
admin.site.register(Place)
admin.site.register(Menagio)
