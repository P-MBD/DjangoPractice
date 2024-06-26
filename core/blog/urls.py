from django.urls import path,include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
app_name = "blog"
urlpatterns = [
    #path('fbv-index', indexView, name="fbv+index"),
    #path('cbv-index', TemplateView.as_view(template_name="index.html", extra_context={"name":"ali"}))
     path('cbv-index', views.IndexView.as_view(),name="index"),
     path('post/',views.PostList.as_view(), name="post-list"),
     path('go-to-maktabkhooneh/<int:pk>/', views.RedirectToMaktab.as_view(), name='redirect-to-maktabkhooneh'),  
     path('post/',views.PostList.as_view(), name='post-list'),
     path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
     path('post/create/',views.PostCreateView.as_view(),name='post-create'),
     path('post/<int:pk>/edit/',views.PostEditView.as_view(), name='post-edit'),
     path('post/<int:pk>/delete/',views.PostDeleteView.as_view(), name='post-delete'),
     path('api/v1/',include('blog.api.v1.urls'))
]