from django import forms
from django.utils import timezone

from runs.models import Run

class NewRunForm(forms.ModelForm):
    #distance_miles = forms.FloatField(label="Distance (miles)", min_value=0.0)
    #start_time = forms.DateTimeField(label="Start Time", initial=timezone.now)
    class Meta:
        model=Run
        fields = ['distance_miles', 'start_time']

    # Override to allow linking current user on new run submission
    def save(self, commit=True, user=None):
        run = super().save(commit=False)
        if user:
            run.user = user
        if commit:
            run.save()
        return run