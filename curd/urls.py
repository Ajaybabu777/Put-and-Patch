
from django.urls import path, include
from.views import post,put,patch

urlpatterns = [
    path('post/',post),
    path('put/',put),
    path('patch/',patch)
] 