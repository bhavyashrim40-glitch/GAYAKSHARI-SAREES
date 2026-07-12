from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views # ಇದನ್ನು ಇಲ್ಲಿ ಸೇರಿಸಲಾಗಿದೆ

urlpatterns = [
    path('admin/', admin.site.urls), # ಅಡ್ಮಿನ್ ಪುಟಕ್ಕೆ ದಾರಿ
    path('', views.home, name='home'), # ನೇರವಾಗಿ views.home ಗೆ ಲಿಂಕ್ ಮಾಡಲಾಗಿದೆ
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('order/<int:product_id>/', views.place_order_view, name='place_order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)