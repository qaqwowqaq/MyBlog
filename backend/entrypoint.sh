#!/bin/sh

# 确保 STATIC_ROOT 和 MEDIA_ROOT 目录存在
mkdir -p /app/staticfiles /app/media
chmod -R 755 /app/staticfiles /app/media

# 应用数据库迁移
python manage.py migrate

# 收集静态文件
python manage.py collectstatic --noinput

# 运行 Gunicorn
exec "$@"