const CACHE_NAME = "tastetracker-cache-v1";

const FILES_TO_CHANGE = [
    "/",
    "/login",
    "/register",
    "/static/css/style.css",
    "/static/js/app.js"
];

// Install event
self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACH_NAME).then(cach => {
            return cach.addAll(FILES_TO_CHANGE);
        })
    );
});

//Fetch event
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});