from django.shortcuts import redirect, render
from django.views.generic import View, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import CreatePlaceForm
from .models import Place


@method_decorator(login_required, name='dispatch')
class PlacesListView(ListView):
    model = Place
    template_name = 'places/places_list.html'

    def get_queryset(self):
        return Place.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class CreatePlaceView(View):
    def get(self, request, *args, **kwargs):
        context = {'form': CreatePlaceForm()}
        return render(request, 'places/place_create.html', context)

    def post(self, request, *args, **kwargs):
        form = CreatePlaceForm(request.POST, request.FILES)
        if form.is_valid():
            print("hello")
            place = form.save(commit=False)
            place.user = request.user
            place.save()
            return redirect('/')
        return render(request, 'places/place_create.html', {'form': form})


def about(request):
    return render(request, 'places/about.html')
