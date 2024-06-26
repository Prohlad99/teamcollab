from django.urls import path
from .views import (
    RegisterUserView, LoginUserView, UserDetailView,
    ProjectListCreateView, ProjectDetailView,
    TaskListCreateView, TaskDetailView,
    CommentListCreateView, CommentDetailView
)

urlpatterns = [
    path('users/register/', RegisterUserView.as_view(), name='register'),
    path('users/login/', LoginUserView.as_view(), name='login'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

    path('projects/<int:project_id>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    path('tasks/<int:task_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
