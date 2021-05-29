from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    path('', include('places.urls')),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

]
