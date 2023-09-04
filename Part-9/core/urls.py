from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls", namespace="account")),
    path("basket/", include("basket.urls", namespace="basket")),
    path("checkout/", include("checkout.urls", namespace="checkout")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("", include("store.urls", namespace="store")),
    path('paypal/', include('paypal.standard.ipn.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
