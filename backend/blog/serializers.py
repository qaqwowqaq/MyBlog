from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Tag, Post, Comment, UserProfile, SiteSetting, Link
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# login serializer负责验证用户登录信息，返回access token和refresh token
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True, style={'input_type': 'password'})
    access = serializers.CharField(read_only=True) 
    refresh = serializers.CharField(read_only=True)
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        if not username or not password:
            raise serializers.ValidationError("用户名和密码不能为空")
        
        user = authenticate(username=username, password=password)
        
        if not user:
            raise serializers.ValidationError("用户名或密码错误")
        
        if not user.is_active:
            raise serializers.ValidationError("用户已被禁用")
        
        refresh = RefreshToken.for_user(user)
        
        return {
            'username': user.username,
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user_id': user.id
        }
    
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "两次密码不匹配"})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'avatar', 'bio', 'website', 'location', 'github', 'twitter', 'weibo']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'parent']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'name', 'email', 'body', 'created_at', 'parent', 'replies']

    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.filter(active=True), many=True).data
        return []

class PostListSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'author', 'summary', 'published_at', 
            'status', 'categories', 'tags', 'views', 'likes', 'comments_count', 'is_pinned'
        ]

class PostDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'author', 'body', 'body_html', 'summary',
            'published_at', 'created_at', 'updated_at', 'status', 'categories',
            'tags', 'views', 'likes', 'comments_count', 'meta_description',
            'meta_keywords', 'allow_comments', 'is_pinned', 'comments'
        ]
    
    def get_comments(self, obj):
        # 只获取顶级评论（没有父评论的）
        comments = obj.comments.filter(active=True, parent=None)
        return CommentSerializer(comments, many=True).data

class SiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'name', 'url', 'logo', 'description', 'is_active']