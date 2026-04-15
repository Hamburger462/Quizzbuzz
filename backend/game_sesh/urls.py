from rest_framework.routers import DefaultRouter
from .views import GameSessionViewSet, PlayerViewSet, PlayerAnswerViewSet

router = DefaultRouter()
router.register(r"sessions", GameSessionViewSet)
router.register(r"players", PlayerViewSet)
router.register(r"answers", PlayerAnswerViewSet)

urlpatterns = router.urls