from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("products",views.ProductsView,basename='Products')
urlpatterns = []

urlpatterns += router.urls