from django.urls import path
from . import views

app_name = 'fsnst_app'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('programs/', views.programs_list_view, name='programs_list'),
    path('programs/<int:pk>/', views.program_detail_view, name='program_detail'),
    path('departments/', views.departments_list_view, name='departments_list'),
    path('departments/<int:pk>/', views.department_detail_view, name='department_detail'),
]