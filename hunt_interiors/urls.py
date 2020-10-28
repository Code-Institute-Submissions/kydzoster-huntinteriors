from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('home.urls')),
    path('gallery/', include('gallery.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('testaments/', include('testaments.urls')),
    path('products/', include('furnitures.urls')),
    path('services/', include('services.urls')),
    path('bag/', include('bag.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
