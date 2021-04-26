from django.urls import path
from .views import product_list, item_list, SaveFile

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('product/', product_list),
    path('item/', item_list),
    path('SaveFile/', SaveFile)
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
