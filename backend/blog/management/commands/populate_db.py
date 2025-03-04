from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Category, Tag, Post, Comment, UserProfile, SiteSetting, Link
from django.utils import timezone
import random

class Command(BaseCommand):
    help = '填充博客系统的测试数据'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('开始填充测试数据...'))
        
        # 创建管理员用户（如果不存在）
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            UserProfile.objects.create(user=admin, bio='网站管理员')
            self.stdout.write(self.style.SUCCESS('创建管理员用户: admin/admin123'))
        
        # 创建普通用户
        test_user = User.objects.create_user('testuser', 'test@example.com', 'test123')
        UserProfile.objects.create(user=test_user, bio='测试用户')
        self.stdout.write(self.style.SUCCESS('创建测试用户: testuser/test123'))
        
        # 创建分类
        categories = []
        for cat in ['技术', '生活', '随笔', '前端', '后端', 'Python', 'JavaScript']:
            category, created = Category.objects.get_or_create(
                name=cat,
                defaults={'slug': cat.lower(), 'description': f'{cat}分类的文章'}
            )
            categories.append(category)
        self.stdout.write(self.style.SUCCESS('创建分类完成'))
        
        # 创建标签
        tags = []
        for tag_name in ['Django', 'Flask', 'React', 'Vue', 'Node.js', '数据库', '学习笔记', '教程']:
            tag, created = Tag.objects.get_or_create(
                name=tag_name,
                defaults={'slug': tag_name.lower()}
            )
            tags.append(tag)
        self.stdout.write(self.style.SUCCESS('创建标签完成'))
        
        # 创建文章
        posts = []
        for i in range(1, 11):
            post = Post.objects.create(
                title=f'测试文章 {i}',
                slug=f'test-post-{i}',
                author=admin if i % 2 == 0 else test_user,
                body=f'这是第 {i} 篇测试文章的内容...\n\n'
                    f'这是正文部分，包含一些格式化的内容。\n\n'
                    f'## 小标题\n\n'
                    f'- 列表项1\n'
                    f'- 列表项2\n\n'
                    f'这是结尾部分。',
                body_html=f'<p>这是第 {i} 篇测试文章的内容...</p>'
                    f'<p>这是正文部分，包含一些格式化的内容。</p>'
                    f'<h2>小标题</h2>'
                    f'<ul>'
                    f'<li>列表项1</li>'
                    f'<li>列表项2</li>'
                    f'</ul>'
                    f'<p>这是结尾部分。</p>',
                summary=f'这是第 {i} 篇测试文章的摘要...',
                status='published',
                views=random.randint(10, 100),
                likes=random.randint(0, 30),
                is_pinned=True if i <= 2 else False
            )
            # 添加分类和标签
            post.categories.add(random.choice(categories))
            post.tags.add(random.choice(tags))
            post.save()
            posts.append(post)
        self.stdout.write(self.style.SUCCESS('创建文章完成'))
        
        # 创建评论
        for post in posts:
            for i in range(random.randint(1, 5)):
                Comment.objects.create(
                    post=post,
                    user=random.choice([admin, test_user]),
                    name=f'评论者 {i}',
                    email=f'commenter{i}@example.com',
                    body=f'这是文章《{post.title}》的第 {i} 条评论。',
                    active=True
                )
        self.stdout.write(self.style.SUCCESS('创建评论完成'))
        
        # 创建站点设置
        SiteSetting.objects.create(
            title='我的博客',
            subtitle='个人技术博客',
            description='这是一个基于Django开发的个人博客系统',
            keywords='博客,技术,Python,Django',
            footer_info='© 2025 我的博客 版权所有'
        )
        self.stdout.write(self.style.SUCCESS('创建站点设置完成'))
        
        # 创建友情链接
        Link.objects.create(
            name='Django官网',
            url='https://www.djangoproject.com/',
            description='Django官方网站'
        )
        Link.objects.create(
            name='Python官网',
            url='https://www.python.org/',
            description='Python编程语言官网'
        )
        self.stdout.write(self.style.SUCCESS('创建友情链接完成'))
        
        self.stdout.write(self.style.SUCCESS('所有测试数据填充完成!'))