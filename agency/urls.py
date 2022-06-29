from django.contrib import admin
from django.urls import path, include

import Products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', include('CRM.urls')),
    path('users/', include('Users.urls')),
    path('', include('Products.urls')),
    path('accounts/', include('allauth.urls'))
]
