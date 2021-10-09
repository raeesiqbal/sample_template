from django.contrib import admin
from courses.models import Course, Subject, Video, Youtube


admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Youtube)
