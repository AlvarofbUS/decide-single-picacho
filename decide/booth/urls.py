from django.urls import path
from .views import BoothView, BoothListView, VotingList

urlpatterns = [
    path('<int:voting_id>/', BoothView.as_view()),
    path('', BoothListView.as_view()),
    path('votaciones/', VotingList.as_view()),
]
