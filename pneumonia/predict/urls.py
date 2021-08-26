from django.urls import path
from . import views

app_name = "predict"

urlpatterns = [
    path('', views.predict, name='prediction_page'),
    path('compute/', views.compute, name='compute'),
    # path('results/', views.view_results, name='results'),
]
