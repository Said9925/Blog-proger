from django.urls import path

from proger.views import HomeView,  ShowPostView, CategoryView, AbbPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:cat_slug>/', CategoryView.as_view(), name='category'),
    path('post/<slug:post_slug>/', ShowPostView.as_view(), name='post'),
    path('add_post/', AbbPostView.as_view(), name='add_post'),
]
