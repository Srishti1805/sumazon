from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("products",views.ProductsView,basename='Products')
router.register("order",views.OrderView,basename='Order')
urlpatterns = []

urlpatterns += router.urls