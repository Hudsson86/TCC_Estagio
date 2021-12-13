from django.views.generic import DetailView, ListView

from .models import Vaga


class VagaListView(ListView):
    model = Vaga

class VagaDetailView(DetailView):
    model = Vaga
