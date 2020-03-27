from django.urls import path
from .views import ProjectListView, ProjectDetailView

app_name = 'upload'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
]