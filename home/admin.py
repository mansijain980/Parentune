from django.contrib import admin
from .models import Parent, Child, Blog

class ParentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'parent_type')
    search_fields = ('name', 'email')
    list_filter = ('parent_type',)

class ChildAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'gender', 'parent')
    search_fields = ('name', 'gender', 'parent__name')
    list_filter = ('age', 'gender')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'age_group', 'gender', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('age_group', 'gender', 'created_at')

admin.site.register(Parent, ParentAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Blog, BlogAdmin)
