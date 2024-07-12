from django.contrib import admin
from django.urls import path, include
from films import views as films_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', films_views.home, name='home'),
    path('films/', include('films.urls')),
]
