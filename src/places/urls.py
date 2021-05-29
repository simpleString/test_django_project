from django.urls import path

from places.views import place_list

urlpatterns = [
    path('', place_list),
]
