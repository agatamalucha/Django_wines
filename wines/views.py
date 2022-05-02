from django.shortcuts import render
from wines.models import WineModel
from django.contrib.auth.decorators import login_required




# @login_required
def my_wines(request):
    wines = WineModel.objects.all()
    wine_types = WineModel.objects.values_list("strain", flat=True).distinct()
    return render(request, "my-wines.html", {"wines": wines,"wine_types": wine_types})


@login_required
def search_wine(request):
    queryset = WineModel.objects.filter(strain__contains=request.GET['query'])

    wine_types = WineModel.objects.values_list("strain", flat=True).distinct()


    return render(request, "my-wines.html", {"queryset": queryset, "wine_types": wine_types})



