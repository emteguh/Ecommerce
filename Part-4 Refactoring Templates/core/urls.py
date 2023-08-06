from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include('account.urls', namespace='account')),
    path("basket/", include('basket.urls', namespace='basket')),
    path("payment/", include('payment.urls', namespace='payment')),
    path("orders/", include('orders.urls', namespace='orders')),
    path("", include('store.urls', namespace='store')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
