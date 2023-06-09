from core.settings.base import env

# Redis
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': env("REDIS_LOCATION", default="redis://localhost:6379"),
    }
}

# Cache time to live is 15 minutes.
CACHE_TTL = 60 * 15