from django.urls import include, path
from rest_framework import routers, serializers, viewsets

from runs.models import Run

from . import views

# API registration
router = routers.DefaultRouter()
router.register(r'runs', views.RunViewSet)

app_name = 'runs'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path('new/', views.new_run, name="new"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
]

