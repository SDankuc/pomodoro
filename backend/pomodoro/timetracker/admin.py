from django.contrib import admin

# Register your models here.
from .models import Schema,Pomodoro,Category

class SchemaAdmin(admin.ModelAdmin):
    list_filter = ("id","duration")
    list_display = ("active",)

class PomodoroAdmin(admin.ModelAdmin):
    list_filter = ("title",)
    list_display = ("title", "amount")

class CategorykAdmin(admin.ModelAdmin):
    list_filter = ("title",)
    list_display = ("title",)

admin.site.register(Schema,SchemaAdmin)
admin.site.register(Pomodoro,PomodoroAdmin)
admin.site.register(Category,CategorykAdmin)
