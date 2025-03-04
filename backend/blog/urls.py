from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet, CategoryViewSet, TagViewSet, PostViewSet, 
    CommentViewSet, SiteSettingView, LinkListView, CustomAuthToken, register_user
)
# 该文件定义了博客应用的 URL 配置，包括用户、分类、标签、文章、评论、站点设置和友情链接等资源的 URL 配置。

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('site-settings/', SiteSettingView.as_view(), name='site-settings'),
    path('links/', LinkListView.as_view(), name='links'),
    path('auth/token/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('auth/register/', register_user, name='register'),
]