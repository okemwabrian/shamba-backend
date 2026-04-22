from django.contrib import admin
from .models import User, Field, FieldUpdate

admin.site.register(User)
admin.site.register(Field)
admin.site.register(FieldUpdate)