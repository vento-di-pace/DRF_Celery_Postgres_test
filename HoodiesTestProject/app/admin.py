from django.contrib import admin
from HoodiesTestProject.app.models import Page, Content, Video, Audio, Text
# Register your models here.

# class PageAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#
#
# class ContentAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#
#
# class VideoAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#
#
# class AudioAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#
#
# class TextAdmin(admin.ModelAdmin):
#     list_display = '__all__'

admin.site.register(Page)
admin.site.register(Content)
admin.site.register(Video)
admin.site.register(Audio)
admin.site.register(Text)
