from django.contrib import admin
from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)

admin.site.site_title = 'ISKRA Админ-панель' #то что на вкладке
admin.site.site_header = 'ISKRA Admin' #То что в хедоре
