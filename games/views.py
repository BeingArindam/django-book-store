from  django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from .models import Game
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'games/index.html'
    context_object_name = 'all_games'

    def get_queryset(self):
        return Game.objects.all()

class DetailsView(generic.DetailView):
    model = Game
    template_name = 'games/detail.html'

class GameCreate(CreateView):
    model = Game
    fields = ['title', 'production', 'genre', 'logo', 'release_year' ]

class GameUpdate(UpdateView):
    model = Game
    fields = ['title', 'production', 'genre', 'logo', 'release_year' ]

class GameDelete(DeleteView):
    model = Game
    success_url = reverse_lazy('games:index')
