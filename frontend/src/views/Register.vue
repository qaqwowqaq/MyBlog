<template>
    <div class="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      <div class="sm:mx-auto sm:w-full sm:max-w-md">
        <div class="text-center">
          <router-link to="/" class="flex justify-center items-center mb-5">
            <img src="@/assets/logo.png" alt="Logo" class="h-12 w-auto" />
          </router-link>
          <h2 class="text-center text-3xl font-extrabold text-gray-900">
            创建您的账户
          </h2>
          <p class="mt-2 text-center text-sm text-gray-600">
            或者
            <router-link to="/login" class="font-medium text-blue-600 hover:text-blue-500">
              登录到您的账户
            </router-link>
          </p>
        </div>
  
        <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
          <div class="bg-white py-8 px-4 shadow-xl rounded-lg sm:px-10 border border-gray-100">
            <form class="space-y-6" @submit.prevent="handleRegister">
              <!-- 用户名 -->
              <div>
                <label for="username" class="block text-sm font-medium text-gray-700">
                  用户名
                </label>
                <div class="mt-1">
                  <input
                    id="username"
                    v-model="registerForm.username"
                    name="username"
                    type="text"
                    autocomplete="username"
                    required
                    class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                    :class="{ 'border-red-500': errors.username }"
                  />
                  <p v-if="errors.username" class="mt-1 text-sm text-red-600">{{ errors.username }}</p>
                </div>
              </div>
  
              <!-- 邮箱 -->
              <div>
                <label for="email" class="block text-sm font-medium text-gray-700">
                  邮箱地址
                </label>
                <div class="mt-1">
                  <input
                    id="email"
                    v-model="registerForm.email"
                    name="email"
                    type="email"
                    autocomplete="email"
                    required
                    class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                    :class="{ 'border-red-500': errors.email }"
                  />
                  <p v-if="errors.email" class="mt-1 text-sm text-red-600">{{ errors.email }}</p>
                </div>
              </div>
  
              <!-- 名字 -->
              <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-2">
                <div>
                  <label for="first_name" class="block text-sm font-medium text-gray-700">名字</label>
                  <div class="mt-1">
                    <input
                      id="first_name"
                      v-model="registerForm.first_name"
                      type="text"
                      name="first_name"
                      class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                      :class="{ 'border-red-500': errors.first_name }"
                    />
                    <p v-if="errors.first_name" class="mt-1 text-sm text-red-600">{{ errors.first_name }}</p>
                  </div>
                </div>
  
                <div>
                  <label for="last_name" class="block text-sm font-medium text-gray-700">姓氏</label>
                  <div class="mt-1">
                    <input
                      id="last_name"
                      v-model="registerForm.last_name"
                      type="text"
                      name="last_name"
                      class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                      :class="{ 'border-red-500': errors.last_name }"
                    />
                    <p v-if="errors.last_name" class="mt-1 text-sm text-red-600">{{ errors.last_name }}</p>
                  </div>
                </div>
              </div>
  
              <!-- 密码 -->
              <div>
                <label for="password" class="block text-sm font-medium text-gray-700">
                  密码
                </label>
                <div class="mt-1 relative">
                  <input
                    id="password"
                    v-model="registerForm.password"
                    :type="showPassword ? 'text' : 'password'"
                    name="password"
                    autocomplete="new-password"
                    required
                    class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                    :class="{ 'border-red-500': errors.password }"
                  />
                  <button 
                    type="button"
                    class="absolute inset-y-0 right-0 pr-3 flex items-center"
                    @click="showPassword = !showPassword"
                  >
                    <svg v-if="showPassword" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21" />
                    </svg>
                    <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                    </svg>
                  </button>
                  <p v-if="errors.password" class="mt-1 text-sm text-red-600">{{ errors.password }}</p>
                </div>
              </div>
  
              <!-- 确认密码 -->
              <div>
                <label for="password2" class="block text-sm font-medium text-gray-700">
                  确认密码
                </label>
                <div class="mt-1 relative">
                  <input
                    id="password2"
                    v-model="registerForm.password2"
                    :type="showPassword ? 'text' : 'password'"
                    name="password2"
                    autocomplete="new-password"
                    required
                    class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                    :class="{ 'border-red-500': errors.password2 }"
                  />
                  <p v-if="errors.password2" class="mt-1 text-sm text-red-600">{{ errors.password2 }}</p>
                </div>
              </div>
  
              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <input
                    id="agree"
                    v-model="agreeTerms"
                    name="agree"
                    type="checkbox"
                    required
                    class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                  />
                  <label for="agree" class="ml-2 block text-sm text-gray-900">
                    我同意
                    <a href="#" class="font-medium text-blue-600 hover:text-blue-500">
                      服务条款
                    </a>
                    和
                    <a href="#" class="font-medium text-blue-600 hover:text-blue-500">
                      隐私政策
                    </a>
                  </label>
                </div>
              </div>
  
              <div>
                <button
                  type="submit"
                  :disabled="loading"
                  class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-all duration-200"
                >
                  <svg v-if="loading" class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  {{ loading ? '注册中...' : '创建账户' }}
                </button>
              </div>
            </form>
  
            <!-- 提示消息 -->
            <div v-if="message" class="mt-4 p-3 rounded-md" :class="successful ? 'bg-green-50 text-green-800' : 'bg-red-50 text-red-800'">
              {{ message }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, reactive } from 'vue';
  import { useRouter } from 'vue-router';
  import { useAuthStore } from '@/store/AuthStore';
  import axios from 'axios';
  
  const router = useRouter();
  const authStore = useAuthStore();
  
  const registerForm = reactive({
    username: '',
    email: '',
    first_name: '',
    last_name: '',
    password: '',
    password2: ''
  });
  
  const agreeTerms = ref(false);
  const showPassword = ref(false);
  const loading = ref(false);
  const message = ref('');
  const successful = ref(false);
  const errors = reactive({
    username: '',
    email: '',
    first_name: '',
    last_name: '',
    password: '',
    password2: '',
    non_field_errors: ''
  });
  
  const resetErrors = () => {
    errors.username = '';
    errors.email = '';
    errors.first_name = '';
    errors.last_name = '';
    errors.password = '';
    errors.password2 = '';
    errors.non_field_errors = '';
  };
  
  const handleRegister = async (): Promise<void> => {
    loading.value = true;
    resetErrors();
    message.value = '';
    
    try {
      const response = await axios.post('http://123.56.118.72:8000/api/auth/register/', registerForm);
      
      successful.value = true;
      message.value = '注册成功！正在跳转到登录页面...';
      
      setTimeout(() => {
        router.push('/login');
      }, 1500);
    } catch (error: any) {
      successful.value = false;
      
      if (error.response && error.response.data) {
        const responseErrors = error.response.data;
        
        // 映射后端返回的错误到本地错误对象
        Object.keys(responseErrors).forEach(key => {
          if (key in errors) {
            errors[key] = Array.isArray(responseErrors[key]) 
              ? responseErrors[key].join(' ') 
              : responseErrors[key];
          }
        });
        
        if (responseErrors.non_field_errors) {
          message.value = Array.isArray(responseErrors.non_field_errors) 
            ? responseErrors.non_field_errors.join(' ') 
            : responseErrors.non_field_errors;
        } else {
          message.value = '注册失败，请检查表单内容并重试。';
        }
      } else {
        message.value = '注册过程中发生错误，请稍后再试。';
        console.error('Registration error:', error);
      }
    } finally {
      loading.value = false;
    }
  };
  </script>