from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("users",views.UsersView,basename="users")




urlpatterns =[
    path('register/',views.RegisterUserView.as_view(),name="register"),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token-refresh'),  
    path('logout/', views.LogoutView.as_view(), name='logout'),

]

urlpatterns += router.urls