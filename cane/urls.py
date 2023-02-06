from django.urls import path
from . import views
from .views import home_page_view

urlpatterns = [
    path('', views.home),
    path('foto/', views.foto),
    path('contatti/', views.contatti),
    path('blog/', views.blog),
    path('', home_page_view, name='home'),
]

