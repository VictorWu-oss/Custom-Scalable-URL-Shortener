# Custom-Scalable-URL-Shortener
Built a distributed URL shortening API with Base62-generated short codes, PostgreSQL-backed storage, SHA-256
deduplication, and idempotent link creation

• Added Redis caching, rate limiting, health checks, and asynchronous analytics processing through a message queue
for high-throughput redirects

• Containerized and deployed services to AWS with Terraform and Kubernetes, adding CI/CD, monitoring, and load
testing to measure p95 latency, throughput, and failure recovery
