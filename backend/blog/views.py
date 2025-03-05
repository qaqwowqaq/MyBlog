from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Category, Tag, Post, Comment, UserProfile, SiteSetting, Link
from .serializers import (
    UserSerializer, UserProfileSerializer, CategorySerializer, 
    TagSerializer, PostListSerializer, PostDetailSerializer,
    CommentSerializer, SiteSettingSerializer, LinkSerializer,UserRegistrationSerializer,LoginSerializer
)
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView

@extend_schema(
    tags=['Authentication'],
    request=LoginSerializer,
    responses={200: LoginSerializer},
    description='用户登录接口，返回JWT令牌'
)
class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

# 自定义获取Token视图
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

@extend_schema(
    tags=['Authentication'],
    request= UserRegistrationSerializer,
    description='用户注册接口，无需认证',
    auth=[],  # 明确指定不需要认证
    responses={201: UserRegistrationSerializer}
)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """用户注册API"""
    serializer = UserRegistrationSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()
        UserProfile.objects.create(user=user)
        return Response({
            'username': user.username,
            'email': user.email,
            'message': '注册成功'
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def current(self, request):
        """获取当前登录用户信息"""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status='published')
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostDetailSerializer
    
    def get_queryset(self):
        """自定义查询集以支持过滤"""
        queryset = Post.objects.filter(status='published')
        
        # 搜索功能
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(body__icontains=search_query)
            )
        
        # 分类过滤
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(categories__slug=category)
        
        # 标签过滤
        tag = self.request.query_params.get('tag', None)
        if tag:
            queryset = queryset.filter(tags__slug=tag)
            
        # 作者过滤
        author = self.request.query_params.get('author', None)
        if author:
            queryset = queryset.filter(author__username=author)
            
        return queryset
    
    @action(detail=True, methods=['post'])
    def like(self, request, slug=None):
        """文章点赞功能"""
        post = self.get_object()
        post.likes += 1
        post.save()
        return Response({'status': 'liked', 'likes': post.likes})
    
    @action(detail=True, methods=['post'])
    def view(self, request, slug=None):
        """增加文章浏览量"""
        post = self.get_object()
        post.views += 1
        post.save()
        return Response({'status': 'viewed', 'views': post.views})

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(active=True)
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        """创建评论时自动关联当前用户"""
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()

class SiteSettingView(generics.RetrieveAPIView):
    """获取网站设置信息"""
    queryset = SiteSetting.objects.all()
    serializer_class = SiteSettingSerializer
    permission_classes = [AllowAny]
    
    def get_object(self):
        # 总是返回第一个设置对象或创建一个默认的
        setting = SiteSetting.objects.first()
        if not setting:
            setting = SiteSetting.objects.create(
                title="我的博客",
                subtitle="一个Django博客系统"
            )
        return setting

class LinkListView(generics.ListAPIView):
    """获取所有友情链接"""
    queryset = Link.objects.filter(is_active=True)
    serializer_class = LinkSerializer
    permission_classes = [AllowAny]