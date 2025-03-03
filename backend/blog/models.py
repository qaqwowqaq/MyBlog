from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from django.utils.text import slugify

class UserProfile(models.Model):
    """用户扩展资料模型"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='用户')
    avatar = models.ImageField(upload_to='avatars/%Y/%m', blank=True, verbose_name='头像')
    bio = models.TextField(max_length=500, blank=True, verbose_name='个人简介')
    website = models.URLField(blank=True, verbose_name='个人网站')
    location = models.CharField(max_length=50, blank=True, verbose_name='所在地')
    
    # 社交媒体链接
    github = models.CharField(max_length=255, blank=True, verbose_name='GitHub')
    twitter = models.CharField(max_length=255, blank=True, verbose_name='Twitter')
    weibo = models.CharField(max_length=255, blank=True, verbose_name='微博')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        verbose_name = '用户资料'
        verbose_name_plural = '用户资料'
        
    def __str__(self):
        return self.user.username

class Category(models.Model):
    """文章分类模型"""
    name = models.CharField(max_length=100, unique=True, verbose_name='分类名')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='分类别名')
    description = models.TextField(blank=True, verbose_name='分类描述')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, 
                              related_name='children', verbose_name='父分类')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['name']
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Tag(models.Model):
    """文章标签模型"""
    name = models.CharField(max_length=50, unique=True, verbose_name='标签名')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='标签别名')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'
        ordering = ['name']
    
    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Post(models.Model):
    """博客文章模型"""
    STATUS_CHOICES = (
        ('draft', '草稿'),
        ('published', '已发布'),
    )
    
    title = models.CharField(max_length=255, verbose_name='标题')
    slug = models.SlugField(max_length=255, unique_for_date='published_at', verbose_name='文章别名')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='作者')
    body = models.TextField(verbose_name='正文内容')
    body_html = models.TextField(blank=True, verbose_name='HTML内容') # 存储转换后的HTML内容
    summary = models.TextField(blank=True, verbose_name='摘要')
    
    published_at = models.DateTimeField(default=timezone.now, verbose_name='发布时间')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='状态')
    
    categories = models.ManyToManyField(Category, blank=True, related_name='posts', verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='标签')
    
    views = models.PositiveIntegerField(default=0, verbose_name='浏览量')
    likes = models.PositiveIntegerField(default=0, verbose_name='点赞数')
    comments_count = models.PositiveIntegerField(default=0, verbose_name='评论数')
    
    # SEO优化字段
    meta_description = models.CharField(max_length=160, blank=True, verbose_name='Meta描述')
    meta_keywords = models.CharField(max_length=255, blank=True, verbose_name='Meta关键词')
    
    # 是否允许评论
    allow_comments = models.BooleanField(default=True, verbose_name='允许评论')
    
    # 置顶文章
    is_pinned = models.BooleanField(default=False, verbose_name='置顶')
    
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-is_pinned', '-published_at']
        
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
            self.published_at.year,
            self.published_at.month,
            self.published_at.day,
            self.slug
        ])
        
    def update_comments_count(self):
        """更新评论数量"""
        self.comments_count = self.comments.filter(active=True).count()
        self.save()

class Comment(models.Model):
    """评论模型"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='文章')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='comments', verbose_name='用户')
    name = models.CharField(max_length=80, verbose_name='评论者')
    email = models.EmailField(verbose_name='邮箱')
    body = models.TextField(verbose_name='评论内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    active = models.BooleanField(default=True, verbose_name='是否显示')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies', verbose_name='父评论')
    
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
        ordering = ['created_at']
        
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # 更新文章评论数
        self.post.update_comments_count()

class SiteSetting(models.Model):
    """站点设置模型"""
    title = models.CharField(max_length=255, verbose_name='网站标题')
    subtitle = models.CharField(max_length=255, blank=True, verbose_name='网站副标题')
    description = models.TextField(blank=True, verbose_name='网站描述')
    keywords = models.CharField(max_length=255, blank=True, verbose_name='网站关键词')
    logo = models.ImageField(upload_to='site/', blank=True, verbose_name='网站Logo')
    favicon = models.ImageField(upload_to='site/', blank=True, verbose_name='网站图标')
    
    # 社交媒体链接
    github = models.URLField(blank=True, verbose_name='GitHub')
    twitter = models.URLField(blank=True, verbose_name='Twitter')
    weibo = models.URLField(blank=True, verbose_name='微博')
    
    # 备案信息
    icp = models.CharField(max_length=30, blank=True, verbose_name='ICP备案号')
    
    # 统计代码
    analytics_code = models.TextField(blank=True, verbose_name='统计代码')
    
    # 底部信息
    footer_info = models.TextField(blank=True, verbose_name='底部信息')
    
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        verbose_name = '站点设置'
        verbose_name_plural = '站点设置'
        
    def __str__(self):
        return self.title

class Link(models.Model):
    """友情链接模型"""
    name = models.CharField(max_length=100, verbose_name='链接名称')
    url = models.URLField(verbose_name='链接地址')
    logo = models.ImageField(upload_to='links/', blank=True, verbose_name='链接Logo')
    description = models.CharField(max_length=255, blank=True, verbose_name='链接描述')
    is_active = models.BooleanField(default=True, verbose_name='是否启用')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'
        ordering = ['name']
        
    def __str__(self):
        return self.name