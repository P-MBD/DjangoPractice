from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    #path('fbv-index', indexView, name="fbv+index"),
    #path('cbv-index', TemplateView.as_view(template_name="index.html", extra_context={"name":"ali"}))
     path('cbv-index', views.IndexView.as_view(),name="index")
]