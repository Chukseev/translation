from django.contrib import admin
from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)

admin.site.site_title = ''
admin.site.site_header = ''
