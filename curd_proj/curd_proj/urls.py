from django.contrib import admin
from django.urls import path

# this two libraries for image upload
from django.conf import settings
from django.conf.urls.static import static

# this is for productsapp
from products.views import * 

urlpatterns = [
    # path('', products, name='products'),
    # path('success-page/', success_page, name='success_page'),
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    # this is for image media
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

