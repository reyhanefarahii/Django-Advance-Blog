from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    path('cbv-index', RedirectView.as_view(pattern_name="blog:cbv-index"),name='redirect-to-index'),
    path('post/', views.PostListView.as_view(),name="post-index"),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name="post-detail"),
    path('post/create/',views.PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/edit/',views.PostEditView.as_view(),name="post-edit"),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(),name="post-delete"),
    
    # path('go-to-maktabkhooneh', RedirectView.as_view(url='https://maktabkhooneh.com'),name='redirext-to-maktabkhooneh'),

    # # Function Base View
     
        # path('fbv-index', views.indexView, name='fbv-index'),
        # path('cbv-index', TemplateView.as_view(template_name="index.html",extra_context={"name":"ali"})),
        # path('cbv-index', views.IndexView.as_view(),name="cbv-index"),
    path('go-to-index1', views.RedirectToMaktab.as_view(), name='redirect-to-maktabkhooneh'),
]

    