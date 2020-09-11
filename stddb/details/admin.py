from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import College,Section,Branch,Student,Faculty,Profile

class StudentAdmin(admin.ModelAdmin):
    list_display = ('College_name',"Branch_name","Section_name","name","roll_number",'gender')
    search_fields = ["name"]
    list_filter = ['College_name','Branch_name',"Section_name","roll_number"]


class FacultyAdmin(admin.ModelAdmin):
    list_display = ("Faculty_name",'College_name','Qualification','Specialization')
    search_fields = ['Faculty_name']
    list_filter = ('College_name','Qualification')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(College)
admin.site.register(Student,StudentAdmin)
admin.site.register(Branch)
admin.site.register(Section)
admin.site.register(Faculty,FacultyAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)