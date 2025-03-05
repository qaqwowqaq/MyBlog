export interface User {
    id: number;
    username: string;
    email?: string;
    first_name?: string;
    last_name?: string;
  }
  
  export interface Category {
    id: number;
    name: string;
    slug: string;
    description?: string;
  }
  
  export interface Tag {
    id: number;
    name: string;
  }
  
  export interface Post {
    id: number;
    title: string;
    slug: string;
    content?: string;
    summary?: string;
    cover_image?: string;
    author: string;
    author_id: number;
    category: Category;
    tags: Tag[];
    views: number;
    likes: number;
    status: 'published' | 'draft';
    created_at: string;
    updated_at: string;
    comment_count?: number;
  }
  
  export interface Comment {
    id: number;
    content: string;
    article_id: number;
    user: User;
    parent_id?: number;
    created_at: string;
    replies?: Comment[];
  }
  
  export interface PaginatedResponse<T> {
    count: number;
    next: string | null;
    previous: string | null;
    results: T[];
  }