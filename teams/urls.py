from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.TeamView.as_view()),
    path('teams/<team_id>/', views.TeamDetailView.as_view())
]