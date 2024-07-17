from django.contrib import admin
from bootcamp.articles.models import Article

#this is the default....
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status")
    list_filter = ("user", "status", "timestamp")

