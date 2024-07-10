from django.views import generic

from runs.models import Run

class IndexView(generic.ListView):
    template_name = 'runs/index.html'

    context_object_name = 'all_runs'

    # Get all of the current user's runs
    def get_queryset(self):
        return Run.objects.filter(user_id=self.request.user.id).order_by('-start_time')

class DetailView(generic.DetailView):
    model = Run
    template_name = 'runs/detail.html'

    # Only get the current user's run
    def get_queryset(self):
        return Run.objects.filter(user_id=self.request.user.id)