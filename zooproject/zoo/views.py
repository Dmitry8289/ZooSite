from django.shortcuts import render
from django.utils import timezone

from zoo.models import Zoo
from .forms import ZooForm


def zoo_list_view(request):
    zoo = Zoo.objects.all()
    context = {'zoo_list': zoo}
    return render(request, 'zooproject/zoo_list.html', context)


def zoo_create_view(request):
    form = ZooForm()
    if request.method == 'POST':
        form = ZooForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.date_of_added = timezone.now()
            form.save()
            form = ZooForm()
        else:
            form = ZooForm()
    return render(request, 'zooproject/zoo_create.html', {'form': form})