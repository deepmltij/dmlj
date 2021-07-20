"""dmlj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from dmljmodel import views
from dmljmodel.views import download_template,download_test_one,download_test_two,download_test_three,download_test_four
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dmlj/',views.dmlj),
    path('test_action/',views.test_action),
    path('download_template/',download_template),   
    path('download_test_one/',download_test_one),
    path('download_test_two/',download_test_two),
    path('download_test_three/',download_test_three),
    path('download_test_four/',download_test_four),
]
