
from django.urls import path, include
from.views import post,put,patch,ajay


urlpatterns = [
    path('post/',post),
    path('put/',put),
    path('patch/',patch),
    path('ajay/',ajay),

] 