"""django_issuetracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from issuetracker.views import get_issue_list, create_an_issue, edit_an_issue ,toggle_status

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_issue_list),
    url(r'^add$', create_an_issue),
    url(r'^edit/(?P<id>\d+)$', edit_an_issue),
    url(r'^toggle/(?P<id>\d+)$', toggle_status)
]