"""fusion URL Configuration

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

from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views

from fusion.service.views import (CategoryViewSet, PartnerViewSet)


router = routers.DefaultRouter()
router.register(r'partners', PartnerViewSet)
router.register(r'categories', CategoryViewSet)

# GHETTO ASS SHIT
engagements_mapping = {'delete': 'engagements', 'patch': 'engagements'}
engagements_view = PartnerViewSet.as_view(engagements_mapping)

comments_mapping = {'delete': 'comments', 'patch': 'comments'}
comments_view = PartnerViewSet.as_view(comments_mapping)

contacts_mapping = {'delete': 'contacts', 'patch': 'contacts'}
contacts_view = PartnerViewSet.as_view(contacts_mapping)

links_mapping = {'delete': 'links', 'patch': 'links'}
links_view = PartnerViewSet.as_view(links_mapping)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^partners/(?P<pk>[^/.]+)/engagements/(?P<engagement_id>[^/.]+)/$', engagements_view),
    url(r'^partners/(?P<pk>[^/.]+)/comments/(?P<comment_id>[^/.]+)/$', comments_view),
    url(r'^partners/(?P<pk>[^/.]+)/contacts/(?P<contact_id>[^/.]+)/$', contacts_view),
    url(r'^partners/(?P<pk>[^/.]+)/links/(?P<link_id>[^/.]+)/$', 
        links_view),
    path('admin/', admin.site.urls),
    url(r'^api-token-auth/', views.obtain_auth_token),
]
