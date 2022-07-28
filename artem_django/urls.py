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
def check_password(request: HttpRequest, user_password) -> HttpResponse:
    """
    function checking if password put correct with allow symbol and length >= 8
    :param request:
    :param user_password:str
    :return:if all correct -> password
            if not -> Error in password
    """
    # set(password) - to reduce iteration of characters
    unique_password = set(user_password)
    # if symbol in password is incorrect -> Error
    if any(mark not in accepted_signs for mark in unique_password):
        return HttpResponse("Пу пу пууу, Вы использовали запрещенный символ!")
    # if length of password < 8
    elif len(user_password) < 8:
        return HttpResponse("Пароль должен быть не меньше  8-ми символов")
    # if all is good -> out put that password saved
    else:
        return HttpResponse("Пароль {} сохранён".format(user_password))
def ganerate_password(request: HttpRequest, length: int) -> HttpResponse:
    """
    function generate
    :param request:
    :param length:int: how long we want password but not less 8
    :return:
    """
    password = ''
    if int(length) < 8:
        return HttpResponse("Пароль должен не меньше 8-ми символов")
    else:
        while len(password) != int(length):
            password += choice(accepted_signs)
        return HttpResponse(f"Your password is {password}")



urlpatterns = [
    path('admin/', admin.site.urls),
    path("homepage", home_text),
    path("home/", home_text),
    path("", home_text),
    path("password/<str:user_password>/", check_password),
    path("password/generate/<int:length>", ganerate_password),

]
