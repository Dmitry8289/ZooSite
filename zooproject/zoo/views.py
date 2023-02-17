from django.shortcuts import render

from zoo.models import Zoo


def zoo_list_view(request):
    zoo = Zoo.objects.all()
    context = {'zoo_list': zoo}
    return render(request, 'zooproject/zoo_list.html', context)