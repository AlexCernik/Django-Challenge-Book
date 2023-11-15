from rest_framework import routers
from .views import BookView

router = routers.SimpleRouter()
router.register(r'book', BookView)
urlpatterns = router.urls
