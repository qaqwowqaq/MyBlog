<template>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <div class="min-h-screen bg-gradient-to-br from-gray-900 to-gray-800 flex items-center justify-center p-4">
      <div 
        class="w-full max-w-5xl bg-white rounded-2xl shadow-2xl overflow-hidden flex flex-col lg:flex-row transform transition-all duration-500 hover:shadow-[0_20px_50px_rgba(8,_112,_184,_0.3)]"
        :class="{ 'opacity-90': isLoading }"
      >
        <!-- 左侧介绍区域 -->
        <div class="hidden lg:block lg:w-1/2 bg-gradient-to-br from-blue-600 to-indigo-800 text-white p-12 relative overflow-hidden">
          <!-- 动态背景元素 -->
          <div class="absolute top-0 left-0 w-full h-full">
            <div class="absolute w-64 h-64 rounded-full bg-blue-400 opacity-10 -top-10 -left-10 animate-pulse"></div>
            <div class="absolute w-96 h-96 rounded-full bg-indigo-500 opacity-10 -bottom-20 -right-20 animate-pulse" style="animation-delay: 1s;"></div>
            <div class="absolute w-48 h-48 rounded-full bg-purple-500 opacity-10 bottom-36 left-10 animate-pulse" style="animation-delay: 2s;"></div>
          </div>
          
          <div class="relative z-10">
            <h1 class="text-4xl font-bold mb-6 leading-tight">欢迎回到您的空间</h1>
            <p class="text-xl text-blue-100 mb-8">登录您的账号，开始分享您的创意与思考。</p>
            
            <div class="space-y-4">
              <div 
                class="bg-white bg-opacity-10 p-6 rounded-xl backdrop-filter backdrop-blur-lg transform transition-all duration-300 hover:translate-x-2"
                v-motion
                :initial="{ opacity: 0, y: 20 }"
                :enter="{ opacity: 1, y: 0, transition: { delay: 200 } }"
              >
                <div class="flex items-center mb-4">
                  <span class="p-2 rounded-full bg-blue-500 bg-opacity-30 mr-3">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                    </svg>
                  </span>
                  <h3 class="font-semibold text-lg">创作与分享</h3>
                </div>
                <p class="text-blue-100">发布您的灵感，连接志同道合的读者</p>
              </div>
              
              <div 
                class="bg-white bg-opacity-10 p-6 rounded-xl backdrop-filter backdrop-blur-lg transform transition-all duration-300 hover:translate-x-2"
                v-motion
                :initial="{ opacity: 0, y: 20 }"
                :enter="{ opacity: 1, y: 0, transition: { delay: 400 } }"
              >
                <div class="flex items-center mb-4">
                  <span class="p-2 rounded-full bg-indigo-500 bg-opacity-30 mr-3">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
                    </svg>
                  </span>
                  <h3 class="font-semibold text-lg">个性化空间</h3>
                </div>
                <p class="text-blue-100">打造专属于您的创作天地</p>
              </div>
            </div>
          </div>
          
          <div class="absolute bottom-8 left-12 right-12 text-sm text-blue-200 z-10">
            <p>© 2025 所有权利保留</p>
          </div>
        </div>
        
        <!-- 右侧登录区域 -->
        <div 
          class="w-full lg:w-1/2 p-8 md:p-12"
          v-motion
          :initial="{ opacity: 0 }"
          :enter="{ opacity: 1, transition: { duration: 500 } }"
        >
          <div class="max-w-md mx-auto">
            <div class="text-center mb-10">
              <h2 class="text-3xl font-bold text-gray-900">登录您的账户</h2>
              <p class="mt-3 text-gray-600">欢迎回来，请登录您的账户</p>
            </div>
            
            <!-- 表单区域 -->
            <form class="space-y-6" @submit.prevent="handleLogin">
              <!-- 错误提示 -->
              <div 
                v-if="error" 
                class="bg-red-50 border-l-4 border-red-500 text-red-700 p-4 rounded-lg" 
                role="alert"
                v-motion
                :initial="{ opacity: 0, x: -20 }"
                :enter="{ opacity: 1, x: 0 }"
              >
                <div class="flex items-center">
                  <svg class="h-5 w-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zm-1 9a1 1 0 01-1-1v-4a1 1 0 112 0v4a1 1 0 01-1 1z" clip-rule="evenodd"></path>
                  </svg>
                  <p>{{ error }}</p>
                </div>
              </div>
              
              <div class="space-y-5">
                <div 
                  v-motion
                  :initial="{ opacity: 0, y: 10 }"
                  :enter="{ opacity: 1, y: 0, transition: { delay: 100 } }"
                >
                  <label for="username" class="block text-sm font-medium text-gray-700 mb-1">用户名</label>
                  <div class="relative">
                    <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                      </svg>
                    </div>
                    <input 
                      id="username" 
                      v-model="formData.username" 
                      type="text" 
                      required 
                      class="appearance-none block w-full px-3 py-3 pl-10 border border-gray-300 rounded-lg placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-300"
                      placeholder="您的用户名"
                      :class="{ 'animate-pulse border-red-500': formErrors.username }"
                    />
                  </div>
                  <p v-if="formErrors.username" class="mt-1 text-sm text-red-600">{{ formErrors.username }}</p>
                </div>
                
                <div 
                  v-motion
                  :initial="{ opacity: 0, y: 10 }"
                  :enter="{ opacity: 1, y: 0, transition: { delay: 200 } }"
                >
                  <label for="password" class="block text-sm font-medium text-gray-700 mb-1">密码</label>
                  <div class="relative">
                    <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                      </svg>
                    </div>
                    <input 
                      id="password" 
                      v-model="formData.password" 
                      :type="showPassword ? 'text' : 'password'" 
                      required 
                      class="appearance-none block w-full px-3 py-3 pl-10 border border-gray-300 rounded-lg placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-300"
                      placeholder="您的密码"
                      :class="{ 'animate-pulse border-red-500': formErrors.password }"
                    />
                    <button 
                      type="button" 
                      @click="showPassword = !showPassword" 
                      class="absolute inset-y-0 right-0 pr-3 flex items-center text-gray-400 hover:text-gray-600 transition-colors"
                    >
                      <svg v-if="showPassword" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21" />
                      </svg>
                      <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                      </svg>
                    </button>
                  </div>
                  <p v-if="formErrors.password" class="mt-1 text-sm text-red-600">{{ formErrors.password }}</p>
                </div>
              </div>
              
              <div 
                class="flex items-center justify-between"
                v-motion
                :initial="{ opacity: 0 }"
                :enter="{ opacity: 1, transition: { delay: 300 } }"
              >
                <div class="flex items-center">
                  <input 
                    id="remember-me" 
                    v-model="rememberMe" 
                    type="checkbox" 
                    class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded transition"
                  />
                  <label for="remember-me" class="ml-2 block text-sm text-gray-700">记住我</label>
                </div>
                <a href="#" class="text-sm text-blue-600 hover:text-blue-800 transition-colors">忘记密码?</a>
              </div>
              
              <div
                v-motion
                :initial="{ opacity: 0, y: 10 }"
                :enter="{ opacity: 1, y: 0, transition: { delay: 400 } }"
              >
                <button 
                  type="submit" 
                  class="w-full flex justify-center py-3 px-4 border border-transparent rounded-lg text-white bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-all duration-300 transform hover:scale-[1.02]"
                  :disabled="isLoading"
                >
                  <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                    <svg 
                      v-if="!isLoading" 
                      class="h-5 w-5 text-blue-300 group-hover:text-blue-200" 
                      xmlns="http://www.w3.org/2000/svg" 
                      viewBox="0 0 20 20" 
                      fill="currentColor" 
                      aria-hidden="true"
                    >
                      <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" />
                    </svg>
                    <svg 
                      v-else 
                      class="animate-spin h-5 w-5 text-white" 
                      xmlns="http://www.w3.org/2000/svg" 
                      fill="none" 
                      viewBox="0 0 24 24"
                    >
                      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                  </span>
                  <span class="flex items-center">
                    <span class="mr-2">{{ isLoading ? '登录中...' : '登录' }}</span>
                    <svg v-if="!isLoading" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                    </svg>
                  </span>
                </button>
              </div>
              
              <div 
                class="text-center mt-6"
                v-motion
                :initial="{ opacity: 0 }"
                :enter="{ opacity: 1, transition: { delay: 500 } }"
              >
                <span class="text-gray-600">还没有账户?</span>
                <router-link to="/register" class="ml-1 text-blue-600 hover:text-blue-800 font-medium transition-colors">
                  立即注册
                </router-link>
              </div>
              
              <div 
                class="relative flex items-center justify-center mt-8"
                v-motion
                :initial="{ opacity: 0 }"
                :enter="{ opacity: 1, transition: { delay: 600 } }"
              >
                <div class="absolute border-t border-gray-200 w-full"></div>
                <div class="relative bg-white px-4 text-sm text-gray-500">其他登录方式</div>
              </div>
              
              <div 
                class="grid grid-cols-3 gap-3"
                v-motion
                :initial="{ opacity: 0, y: 10 }"
                :enter="{ opacity: 1, y: 0, transition: { delay: 700 } }"
              >
                <button 
                  type="button" 
                  class="flex justify-center items-center py-2 px-4 border border-gray-300 rounded-md shadow-sm bg-white hover:bg-gray-50 transition-all duration-300 transform hover:scale-105"
                >
                  <svg class="h-5 w-5 text-blue-600" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M23.998 12c0-6.628-5.372-12-11.999-12C5.372 0 0 5.372 0 12c0 5.988 4.388 10.952 10.124 11.852v-8.384H7.078v-3.469h3.046V9.356c0-3.008 1.792-4.669 4.532-4.669 1.313 0 2.686.234 2.686.234v2.953H15.83c-1.49 0-1.955.925-1.955 1.874V12h3.328l-.532 3.469h-2.796v8.384c5.736-.9 10.124-5.864 10.124-11.853z" />
                  </svg>
                </button>
                <button 
                  type="button" 
                  class="flex justify-center items-center py-2 px-4 border border-gray-300 rounded-md shadow-sm bg-white hover:bg-gray-50 transition-all duration-300 transform hover:scale-105"
                >
                  <svg class="h-5 w-5 text-blue-400" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M23.954 4.569a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723 9.99 9.99 0 01-3.127 1.195 4.92 4.92 0 00-8.384 4.482C7.691 8.094 4.066 6.13 1.64 3.161a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.061a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.937 4.937 0 004.604 3.417 9.868 9.868 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.054 0 13.999-7.496 13.999-13.986 0-.209 0-.42-.015-.63a9.936 9.936 0 002.46-2.548l-.047-.02z" />
                  </svg>
                </button>
                <button 
                  type="button" 
                  class="flex justify-center items-center py-2 px-4 border border-gray-300 rounded-md shadow-sm bg-white hover:bg-gray-50 transition-all duration-300 transform hover:scale-105"
                >
                  <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12.545 10.239v3.821h5.445c-.712 2.315-2.647 3.972-5.445 3.972a6.033 6.033 0 110-12.064 5.963 5.963 0 014.202 1.646l2.905-2.905A9.996 9.996 0 0012.545 2.001c-5.518 0-9.996 4.478-9.996 9.996s4.478 9.996 9.996 9.996c4.998 0 9.514-3.678 9.514-8.996 0-.664-.094-1.379-.201-1.989l-9.313.231z" />
                  </svg>
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, reactive } from 'vue';
  import { useRouter } from 'vue-router';
  import { useAuthStore } from '../store/AuthStore';
  //import { vMotion } from '@vueuse/motion';
  
  const router = useRouter();
  const authStore = useAuthStore();
  const isLoading = ref(false);
  const error = ref('');
  const showPassword = ref(false);
  const rememberMe = ref(false);
  
  const formData = reactive({
    username: '',
    password: ''
  });
  
  const formErrors = reactive({
    username: '',
    password: ''
  });
  
  const validateForm = () => {
    let isValid = true;
    formErrors.username = '';
    formErrors.password = '';
  
    if (!formData.username.trim()) {
      formErrors.username = '请输入用户名';
      isValid = false;
    }
  
    if (!formData.password) {
      formErrors.password = '请输入密码';
      isValid = false;
    } else if (formData.password.length < 6) {
      formErrors.password = '密码长度不能少于6个字符';
      isValid = false;
    }
  
    return isValid;
  };
  
  const handleLogin = async () => {
    if (!validateForm()) return;
    
    try {
      isLoading.value = true;
      error.value = '';
      
      // 使用 AuthStore 进行登录
      await authStore.login(formData.username, formData.password, rememberMe.value);
      
      // 登录成功动画效果
      setTimeout(() => {
        // 跳转到首页或之前的页面
        router.push('/');
      }, 500);
      
    } catch (err: any) {
      console.error('登录错误:', err);
      
      if (err.response && err.response.data) {
        // 处理不同类型的错误
        if (typeof err.response.data === 'object') {
          if (err.response.data.non_field_errors) {
            error.value = err.response.data.non_field_errors[0];
          } else {
            const errorMessages = Object.entries(err.response.data)
              .map(([key, value]) => `${key}: ${value}`)
              .join('; ');
            error.value = errorMessages;
          }
        } else {
          error.value = err.response.data;
        }
      } else {
        error.value = '登录失败，请检查您的网络连接';
      }
    } finally {
      isLoading.value = false;
    }
  };
  </script>
  
  <style scoped>
  @keyframes pulse {
    0%, 100% {
      opacity: 0.5;
    }
    50% {
      opacity: 0.2;
    }
  }
  
  .animate-pulse {
    animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  }
  
  /* 添加阴影过渡效果 */
  .shadow-2xl {
    transition: all 0.5s ease;
  }
  </style>