import axios from 'axios';
import Cookies from 'js-cookie';
import { useAuthStore } from './store/AuthStore';

// 创建axios实例
const api = axios.create({
  baseURL: 'http://123.56.118.72:8000/api',
  withCredentials: false,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
});

// 请求拦截器 - 添加token到请求头
api.interceptors.request.use(
  (config) => {
    const token = Cookies.get('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 响应拦截器 - 处理token过期
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    
    // 检查是否是401错误(未授权)且未尝试过刷新token
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      
      try {
        const refreshToken = Cookies.get('refresh_token');
        if (!refreshToken) throw new Error('No refresh token available');
        
        // 刷新token
        const response = await axios.post(
          'http://123.56.118.72:8000/api/token/refresh/',
          { refresh: refreshToken }
        );
        
        const newAccessToken = response.data.access;
        
        // 更新cookie中的token
        Cookies.set('access_token', newAccessToken, { expires: 1/12 }); // 2小时
        
        // 更新store中的token (直接尝试使用authStore)
        try {
          const authStore = useAuthStore();
          authStore.accessToken = newAccessToken;
        } catch (e) {
          // 如果获取store失败，静默处理
          console.warn('Failed to update auth store', e);
        }
        
        // 使用新token重试原始请求
        originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
        return api(originalRequest);
      } catch (refreshError) {
        // 如果刷新失败，清除用户凭据并重定向到登录页
        try {
          const authStore = useAuthStore();
          authStore.logout();
        } catch (e) {
          // 如果获取store失败，手动清除cookies
          Cookies.remove('access_token');
          Cookies.remove('refresh_token');
        }
        // 重定向到登录页
        window.location.href = '/login';
        return Promise.reject(refreshError);
      }
    }
    
    return Promise.reject(error);
  }
);

export default api;