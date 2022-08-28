
from django.contrib import admin
from django.urls import path
from asosiy.views import *
from stats.views import *
from user.views import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Bu loyha Omborxona uchun klon qilib ishlatilaishi mumkin",
      contact=openapi.Contact(email="Muhammadjonov Muhammadali: <Bekruhblog@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientlar/', ClienApiView.as_view()),
    path('client/<int:pk>/', ClientRUD.as_view()),
    path('mahsulotlar/', MahsulotApiView.as_view()),
    path('mahsulot/<int:pk>/', MahsulotRUD.as_view()),
    path('stats/', StatsApiView.as_view()),
    path('stats/<int:pk>/', StatsRUD.as_view()),
    path('omborlar/', OmborApiView.as_view()),
    path('ombor/<int:pk>/', OmborRUD.as_view()),
    path('token-ber/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-doc'),
]
