from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(PDF)
admin.site.register(Comment)
admin.site.register(Thread)
