from django.contrib import admin

from .models import Art
from .models import Comment

admin.site.register(Art)
admin.site.register(Comment)
