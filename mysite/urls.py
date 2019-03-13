"""mysite URL Configuration

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
import requests
my_domain = 'sd55.pythonanywhere.com'
username = 'sd55'
token = 'f8594b58636acfca44912b3afa7637d02b1ea1b9'

urlpatterns = [
    path('admin/', admin.site.urls),
]
response = requests.post(
  'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
      username=username, domain=my_domain
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
  print('All OK')
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))