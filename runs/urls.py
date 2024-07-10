from django.urls import include, path

from . import views

app_name = 'runs'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path('new/', views.new_run, name="new"),
    path('accounts/', include('django.contrib.auth.urls')),
]