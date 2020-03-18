from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/chinagate/timeline/', views.cg_timeline),
    path('/chinagate/archive/', views.cg_ar),
    path('/chinagate/factcheck/', views.cg_fact),
]

