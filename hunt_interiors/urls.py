from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from testimonial.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('testimonial/', include('testimonial.urls', namespace='testimonial')),
    path('testament/', include('testament.urls')),
    path('sitemap.xml', sitemap, {
        'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
