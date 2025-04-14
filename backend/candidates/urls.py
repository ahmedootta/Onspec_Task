from django.urls import path
from .views import CandidateListView

urlpatterns = [
    path("", CandidateListView.as_view(), name="list_candidates")
]