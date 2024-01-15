from django.urls import path
from .views import group_list, GroupMembersView, subjects_list


urlpatterns = [
    path('get_groups', group_list, name='group_list'),
    path('group_members/<int:group_id>/', GroupMembersView.as_view(), name='group_members'),
    path('get_subjects/', subjects_list, name='subjects_list'),
]
