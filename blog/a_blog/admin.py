from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
  list_display = ("post_title","post_author","post_publish_date")


admin.site.register(models.Post,PostAdmin)