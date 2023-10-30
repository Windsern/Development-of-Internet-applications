"""Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# urls.py - соответствие урлам обработчиков(views)
# templates - папка для шаблонов (html-файлы)
from django.contrib import admin
from django.urls import path

from bmstu_lab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.GetBuilds),
    path('build/<int:id>/', views.GetBuild, name='build_url'),
    path('', views.GetBuilds, name='building'),

    # Для работы с изменением статуса в здания (услуги) нужна работа с БД
    path('delete_building/', views.delete_building, name='delete_building'),

    # path('', views.bookList),
    # path('book/<int:id>/', views.GetBook, name='book_url')
]
