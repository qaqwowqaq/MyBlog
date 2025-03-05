<template>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <div class="min-h-screen bg-white">
      <!-- 顶部英雄区域 - 使用Tailwind CSS 4.x的渐变和动画特性 -->
      <section class="relative py-28 overflow-hidden">
        <!-- 背景渐变 -->
        <div class="absolute inset-0 bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-500"></div>
        
        <!-- 动态几何图形装饰 -->
        <div class="absolute inset-0 opacity-10">
          <div class="absolute top-0 left-0 w-72 h-72 bg-white rounded-full mix-blend-overlay blur-3xl animate-blob"></div>
          <div class="absolute top-0 right-0 w-72 h-72 bg-pink-300 rounded-full mix-blend-overlay blur-3xl animate-blob animation-delay-2000"></div>
          <div class="absolute bottom-0 left-1/4 w-72 h-72 bg-yellow-300 rounded-full mix-blend-overlay blur-3xl animate-blob animation-delay-4000"></div>
        </div>
        
        <!-- 内容 -->
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
          <div class="text-center">
            <h1 class="text-4xl md:text-6xl font-extrabold mb-6 tracking-tight text-white drop-shadow-lg">
              <span class="bg-clip-text text-transparent bg-gradient-to-r from-white to-indigo-200">
                探索想法，分享知识
              </span>
            </h1>
            <p class="text-xl max-w-3xl mx-auto mb-10 text-indigo-100 opacity-90">
              欢迎来到我的博客空间，这里记录了我的思考、学习和成长历程
            </p>
            <div class="flex flex-wrap justify-center gap-4">
              <router-link to="/posts" class="bg-white text-indigo-600 hover:text-indigo-800 hover:bg-indigo-50 font-medium px-8 py-3.5 rounded-lg shadow-lg transition-all duration-300 transform hover:-translate-y-1">
                浏览文章
              </router-link>
              <router-link to="/about" class="bg-white bg-opacity-10 backdrop-blur-sm hover:bg-opacity-20 text-white border border-white/30 px-8 py-3.5 rounded-lg transition-all duration-300 transform hover:-translate-y-1">
                了解更多
              </router-link>
            </div>
          </div>
        </div>
        
        <!-- 波浪底部装饰 -->
        <div class="absolute bottom-0 left-0 right-0">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320" class="w-full h-auto fill-white">
            <path d="M0,224L48,213.3C96,203,192,181,288,181.3C384,181,480,203,576,213.3C672,224,768,224,864,197.3C960,171,1056,117,1152,96C1248,75,1344,85,1392,90.7L1440,96L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
          </svg>
        </div>
      </section>
  
      <!-- 特色内容区 -->
      <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-16">
            <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">精选文章</h2>
            <div class="w-24 h-1.5 bg-gradient-to-r from-indigo-500 to-purple-600 mx-auto rounded-full"></div>
          </div>
          
          <!-- 文章加载状态 -->
          <div v-if="isLoading" class="flex flex-col items-center justify-center py-20">
            <div class="w-16 h-16 border-4 border-indigo-200 border-t-indigo-600 rounded-full animate-spin"></div>
            <p class="mt-4 text-gray-500">正在加载精彩内容...</p>
          </div>
          
          <!-- 文章展示区 -->
          <div v-else-if="posts.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- 精选文章卡片 -->
            <article v-for="post in posts" :key="post.id" 
              class="bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition-all duration-300 flex flex-col group">
              <!-- 文章图片 -->
              <div class="relative h-56 overflow-hidden">
                <img 
                  :src="post.cover_image || `https://source.unsplash.com/random/800x450?${post.id}`" 
                  :alt="post.title"
                  class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                />
                <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent"></div>
                
                <!-- 分类标签 -->
                <div class="absolute bottom-4 left-4 flex gap-2">
                  <span class="px-3 py-1 bg-indigo-600 text-white text-xs font-medium rounded-full">
                    {{ post.category?.name || '未分类' }}
                  </span>
                </div>
              </div>
              
              <!-- 文章内容 -->
              <div class="p-6 flex-1 flex flex-col">
                <h3 class="text-xl font-bold mb-3 text-gray-900 group-hover:text-indigo-600 transition-colors duration-300">
                  <router-link :to="`/post/${post.slug}`" class="hover:underline decoration-2 decoration-indigo-400 underline-offset-2">
                    {{ post.title }}
                  </router-link>
                </h3>
                <p class="text-gray-600 mb-4 text-sm line-clamp-2 flex-1">
                  {{ post.summary || '暂无摘要' }}
                </p>
                
                <!-- 文章元信息 -->
                <div class="flex items-center justify-between pt-4 border-t border-gray-100">
                  <!-- 作者信息 -->
                  <div class="flex items-center gap-2">
                    <img 
                      :src="`https://api.dicebear.com/7.x/micah/svg?seed=${post.author}`" 
                      class="w-8 h-8 rounded-full bg-gray-200" 
                      :alt="post.author"
                    />
                    <span class="text-sm text-gray-700">{{ post.author }}</span>
                  </div>
                  
                  <!-- 日期 -->
                  <div class="text-xs text-gray-500">
                    {{ formatDate(post.created_at) }}
                  </div>
                </div>
              </div>
            </article>
          </div>
          
          <!-- 无文章状态 -->
          <div v-else class="text-center py-20 bg-gray-50 rounded-2xl">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 mx-auto text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z" />
            </svg>
            <h3 class="mt-4 text-xl font-medium text-gray-600">暂无文章</h3>
            <p class="mt-2 text-gray-500">敬请期待精彩内容</p>
          </div>
          
          <!-- 查看更多按钮 -->
          <div v-if="posts.length" class="mt-12 text-center">
            <router-link to="/posts" 
              class="inline-flex items-center px-6 py-3 border border-indigo-500 text-indigo-600 rounded-lg hover:bg-indigo-500 hover:text-white transition-colors duration-300">
              查看更多文章
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
              </svg>
            </router-link>
          </div>
        </div>
      </section>
  
      <!-- 技术栈展示区 -->
      <section class="py-20 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-16">
            <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">技术栈</h2>
            <p class="text-lg text-gray-600 max-w-3xl mx-auto">
              本博客采用现代化的技术栈构建，提供流畅的用户体验
            </p>
          </div>
  
          <div class="grid grid-cols-2 md:grid-cols-4 gap-6 md:gap-8">
            <div class="bg-white p-6 rounded-xl shadow-md flex flex-col items-center transition-transform hover:-translate-y-1 duration-300">
              <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Vue.js_Logo_2.svg" alt="Vue.js" class="h-16 w-auto mb-4" />
              <h3 class="font-bold text-gray-900">Vue 3</h3>
              <p class="text-gray-600 text-sm text-center mt-2">渐进式 JavaScript 框架</p>
            </div>
            
            <div class="bg-white p-6 rounded-xl shadow-md flex flex-col items-center transition-transform hover:-translate-y-1 duration-300">
              <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Typescript_logo_2020.svg/512px-Typescript_logo_2020.svg.png" alt="TypeScript" class="h-16 w-auto mb-4" />
              <h3 class="font-bold text-gray-900">TypeScript</h3>
              <p class="text-gray-600 text-sm text-center mt-2">类型安全的 JavaScript</p>
            </div>
            
            <div class="bg-white p-6 rounded-xl shadow-md flex flex-col items-center transition-transform hover:-translate-y-1 duration-300">
              <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/640px-Python-logo-notext.svg.png" alt="Python" class="h-16 w-auto mb-4" />
              <h3 class="font-bold text-gray-900">Django</h3>
              <p class="text-gray-600 text-sm text-center mt-2">强大的 Python Web 框架</p>
            </div>
            
            <div class="bg-white p-6 rounded-xl shadow-md flex flex-col items-center transition-transform hover:-translate-y-1 duration-300">
              <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Tailwind_CSS_Logo.svg/2048px-Tailwind_CSS_Logo.svg.png" alt="Tailwind CSS" class="h-16 w-auto mb-4" />
              <h3 class="font-bold text-gray-900">Tailwind CSS</h3>
              <p class="text-gray-600 text-sm text-center mt-2">实用优先的 CSS 框架</p>
            </div>
          </div>
        </div>
      </section>
      
      <!-- 简短介绍区 -->
      <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="bg-gradient-to-br from-indigo-600 to-purple-600 rounded-3xl overflow-hidden shadow-xl">
            <div class="md:flex">
              <div class="md:w-1/2 p-12 md:p-16 text-white">
                <h2 class="text-3xl md:text-4xl font-bold mb-6">关于本站</h2>
                <p class="text-indigo-100 mb-8 text-lg">
                  这是我的个人博客，用于分享我在技术领域的探索与思考。
                  无论你是技术爱好者、学生还是专业人士，希望你能在这里找到有价值的内容。
                </p>
                <router-link to="/about" 
                  class="inline-block bg-white text-indigo-600 font-medium px-6 py-3 rounded-lg hover:bg-opacity-90 transition-colors duration-300">
                  了解更多
                </router-link>
              </div>
              <div class="md:w-1/2 aspect-video md:aspect-auto">
                <img 
                  src="https://images.unsplash.com/photo-1498050108023-c5249f4df085" 
                  alt="About" 
                  class="w-full h-full object-cover"
                />
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  
  interface Post {
    id: number;
    title: string;
    slug: string;
    summary?: string;
    cover_image?: string;
    author: string;
    category: { name: string } | null;
    created_at: string;
  }
  
  // 文章数据
  const posts = ref<Post[]>([]);
  const isLoading = ref(true);
  
  // 格式化日期
  const formatDate = (dateString: string) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('zh-CN', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    }).format(date);
  };
  
  // 加载文章数据
  const fetchPosts = async () => {
    try {
      isLoading.value = true;
      // 这里替换为你的实际API端点
      const response = await axios.get('http://123.56.118.72:8000/api/articles/');
      posts.value = response.data.results.slice(0, 6); // 只显示前6篇文章
    } catch (error) {
      console.error('获取文章失败:', error);
      posts.value = [];
    } finally {
      isLoading.value = false;
    }
  };
  
  onMounted(() => {
    fetchPosts();
  });
  </script>
  
  <style>
  @keyframes blob {
    0% { transform: translate(0px, 0px) scale(1); }
    33% { transform: translate(30px, -50px) scale(1.1); }
    66% { transform: translate(-20px, 20px) scale(0.9); }
    100% { transform: translate(0px, 0px) scale(1); }
  }
  
  .animate-blob {
    animation: blob 7s infinite;
  }
  
  .animation-delay-2000 {
    animation-delay: 2s;
  }
  
  .animation-delay-4000 {
    animation-delay: 4s;
  }
  
  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;  
    overflow: hidden;
  }
  </style>