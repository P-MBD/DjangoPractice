from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter,SimpleRouter
app_name = "api-v1"

router = SimpleRouter()
router.register('post', views.PostModelViewSet,basename ='post')
router.register('category',views.CategoryModelViewSet, basename='category')
urlpatterns = router.urls

# urlpatterns = [  
#     # path('post/',views.PostViewSet.as_view({'get':'list','post':'create'}),name='post-list'),
#     # path('post/<int:pk>/',views.PostViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}),name='post-detail'),  
#    ]
