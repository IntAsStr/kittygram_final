from django.urls import include, path
from rest_framework import routers
from cats.views import AchievementViewSet, CatViewSet

router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('token/', include('rest_framework.authtoken.urls')),
]
