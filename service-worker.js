    const CACHE_NAME = 'cheshmash-decori-cache-v1';
    const urlsToCache = [
      '/',
      '/manifest.json'
      // اگر آیکون رو اضافه کردی، اینجا باید مسیرش رو هم اضافه کنی
      // '/icons/icon-192x192.png',
      // '/icons/icon-512x512.png'
    ];

    // نصب Service Worker و کش کردن منابع ثابت
    self.addEventListener('install', (event) => {
      event.waitUntil(
        caches.open(CACHE_NAME)
          .then((cache) => {
            console.log('Opened cache');
            return cache.addAll(urlsToCache);
          })
      );
    });

    // فعال‌سازی Service Worker و پاکسازی کش‌های قدیمی
    self.addEventListener('activate', (event) => {
      const cacheWhitelist = [CACHE_NAME];
      event.waitUntil(
        caches.keys().then((cacheNames) => {
          return Promise.all(
            cacheNames.map((cacheName) => {
              if (cacheWhitelist.indexOf(cacheName) === -1) {
                return caches.delete(cacheName);
              }
            })
          );
        })
      );
    });

    // واکشی (Fetch) منابع: اول برو سراغ کش، اگه نبود از شبکه بیار
    self.addEventListener('fetch', (event) => {
      event.respondWith(
        caches.match(event.request)
          .then((response) => {
            // برگشت از کش در صورت وجود
            if (response) {
              return response;
            }
            // در غیر این صورت، از شبکه بگیر
            return fetch(event.request);
          })
      );
    });
