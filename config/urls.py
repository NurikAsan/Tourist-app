from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
# from apps.tour.views import PushApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.tour.urls'))
]

swagger_url = [
    path('swagger/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/token/register/', FCMDeviceAuthorizedViewSet.as_view({"post": "create"})),
    # path('api/v1/send_message', PushApi.as_view())
]

urlpatterns += swagger_url
urlpatterns += debug_toolbar_urls()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
