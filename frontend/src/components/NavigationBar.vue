<template>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
  <div class="sticky top-0 z-50 w-full bg-white transition-all duration-300" 
       :class="{ 'shadow-md': scrolled }">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- 左侧 Logo 区域 -->
        <div class="flex-shrink-0 flex items-center">
          <router-link to="/" class="flex items-center space-x-2 group">
            <img src="@/assets/logo.png" alt="Logo" class="h-8 w-auto transition-transform duration-300 group-hover:scale-110 rounded-2xl" />
            <span class="text-xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">MyBlog</span>
          </router-link>
        </div>

        <!-- 中间导航链接 -->
        <div class="hidden md:flex md:items-center md:space-x-8">
          <router-link 
            v-for="(item, index) in navItems" 
            :key="index" 
            :to="item.path" 
            class="font-medium text-gray-700 hover:text-blue-600 transition-colors duration-200 relative py-2 px-1"
            :class="{ 'text-blue-600 after:w-full': isActive(item.path) }"
          >
            <span>{{ item.name }}</span>
            <span class="absolute bottom-0 left-0 h-0.5 bg-blue-600 transform origin-left transition-all duration-200"
                  :class="isActive(item.path) ? 'w-full' : 'w-0'"></span>
          </router-link>
        </div>

        <!-- 右侧功能区 -->
        <div class="flex items-center space-x-4">
          <!-- 搜索框 -->
          <div class="relative" :class="{ 'w-64 transition-all duration-300 ease-in-out': isSearchExpanded, 'w-10 transition-all duration-300 ease-in-out': !isSearchExpanded }">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none" v-if="isSearchExpanded">
              <svg class="h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd" />
              </svg>
            </div>
            <input 
              v-model="searchQuery" 
              type="text" 
              class="w-full bg-gray-50 border-0 rounded-full py-2 pl-10 pr-4 focus:ring-2 focus:ring-blue-500 focus:outline-none transition-opacity duration-300"
              :class="{ 'opacity-100': isSearchExpanded, 'opacity-0': !isSearchExpanded }"
              placeholder="搜索文章..." 
              @keyup.enter="handleSearch"
              v-show="isSearchExpanded"
            >
            <button 
              class="bg-gray-100 hover:bg-gray-200 p-2 rounded-full transition-all duration-200 flex items-center justify-center"
              :class="{ 'absolute right-0 top-0': isSearchExpanded }"
              @click="toggleSearch"
            >
              <svg class="h-5 w-5 text-gray-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" v-if="!isSearchExpanded">
                <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd" />
              </svg>
              <svg class="h-5 w-5 text-gray-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" v-else>
                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </button>
          </div>

          <!-- 登录/注册按钮 -->
          <div v-if="!isLoggedIn" class="hidden sm:flex sm:items-center sm:space-x-3">
            <router-link 
              to="/login" 
              class="text-blue-600 hover:text-blue-800 border border-blue-600 hover:border-blue-800 px-4 py-2 rounded-md text-sm font-medium transition-all duration-200"
            >
              登录
            </router-link>
            <router-link 
              to="/register" 
              class="bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white px-4 py-2 rounded-md text-sm font-medium shadow-sm hover:shadow-md transition-all duration-200"
            >
              注册
            </router-link>
          </div>

          <!-- 用户菜单 -->
          <div class="relative" v-else>
            <div 
              @click="toggleUserMenu" 
              class="flex items-center space-x-3 cursor-pointer group"
            >
              <img 
                :src="userAvatar" 
                alt="User Avatar" 
                class="h-9 w-9 rounded-full object-cover border-2 border-gray-200 group-hover:border-blue-500 transition-all duration-300 shadow-sm"
              >
              <span class="hidden md:block font-medium text-gray-700 group-hover:text-blue-600 transition-colors duration-200">{{ username }}</span>
              <svg 
                class="h-5 w-5 text-gray-400 transition-transform duration-200" 
                :class="{ 'rotate-180': showUserMenu }"
                xmlns="http://www.w3.org/2000/svg" 
                viewBox="0 0 20 20" 
                fill="currentColor"
              >
                <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </div>

            <!-- 下拉菜单 -->
            <div 
              v-if="showUserMenu" 
              class="absolute right-0 mt-3 w-56 rounded-xl bg-white py-2 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none transform origin-top-right transition-all duration-200 z-50"
            >
              <router-link 
                to="/dashboard" 
                class="flex items-center px-4 py-3 text-gray-700 hover:bg-gray-50 hover:text-blue-600 space-x-3"
              >
                <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z" />
                  <path d="M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z" />
                </svg>
                <span>仪表板</span>
              </router-link>
              
              <router-link 
                to="/profile" 
                class="flex items-center px-4 py-3 text-gray-700 hover:bg-gray-50 hover:text-blue-600 space-x-3"
              >
                <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
                </svg>
                <span>个人资料</span>
              </router-link>
              
              <router-link 
                to="/new-post" 
                class="flex items-center px-4 py-3 text-gray-700 hover:bg-gray-50 hover:text-blue-600 space-x-3"
              >
                <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                </svg>
                <span>写文章</span>
              </router-link>
              
              <div class="h-px bg-gray-200 my-2"></div>
              
              <button 
                @click="handleLogout" 
                class="flex w-full items-center px-4 py-3 text-red-600 hover:bg-red-50 space-x-3"
              >
                <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M3 3a1 1 0 00-1 1v12a1 1 0 001 1h12a1 1 0 001-1V7.414l-4-4H3zm4 10.5a.5.5 0 01-.5.5h-1a.5.5 0 01-.5-.5v-1a.5.5 0 01.5-.5h1a.5.5 0 01.5.5v1zm0-3a.5.5 0 01-.5.5h-1a.5.5 0 01-.5-.5v-1a.5.5 0 01.5-.5h1a.5.5 0 01.5.5v1zm4 3a.5.5 0 01-.5.5h-1a.5.5 0 01-.5-.5v-1a.5.5 0 01.5-.5h1a.5.5 0 01.5.5v1zm0-6a.5.5 0 01-.5.5h-1a.5.5 0 01-.5-.5v-1a.5.5 0 01.5-.5h1a.5.5 0 01.5.5v1zm4 3a.5.5 0 01-.5.5h-1a.5.5 0 01-.5-.5v-1a.5.5 0 01.5-.5h1a.5.5 0 01.5.5v1z" clip-rule="evenodd" />
                </svg>
                <span>退出登录</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();

// 导航项目
const navItems = [
  { name: '首页', path: '/' },
  { name: '文章', path: '/posts' },
  { name: '分类', path: '/categories' },
  { name: '标签', path: '/tags' },
  { name: '关于', path: '/about' }
];

// 搜索功能
const searchQuery = ref('');
const isSearchExpanded = ref(false);

const toggleSearch = () => {
  if (isSearchExpanded.value && searchQuery.value) {
    handleSearch();
  } else {
    isSearchExpanded.value = !isSearchExpanded.value;
  }
};

const handleSearch = () => {
  if (searchQuery.value.trim()) {
    router.push({
      path: '/search',
      query: { q: searchQuery.value }
    });
    isSearchExpanded.value = false;
  }
};

// 用户菜单
const showUserMenu = ref(false);
const scrolled = ref(false);

// 模拟用户登录状态 (实际应用中应该从 store 或 API 获取)
const isLoggedIn = ref(false);
const username = ref('User');
const userAvatar = ref('https://api.dicebear.com/7.x/avataaars/svg?seed=Abby');

// 检查用户登录状态
onMounted(() => {
  const token = localStorage.getItem('token');
  if (token) {
    isLoggedIn.value = true;
    // 这里应该从 API 获取用户信息
    // 例如: getUserInfo(token).then(user => username.value = user.username)
  }

  // 添加滚动监听器
  window.addEventListener('scroll', handleScroll);
  
  // 添加点击外部关闭菜单
  document.addEventListener('click', handleOutsideClick);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
  document.removeEventListener('click', handleOutsideClick);
});

const handleScroll = () => {
  scrolled.value = window.scrollY > 10;
};

const toggleUserMenu = (event: Event) => {
  event.stopPropagation();
  showUserMenu.value = !showUserMenu.value;
};

const handleOutsideClick = (event: Event) => {
  const target = event.target as HTMLElement;
  if (!target.closest('.user-menu')) {
    showUserMenu.value = false;
  }
};

const handleLogout = () => {
  localStorage.removeItem('token');
  isLoggedIn.value = false;
  showUserMenu.value = false;
  router.push('/');
};

// 检查当前路由是否活跃
const isActive = (path: string) => {
  if (path === '/') {
    return route.path === '/';
  }
  return route.path.startsWith(path);
};
</script>