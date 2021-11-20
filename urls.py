from django.contrib import admin
from django.urls import path, include
from register import views as v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name="register"),
    path('', include("main.urls")),
    path('', include("django.contrib.auth.urls")),


    url(r'^media/(?P<path>.*)$', serve,
        {'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]
