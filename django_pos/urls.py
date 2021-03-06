"""django_pos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django_pos import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pos/', include('pos.urls')),
    path('', include('pos.urls')),
    path('invoice/', include('invoice.urls')),
    path('registration/', include('customer_onboarding.urls')),

    url(r'^face$', app_views.index),
    url(r'^error_image$', app_views.errorImg),
    url(r'^create_dataset$', app_views.create_dataset),
    url(r'^trainer$', app_views.trainer),
    url(r'^eigen_train$', app_views.eigenTrain),
    url(r'^detect$', app_views.detect),
    url(r'^detect_image$', app_views.detectImage),
    # url(r'^admin/', admin.site.urls),
    url(r'^records/', include('records.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
