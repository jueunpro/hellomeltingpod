from django.contrib import admin
from .models import Post, Comment
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','photo_tag')

    def photo_tag(self, post):
        return mark_safe('<img src="{}" width=80 />'.format(post.photo.url))
    
 
#admin.site.register(Post)
admin.site.register(Comment)