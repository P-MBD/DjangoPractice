from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)



app_name = 'api-v1'
urlpatterns =[
    #registration
    path('registration/',views.RegistrationApiView.as_view(), name='registration' ),
    path('token/login/', views.CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout',views.CustomDiscardAuthToken.as_view(), name='token-logout'),
    #change password
    #reset password
    #login token
    #login jwt
    path('api/token/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('api/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('api/verify',TokenVerifyView.as_view(), name='jwt-verify')
]