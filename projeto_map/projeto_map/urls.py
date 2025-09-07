from django.contrib import admin
from django.urls import path
from artistas.views import LoginView, sim

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'), 
    path('sim/', sim.as_view(), name='sim'),
]
