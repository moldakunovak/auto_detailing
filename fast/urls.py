from django.urls import path
from .views import *
urlpatterns = [
    path('', index_page, name='index'),
    path("create/post/", CreatePostView.as_view(), name="create_post"),
    path("detail/post/<int:pk>/", DetailPostView.as_view(), name="detail_post"),
    path('update/<int:id>/', update_author, name='author_update'),
    path('delete/<int:id>/', delete_author, name='author_delete'),
]