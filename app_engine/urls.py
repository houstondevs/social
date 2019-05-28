from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns
from app_engine import settings
from django.conf.urls.static import static
from .views import main_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_users.urls')),
    path('', main_page, name='main_page_url'),
    path('blog/', include('app_blog.urls')),
]

urlpatterns +=  staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)