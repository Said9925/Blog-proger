from django.urls import path

from proger.views import HomeView, login, signup, ShowPostView, CategoryView, AbbPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:cat_slug>/', CategoryView.as_view(), name='category'),
    path('post/<slug:post_slug>/', ShowPostView.as_view(), name='post'),
    path('add_post/', AbbPostView.as_view(), name='add_post'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
]
