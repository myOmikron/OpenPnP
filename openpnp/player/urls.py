from django.urls import path
from player.views import *

urlpatterns = [
    path('', PlayerView.as_view()),
]
