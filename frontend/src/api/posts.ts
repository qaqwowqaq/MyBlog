// src/api/posts.ts
import apiClient from './index';

export const PostsApi = {
  getAll(params = {}) {
    return apiClient.get('/posts/', { params });
  },
  get(slug: string) {
    return apiClient.get(`/posts/${slug}/`);
  },
  create(data: any) {
    return apiClient.post('/posts/', data);
  },
  update(slug: string, data: any) {
    return apiClient.put(`/posts/${slug}/`, data);
  },
  delete(slug: string) {
    return apiClient.delete(`/posts/${slug}/`);
  },
  like(slug: string) {
    return apiClient.post(`/posts/${slug}/like/`);
  },
  view(slug: string) {
    return apiClient.post(`/posts/${slug}/view/`);
  },
};