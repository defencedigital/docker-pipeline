from django.views.generic import ListView, DetailView
from .models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'upload/project-overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['backlog'] = Project.objects.filter(phase='B')
        context['inprogress'] = Project.objects.filter(phase='IP')
        context['readytodeploy'] = Project.objects.filter(phase='RD')
        context['live'] = Project.objects.filter(phase='L')
        context['retired'] = Project.objects.filter(phase='R')
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'upload/project-detail.html'
    context_object_name = 'project'
