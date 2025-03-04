"""
生产环境配置
"""

from .settings import *

DEBUG = False

#ALLOWED_HOSTS = ['123.56.118.72', 'yourdomain.com']  # 添加您的域名

# 静态文件配置
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 安全设置
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

# 数据库连接池
DATABASES['default']['CONN_MAX_AGE'] = 60

# 缓存配置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django_error.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}