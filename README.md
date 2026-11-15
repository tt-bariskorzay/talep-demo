# Talep uygulaması: CI/CD demosu

Eğitim sunumunda kullanılan küçük bir talep uygulaması. Bir değişikliğin pull request'ten prod ortamına kadar nasıl ilerlediğini göstermek için hazırlandı.

- `backend/`: Django ve PostgreSQL
- `frontend/`: Vue arayüzü, nginx ile sunulur
- `docker-compose.yml`: üç container (veritabanı, arka uç, arayüz)
- `.github/workflows/ci.yml`: test → imaj (GHCR) → test ortamı → onay → prod

## Yerelde çalıştırma

```
docker compose up -d --build
```

Arayüz: http://localhost:8080
