// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    '/static/css/style.css',
    '/static/css/flexboxgrid.min.css',
    '/static/owlcarousel/owl.carousel.min.css',
    '/static/owlcarousel/owl.theme.default.min.css',
    '/static/script.js',
    '/static/owlcarousel/owl.carousel.min.js',
    '/static/img/logos.jpg',
    '/static/img/logo.gif',
    '/static/img/face.png',
    '/static/img/insta.png',
    '/static/img/twit.png',
    '/static/img/yt.png',
    '/static/img/gmail.png',
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
/*
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/');
            })
    )
});
*/

self.addEventListener("fetch", function(event){
    event.respondWith(
        fetch(event.request)
        .then(function(result){
            return caches.open(staticCacheName)
            .then(function(c){
                c.put(event.request.url, result.clone())
                return result
            })
        })
        .catch(function(e){
            return caches.match(event.request)
        })
    )
});