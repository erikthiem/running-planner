from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from runs.forms import NewRunForm
from runs.models import Run

from rest_framework import viewsets

from runs.serializers import RunSerializer

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
    
def new_run(request):
    if request.method == "POST":
        form = NewRunForm(request.POST)

        if form.is_valid():
            form.save(user=request.user)
            return HttpResponseRedirect(reverse('runs:index'))
    else:
        form = NewRunForm()
    
    return render(request, "runs/new.html", {"form": form})

class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.order_by('-start_time')
    serializer_class = RunSerializer

    def get_queryset(self):
        return Run.objects.filter(user_id=self.request.user.id).order_by('-start_time')
