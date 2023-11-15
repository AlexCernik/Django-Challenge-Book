from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('app_book.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/signin/', include('dj_rest_auth.registration.urls'))
]