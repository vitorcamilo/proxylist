"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from scrape import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IpListView.as_view(), name='index'),
    path('create/', views.CreateIPView.as_view(), name='create'),
    path('<int:pk>/detail', views.IPDetailView.as_view(), name='ipdetail'),
    path('<int:pk>/update', views.UpdateIPView.as_view(), name='update'),
    path('<int:pk>/delete', views.DeleteIPView.as_view(), name='delete'),
    path('deleteall', views.delete_ips, name='allipdelete'),
    path('crawl', views.run_ip_scraper, name='crawlip')
]
