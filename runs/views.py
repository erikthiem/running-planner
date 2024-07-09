from django.views import generic

from runs.models import Run

class IndexView(generic.ListView):
    template_name = 'runs/index.html'

    context_object_name = 'all_runs'

    def get_queryset(self):
        return Run.objects.order_by('-start_time')