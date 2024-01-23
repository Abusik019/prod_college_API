from django.contrib import admin
from django.db.models import Q
from .models import User, Student, Teacher


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_teacher')
    search_fields = ('first_name', 'last_name')
    exclude = ('user_permissions', 'groups', 'date_joined', 'last_login')

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        search_term = search_term.strip()
        if search_term:
            search_term_list = search_term.split()
            search_condition = Q()
            for term in search_term_list:
                search_condition |= Q(first_name__icontains=term)
                search_condition |= Q(last_name__icontains=term)
            queryset |= self.model.objects.filter(search_condition)
        return queryset, use_distinct


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_user_name',)

    def get_user_name(self, obj):
        return f"{obj.teacher.first_name} {obj.teacher.last_name}"

    get_user_name.short_description = 'Teacher Name'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_user_name', 'group')

    def get_user_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"

    get_user_name.short_description = 'Student Name'
