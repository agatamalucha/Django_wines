from django.urls import path, include
from wines.views import my_wines, search_wine

app_name = "wines"


urlpatterns = [
    path("", my_wines, name="my-wines"),
    path("search-wine", search_wine, name="search-wine"),
    ]

