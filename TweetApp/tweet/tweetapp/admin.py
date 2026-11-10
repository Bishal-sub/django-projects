from django.contrib import admin
from .models import Tweet

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user','text','img','created_at','updated_at')
    fields = ('user','text','img',)