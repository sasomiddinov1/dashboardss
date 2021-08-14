from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),

    path('create_post', views.createPost, name="create_post"),

    path('create_mentor', views.createMentor, name="create_mentor"),
    path('mentors_table', views.mentorsTable, name="mentors_table"),
    path('update_mentor/<str:pk>', views.updateMentor, name="update_mentor"),
    path('delete_mentor/<str:pk>', views.deleteMentor, name="delete_mentor"),

    path('create_group', views.createGroup, name="create_group"),
    path('update_group/<str:pk>', views.updateGroup, name="update_group"),
    path('delete_group/<str:pk>', views.deleteGroup, name="delete_group"),
    path('groups_table', views.groupsTable, name="groups_table"), 
      
]