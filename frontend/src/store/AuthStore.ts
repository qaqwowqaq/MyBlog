import { defineStore } from 'pinia';
import axios from 'axios';
import Cookies from 'js-cookie';
import api from '../axiosConfig';

interface UserState {
  accessToken: string | null;
  refreshToken: string | null;
  user: {
    id: number | null;
    username: string | null;
    email: string | null;
    firstName: string | null;
    lastName: string | null;
  };
}

interface RegisterForm {
  username: string;
  email: string;
  first_name: string;
  last_name: string;
  password: string;
  password2: string;
}

export const useAuthStore = defineStore('auth', {
  state: (): UserState => ({
    accessToken: Cookies.get('access_token') || null,
    refreshToken: Cookies.get('refresh_token') || null,
    user: {
      id: null,
      username: null,
      email: null,
      firstName: null,
      lastName: null
    }
  }),
  
  getters: {
    isAuthenticated: (state) => !!state.accessToken,
    getUser: (state) => state.user
  },
  
  actions: {
    async login(username: string, password: string, rememberMe: boolean = false) {
      try {
        const response = await api.post('/login/', {
          username,
          password
        });
        
        const { access, refresh, user } = response.data;
        
        // 设置令牌到cookies
        const accessExpires = rememberMe ? 1/12 : undefined; // 2小时或会话
        const refreshExpires = rememberMe ? 1 : undefined; // 1天或会话
        
        Cookies.set('access_token', access, { expires: accessExpires });
        Cookies.set('refresh_token', refresh, { expires: refreshExpires });
        
        // 设置状态
        this.accessToken = access;
        this.refreshToken = refresh;
        this.user = {
          id: user.id,
          username: user.username,
          email: user.email,
          firstName: user.first_name,
          lastName: user.last_name
        };

        return user;
      } catch (error) {
        console.error('Login failed:', error);
        throw error;
      }
    },
    
    async register(form: RegisterForm) {
      try {
        const response = await api.post('/auth/register/', form);
        return response.data;
      } catch (error) {
        console.error('Registration failed:', error);
        throw error;
      }
    },
    
    async logout() {
      // 清除cookies
      Cookies.remove('access_token');
      Cookies.remove('refresh_token');
      
      // 清除状态
      this.accessToken = null;
      this.refreshToken = null;
      this.user = {
        id: null,
        username: null,
        email: null,
        firstName: null,
        lastName: null
      };
    },
    
    async fetchUserProfile() {
      if (!this.accessToken) return;
      
      try {
        const response = await api.get('/user/profile/');
        const userData = response.data;
        
        this.user = {
          id: userData.id,
          username: userData.username,
          email: userData.email,
          firstName: userData.first_name,
          lastName: userData.last_name
        };
        
        return userData;
      } catch (error) {
        console.error('Failed to fetch user profile:', error);
        throw error;
      }
    },

    // 刷新令牌方法
    async refreshToken() {
      try {
        if (!this.refreshToken) {
          throw new Error("No refresh token available");
        }

        const response = await axios.post(
          'http://123.56.118.72:8000/api/token/refresh/',
          { refresh: this.refreshToken }
        );

        const newAccessToken = response.data.access;
        
        // 更新 cookies 和 store
        Cookies.set('access_token', newAccessToken, { expires: 1/12 });
        this.accessToken = newAccessToken;
        
        return newAccessToken;
      } catch (error) {
        console.error('Token refresh failed:', error);
        this.logout();
        throw error;
      }
    }
  }
});