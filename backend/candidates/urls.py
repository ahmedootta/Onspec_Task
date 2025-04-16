from django.urls import path
from .views import CandidateListView, CandidateCreateUpdate

urlpatterns = [
    path("", CandidateListView.as_view(), name="list_candidates"),
    path('create_update', CandidateCreateUpdate.as_view(), name="create_update"),
    # path('<int:candidate_id>/update', CandidateUpdate.as_view(), name="update_candidate"),
]