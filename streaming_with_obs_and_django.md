# Создание стрима с использованием OBS и Django

## 1. Настройка OBS:
1. **Установите OBS**: Скачайте и установите OBS с [официального сайта](https://obsproject.com/).
2. **Настройте поток**: В OBS, перейдите в `Settings` > `Stream` и выберите `Custom...` в качестве сервиса. Укажите URL и Stream Key вашего сервера RTMP (подробнее об этом ниже).

## 2. Настройка сервера RTMP:
Для создания RTMP-сервера вы можете использовать nginx с модулем RTMP или специализированный сервер, например, Wowza.

### Пример настройки nginx с модулем RTMP:
1. **Установите nginx с RTMP-модулем**. В Ubuntu это можно сделать так:
   ```bash
   sudo apt update
   sudo apt install libnginx-mod-rtmp
   ```
2. **Настройте nginx**:
   Добавьте следующий блок в ваш конфигурационный файл nginx (`/etc/nginx/nginx.conf`):
   ```nginx
   rtmp {
       server {
           listen 1935;
           chunk_size 4096;

           application live {
               live on;
               record off;
           }
       }
   }

   http {
       ...
       server {
           listen 8080;

           location / {
               root /path/to/your/django/project;
           }

           location /hls {
               types {
                   application/vnd.apple.mpegurl m3u8;
                   video/mp2t ts;
               }
               alias /tmp/hls;
               expires -1;
           }
       }
   }
   ```
3. **Перезапустите nginx**:
   ```bash
   sudo systemctl restart nginx
   ```

## 3. Интеграция с Django:
1. **Установите Django и создайте проект**:
   ```bash
   pip install django
   django-admin startproject myproject
   cd myproject
   python manage.py startapp livestream
   ```

2. **Настройка модели и представления**:
   В файле `livestream/views.py` добавьте код для отображения видеопотока:
   ```python
   from django.shortcuts import render

   def stream(request):
       return render(request, 'livestream/stream.html')
   ```

3. **Настройка URL**:
   В файле `livestream/urls.py` добавьте маршрутизацию:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('stream/', views.stream, name='stream'),
   ]
   ```

   В файле `myproject/urls.py` подключите приложение:
   ```python
   from django.contrib import admin
   from django.urls import include, path

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('livestream/', include('livestream.urls')),
   ]
   ```

4. **Создайте шаблон**:
   В папке `livestream/templates/livestream/` создайте файл `stream.html` и добавьте HTML-код для воспроизведения HLS-потока:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Live Stream</title>
   </head>
   <body>
       <h1>Live Stream</h1>
       <video width="640" height="360" controls>
           <source src="http://yourdomain.com/hls/live.m3u8" type="application/x-mpegURL">
           Your browser does not support the video tag.
       </video>
   </body>
   </html>
   ```

## 4. Запуск стрима:
1. **Запустите сервер Django**:
   ```bash
   python manage.py runserver
   ```
2. **Настройте OBS**:
   В OBS введите URL вашего RTMP-сервера (например, `rtmp://yourdomain.com/live`) и Stream Key (например, `live`).
3. **Начните трансляцию**.

Теперь вы должны иметь работающий стрим, который можно просматривать на вашем Django сайте.
