from django.shortcuts import redirect, render


def place_list(request):

    return render(request, 'places/places_list.html')
