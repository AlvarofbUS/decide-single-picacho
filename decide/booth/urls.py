from django.urls import path
from .views import BoothView, BoothListView

urlpatterns = [
    path('<int:voting_id>/', BoothView.as_view()),
    path('', BoothListView.as_view())
]
