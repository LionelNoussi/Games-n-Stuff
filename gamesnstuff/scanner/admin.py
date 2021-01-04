from django.contrib import admin
from .models import Item, Student
from django.contrib.auth.models import Group, User

admin.site.site_header = "Administration"
admin.site.index_title = "Welcome to: Games 'n Stuff"

class AdminStudent(admin.ModelAdmin):
    list_display = ("student_name", "student_id")
    search_fields = ("student_name__startswith", "student_id__startswith")

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class AdminItem(admin.ModelAdmin):
    search_fields = ("item_name__startswith",)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


# Register your models here.
admin.site.register(Item, AdminItem)
admin.site.register(Student, AdminStudent)
admin.site.unregister(Group)
admin.site.unregister(User)
