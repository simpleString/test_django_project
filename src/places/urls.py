from django.urls import path
from places.views import PlacesListView, CreatePlaceView, about

urlpatterns = [
    path('', PlacesListView.as_view()),
    path('place/create', CreatePlaceView.as_view(), name='create_place'),
    path('about', about)
]
