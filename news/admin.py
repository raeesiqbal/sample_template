from django.contrib import admin
from news.models import News, Media, Subject


admin.site.register(News)
admin.site.register(Subject)
admin.site.register(Media)
