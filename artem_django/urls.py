"""artem_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpRequest, HttpResponse

# home page
def home_text(request: HttpRequest) -> HttpResponse:
    """
    function out put text on home page
    :param request:
    :return: str
    """
    return HttpResponse("Это домашняя страница с статичным текстом !")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("homepage", home_text),
    path("home/", home_text),
    path("", home_text),
]
