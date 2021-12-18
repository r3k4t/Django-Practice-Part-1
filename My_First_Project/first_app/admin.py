# python manage.py createsuperuser
# 127.0.0.1:8080/admin

from django.contrib import admin
from first_app.models import Musician,Album


admin.site.register(Musician)
admin.site.register(Album)