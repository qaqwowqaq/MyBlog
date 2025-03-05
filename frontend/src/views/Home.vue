<template>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
  <div class="min-h-screen bg-white">
    <!-- 顶部英雄区域 -->
    <section class="relative py-24 bg-gradient-to-r from-indigo-600 to-purple-600 text-white overflow-hidden">
      <div class="absolute inset-0 z-0 opacity-10">
        <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1499750310107-5fef28a66643')] bg-cover bg-center"></div>
      </div>
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="text-center">
          <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold mb-6 tracking-tight">探索想法，分享知识</h1>
          <p class="text-xl max-w-3xl mx-auto mb-8 text-indigo-100">欢迎来到我的博客空间，这里记录了我的思考、学习和成长</p>
          <div class="flex flex-wrap justify-center gap-4">
            <router-link to="/posts" class="bg-white text-indigo-600 hover:bg-indigo-50 font-medium px-6 py-3 rounded-lg shadow-lg transition duration-300">
              浏览文章
            </router-link>
            <router-link to="/about" class="bg-transparent border border-white text-white hover:bg-white/10 px-6 py-3 rounded-lg transition duration-300">
              了解更多
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- 特色内容区 -->
    <section class="py-16 bg-gray-50">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-gray-900 mb-8 text-center">精选文章</h2>
        
        <div v-if="!isLoading" class="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <!-- 主要特色文章 -->
          <div v-if="featuredPost" class="lg:col-span-2 group">
            <div class="bg-white rounded-xl overflow-hidden shadow-md h-full transition-all duration-300 hover:shadow-xl">
              <div class="aspect-w-16 aspect-h-9 overflow-hidden">
                <img 
                  :src="featuredPost.cover_image || getRandomImage(featuredPost.title)" 
                  :alt="featuredPost.title"
                  class="object-cover w-full h-full transition-transform duration-500 group-hover:scale-105"
                >
              </div>
              <div class="p-6">
                <div class="flex items-center gap-3 mb-3 text-sm">
                  <span class="bg-indigo-100 text-indigo-800 px-2.5 py-0.5 rounded-full">{{ featuredPost.category }}</span>
                  <span class="text-gray-500">{{ formatDate(featuredPost.created_at) }}</span>
                </div>
                <h3 class="text-2xl font-bold mb-3 text-gray-900">
                  <router-link :to="`/post/${featuredPost.slug}`" class="hover:text-indigo-600 transition duration-300">
                    {{ featuredPost.title }}
                  </router-link>
                </h3>
                <p class="text-gray-600 mb-6 line-clamp-3">{{ featuredPost.summary }}</p>
                <div class="flex justify-between items-center">
                  <div class="flex items-center gap-2">
                    <img :src="getAvatarUrl(featuredPost.author)" alt="Author" class="w-8 h-8 rounded-full">
                    <span class="text-sm text-gray-700">{{ featuredPost.author }}</span>
                  </div>
                  <div class="text-sm text-gray-500 flex items-center gap-4">
                    <span class="flex items-center">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
                        <path d="M10 12a2 2 0 100-4 2 2 0 000 4z" />
                        <path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd" />
                      </svg>
                      {{ featuredPost.views }}
                    </span>
                    <span class="flex items-center">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd" />
                      </svg>
                      {{ featuredPost.likes }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <!-- 次要特色文章 -->
          <div class="lg:col-span-1 space-y-8">
            <div v-for="post in secondaryPosts" :key="post.id" class="bg-white rounded-xl overflow-hidden shadow-md group transition-all duration-300 hover:shadow-xl">
              <div class="aspect-w-16 aspect-h-9 overflow-hidden">
                <img 
                  :src="post.cover_image || getRandomImage(post.title)" 
                  :alt="post.title"
                  class="object-cover w-full h-full transition-transform duration-500 group-hover:scale-105"
                >
              </div>
              <div class="p-5">
                <div class="flex items-center gap-2 mb-2 text-xs">
                  <span class="bg-indigo-100 text-indigo-800 px-2 py-0.5 rounded-full">{{ post.category }}</span>
                  <span class="text-gray-500">{{ formatDate(post.created_at) }}</span>
                </div>
                <h3 class="text-lg font-bold mb-2 text-gray-900">
                  <router-link :to="`/post/${post.slug}`" class="hover:text-indigo-600 transition duration-300">
                    {{ post.title }}
                  </router-link>
                </h3>
                <p class="text-gray-600 text-sm line-clamp-2">{{ post.summary }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- 加载骨架屏 -->
        <div v-else class="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div class="lg:col-span-2">
            <div class="bg-white rounded-xl overflow-hidden shadow-md h-full">
              <div class="w-full h-64 bg-gray-200 animate-pulse"></div>
              <div class="p-6">
                <div class="h-4 bg-gray-200 rounded animate-pulse mb-3 w-1/4"></div>
                <div class="h-8 bg-gray-200 rounded animate-pulse mb-3"></div>
                <div class="h-4 bg-gray-200 rounded animate-pulse mb-2"></div>
                <div class="h-4 bg-gray-200 rounded animate-pulse mb-2"></div>
                <div class="h-4 bg-gray-200 rounded animate-pulse mb-6 w-3/4"></div>
                <div class="flex justify-between items-center">
                  <div class="h-8 bg-gray-200 rounded-full animate-pulse w-24"></div>
                  <div class="h-4 bg-gray-200 rounded animate-pulse w-16"></div>
                </div>
              </div>
            </div>
          </div>
          <div class="lg:col-span-1 space-y-8">
            <div v-for="i in 2" :key="i" class="bg-white rounded-xl overflow-hidden shadow-md">
              <div class="w-full h-36 bg-gray-200 animate-pulse"></div>
              <div class="p-5">
                <div class="h-3 bg-gray-200 rounded animate-pulse mb-2 w-1/3"></div>
                <div class="h-5 bg-gray-200 rounded animate-pulse mb-2"></div>
                <div class="h-3 bg-gray-200 rounded animate-pulse mb-1"></div>
                <div class="h-3 bg-gray-200 rounded animate-pulse w-2/3"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 最新文章区 -->
    <section class="py-16 bg-white">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center mb-10">
          <h2 class="text-3xl font-bold text-gray-900">最新文章</h2>
          <router-link to="/posts" class="text-indigo-600 hover:text-indigo-800 font-medium flex items-center transition duration-300">
            查看全部
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </router-link>
        </div>
        
        <div v-if="!isLoading" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="post in latestPosts" :key="post.id" class="bg-white border border-gray-100 rounded-xl overflow-hidden shadow-sm group hover:shadow-md transition-all duration-300">
            <div class="aspect-w-16 aspect-h-9 overflow-hidden">
              <img 
                :src="post.cover_image || getRandomImage(post.title)" 
                :alt="post.title"
                class="object-cover w-full h-full transition-transform duration-500 group-hover:scale-105"
              >
            </div>
            <div class="p-5">
              <div class="flex items-center gap-2 mb-2 text-xs">
                <span class="bg-indigo-100 text-indigo-800 px-2 py-0.5 rounded-full">{{ post.category }}</span>
                <span class="text-gray-500">{{ formatDate(post.created_at) }}</span>
              </div>
              <h3 class="text-lg font-bold mb-2 text-gray-900">
                <router-link :to="`/post/${post.slug}`" class="hover:text-indigo-600 transition duration-300">
                  {{ post.title }}
                </router-link>
              </h3>
              <p class="text-gray-600 text-sm mb-3 line-clamp-2">{{ post.summary }}</p>
              <div class="flex justify-end items-center text-xs text-gray-500">
                <span class="flex items-center mr-3">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 mr-1" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M10 12a2 2 0 100-4 2 2 0 000 4z" />
                    <path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd" />
                  </svg>
                  {{ post.views }}
                </span>
                <span class="flex items-center">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 mr-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd" />
                  </svg>
                  {{ post.likes }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- 加载骨架屏 -->
        <div v-else class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="i in 6" :key="i" class="bg-white border border-gray-100 rounded-xl overflow-hidden shadow-sm">
            <div class="w-full h-48 bg-gray-200 animate-pulse"></div>
            <div class="p-5">
              <div class="h-3 bg-gray-200 rounded animate-pulse mb-2 w-1/3"></div>
              <div class="h-5 bg-gray-200 rounded animate-pulse mb-2"></div>
              <div class="h-3 bg-gray-200 rounded animate-pulse mb-1"></div>
              <div class="h-3 bg-gray-200 rounded animate-pulse w-2/3 mb-3"></div>
              <div class="flex justify-end">
                <div class="h-3 bg-gray-200 rounded animate-pulse w-16"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 分类导航区 -->
    <section class="py-16 bg-gray-50">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-gray-900 mb-10 text-center">探索分类</h2>
        
        <div v-if="!isLoading" class="grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-6">
          <router-link 
            v-for="category in categories" 
            :key="category.id"
            :to="`/category/${category.slug}`" 
            class="flex flex-col items-center bg-white rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-300 group"
          >
            <div class="w-16 h-16 flex items-center justify-center rounded-full bg-indigo-100 text-indigo-600 mb-4 group-hover:bg-indigo-200 transition-colors duration-300">
              <i :class="`${getCategoryIcon(category.name)} text-xl`"></i>
            </div>
            <h3 class="font-semibold text-gray-900 mb-1">{{ category.name }}</h3>
            <span class="text-sm text-gray-500">{{ category.count }} 篇文章</span>
          </router-link>
        </div>

        <!-- 加载骨架屏 -->
        <div v-else class="grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-6">
          <div v-for="i in 6" :key="i" class="flex flex-col items-center bg-white rounded-xl p-6 shadow-sm">
            <div class="w-16 h-16 rounded-full bg-gray-200 animate-pulse mb-4"></div>
            <div class="h-4 bg-gray-200 rounded animate-pulse w-20 mb-1"></div>
            <div class="h-3 bg-gray-200 rounded animate-pulse w-12"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 通讯订阅区 -->
    <section class="py-16 bg-gradient-to-br from-indigo-900 to-purple-900 text-white">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl font-bold mb-4">订阅我的通讯</h2>
        <p class="text-indigo-100 mb-8 max-w-2xl mx-auto">获取最新的文章更新和独家内容，直接发送到您的邮箱</p>
        <form @submit.prevent="subscribeNewsletter" class="flex flex-col sm:flex-row gap-4 max-w-lg mx-auto mb-6">
          <input 
            type="email" 
            v-model="newsletterEmail" 
            placeholder="您的电子邮件地址"
            class="px-4 py-3 rounded-lg flex-grow text-gray-900 border-2 border-transparent focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 outline-none"
            required
          >
          <button 
            type="submit" 
            class="px-6 py-3 bg-white text-indigo-600 font-medium rounded-lg shadow transition-colors duration-300 hover:bg-indigo-50"
          >
            订阅
          </button>
        </form>
        <p class="text-xs text-indigo-200">
          我们尊重您的隐私，不会发送垃圾邮件。您可以随时取消订阅。
        </p>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

// 类型定义
interface Post {
  id: number;
  title: string;
  slug: string;
  summary: string;
  content?: string;
  cover_image?: string;
  author: string;
  category: string;
  views: number;
  likes: number;
  created_at: string;
}

interface Category {
  id: number;
  name: string;
  slug: string;
  count: number;
}

// 响应式状态
const isLoading = ref(true);
const featuredPost = ref<Post | null>(null);
const secondaryPosts = ref<Post[]>([]);
const latestPosts = ref<Post[]>([]);
const categories = ref<Category[]>([]);
const newsletterEmail = ref('');

// 获取数据
onMounted(async () => {
  try {
    isLoading.value = true;
    
    // 模拟API调用
    setTimeout(() => {
      // 设置模拟数据
      featuredPost.value = {
        id: 1,
        title: "构建现代响应式网站的10个最佳实践",
        slug: "modern-responsive-website-best-practices",
        summary: "了解如何利用最新的技术和方法创建流畅、快速且用户友好的响应式网站...",
        author: "张三",
        category: "Web开发",
        views: 1250,
        likes: 302,
        created_at: "2023-03-15T09:30:00Z",
        cover_image: "https://images.unsplash.com/photo-1555099962-4199c345e5dd?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
      };

      secondaryPosts.value = [
        {
          id: 2,
          title: "JavaScript Promise 完全指南",
          slug: "javascript-promise-complete-guide",
          summary: "深入了解JavaScript Promise的工作原理，以及如何有效地使用它们来处理异步操作...",
          author: "李四",
          category: "JavaScript",
          views: 850,
          likes: 175,
          created_at: "2023-03-10T14:20:00Z"
        },
        {
          id: 3,
          title: "Vue 3 组合式API与响应式系统解析",
          slug: "vue3-composition-api-reactivity",
          summary: "探索Vue 3的组合式API如何改变我们编写和组织Vue组件的方式，以及响应式系统的工作原理...",
          author: "王五",
          category: "Vue.js",
          views: 720,
          likes: 198,
          created_at: "2023-03-05T11:45:00Z"
        }
      ];

      latestPosts.value = [
        {
          id: 4,
          title: "使用Docker简化开发环境配置",
          slug: "simplify-dev-environment-with-docker",
          summary: "了解如何使用Docker容器化您的开发环境，提高团队协作效率并减少环境不一致问题...",
          author: "赵六",
          category: "DevOps",
          views: 560,
          likes: 120,
          created_at: "2023-03-01T16:30:00Z"
        },
        {
          id: 5,
          title: "CSS Grid布局完全指南",
          slug: "css-grid-layout-complete-guide",
          summary: "详细探讨CSS Grid布局系统，包括基础概念、实际应用案例和高级技巧...",
          author: "孙七",
          category: "CSS",
          views: 490,
          likes: 105,
          created_at: "2023-02-25T08:15:00Z"
        },
        {
          id: 6,
          title: "TypeScript高级类型和类型操作",
          slug: "typescript-advanced-types",
          summary: "深入TypeScript的类型系统，学习如何利用高级类型特性编写更安全、更可维护的代码...",
          author: "周八",
          category: "TypeScript",
          views: 410,
          likes: 88,
          created_at: "2023-02-20T13:50:00Z"
        },
        {
          id: 7,
          title: "React性能优化策略",
          slug: "react-performance-optimization",
          summary: "学习识别和解决React应用中的常见性能问题，掌握提升用户体验的优化技巧...",
          author: "吴九",
          category: "React",
          views: 380,
          likes: 95,
          created_at: "2023-02-15T10:20:00Z"
        },
        {
          id: 8,
          title: "现代化API设计原则",
          slug: "modern-api-design-principles",
          summary: "探讨设计直观、高效且易于使用的REST和GraphQL API的最佳实践和原则...",
          author: "郑十",
          category: "后端开发",
          views: 320,
          likes: 76,
          created_at: "2023-02-10T09:05:00Z"
        },
        {
          id: 9,
          title: "使用Jest进行前端测试",
          slug: "frontend-testing-with-jest",
          summary: "学习如何使用Jest和测试库为你的React和Vue应用编写有效的单元测试和集成测试...",
          author: "钱一",
          category: "测试",
          views: 290,
          likes: 65,
          created_at: "2023-02-05T14:40:00Z"
        }
      ];

      categories.value = [
        { id: 1, name: "Web开发", slug: "web-development", count: 42 },
        { id: 2, name: "JavaScript", slug: "javascript", count: 35 },
        { id: 3, name: "Vue.js", slug: "vue-js", count: 28 },
        { id: 4, name: "CSS", slug: "css", count: 22 },
        { id: 5, name: "React", slug: "react", count: 19 },
        { id: 6, name: "后端开发", slug: "backend", count: 17 }
      ];

      isLoading.value = false;
    }, 1000);
    
    // TODO: 实际API调用在这里
  } catch (error) {
    console.error('获取数据失败:', error);
    isLoading.value = false;
  }
});

// 工具函数
const formatDate = (dateString: string) => {
  const date = new Date(dateString);
  return new Intl.DateTimeFormat('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  }).format(date);
};

const getRandomImage = (seed: string) => {
  return `https://source.unsplash.com/random/800x600/?blog,${seed}`;
};

const getAvatarUrl = (username: string) => {
  return `https://api.dicebear.com/7.x/avataaars/svg?seed=${username}`;
};

const getCategoryIcon = (categoryName: string) => {
  const iconMap: {[key: string]: string} = {
    'Web开发': 'fas fa-globe',
    'JavaScript': 'fab fa-js',
    'Vue.js': 'fab fa-vuejs',
    'CSS': 'fab fa-css3-alt',
    'React': 'fab fa-react',
    '后端开发': 'fas fa-server',
    'DevOps': 'fab fa-docker',
    'TypeScript': 'fab fa-js',
    '测试': 'fas fa-vial'
  };
  
  return iconMap[categoryName] || 'fas fa-folder';
};

// 订阅处理
const subscribeNewsletter = async () => {
  if (!newsletterEmail.value) return;
  
  try {
    // TODO: 实际API调用
    alert(`感谢您的订阅！确认邮件已发送至 ${newsletterEmail.value}`);
    newsletterEmail.value = '';
  } catch (error) {
    console.error('订阅失败:', error);
    alert('订阅失败，请稍后重试');
  }
};
</script>