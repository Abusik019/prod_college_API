from django.contrib import admin
from django.db.models import Q
from .models import User, Facult, Course, Group, Student, Teacher


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    exclude = ('email', 'user_permissions', 'groups', 'date_joined', 'last_login')

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
    list_display = ('pk',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk',)



@admin.register(Facult)
class FacultAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
