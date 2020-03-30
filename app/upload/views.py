# from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from django.views.generic import ListView, DetailView
from .models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'upload/project-overview.html'

    def get_context_data(self, **kwargs):
        theme_colors = {
            "EC": "mod-bright-purple",
            "IC": "mod-light-grey",
            "UG": "mod-bright-blue",
            "MP": "mod-light-green",
            "ES": "mod-bright-yellow",
        }
        context = super().get_context_data(**kwargs)
        context['backlog'] = Project.objects.filter(phase='B').order_by('priority')
        context['inprogress'] = Project.objects.filter(phase='IP').order_by('priority')
        context['readytodeploy'] = Project.objects.filter(phase='RD').order_by('priority')
        context['live'] = Project.objects.filter(phase='L').order_by('priority')
        context['retired'] = Project.objects.filter(phase='R').order_by('priority')
        context['theme_colors'] = theme_colors
        return context


# @login_required(login_url='/accounts/login/')
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'upload/project-detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        theme_colors = {
            "EC": "mod-bright-purple",
            "IC": "mod-light-grey",
            "UG": "mod-bright-blue",
            "MP": "mod-light-green",
            "ES": "mod-bright-yellow",
        }
        context = super().get_context_data(**kwargs)
        context['theme_colors'] = theme_colors
        return context


@register.filter
def get_theme_color(dict, key):
    return dict.get(key)

