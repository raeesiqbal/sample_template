from django.contrib import admin
from articles.models import Article, Subject

admin.site.register(Subject)

@admin.register(Article)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug':('title',), }
