# Product Management Microservice

Bu proje, **FastAPI** kullanılarak geliştirilmiş, **PostgreSQL** veritabanı ile asenkron bir şekilde haberleşen (asyncpg), katmanlı mimariye sahip bir ürün yönetim mikroservisidir.

## 🚀 Özellikler

- **Asenkron Yapı:** `asyncio`, `asyncpg` ve `FastAPI` ile yüksek performanslı I/O yönetimi.
- **Lifespan Yönetimi:** Uygulama ömrü boyunca tek bir veritabanı bağlantı havuzu (connection pool) yönetimi.
- **Katmanlı Mimari:** Router, Service, Repository ve Schema katmanları ile modüler yapı.
- **Özel Hata Yönetimi:** Uygulamaya özel `Exception Handler` yapıları (404 Not Found, 409 Already Exists).
- **Dependency Injection:** Servis ve veritabanı bağımlılıklarının FastAPI DI sistemi ile yönetilmesi.

## 🛠 Kullanılan Teknolojiler

- **Backend Framework:** FastAPI
- **Veritabanı Sürücüsü:** asyncpg (PostgreSQL)
- **Veri Doğrulama:** Pydantic (Schemas)
- **Sunucu:** Uvicorn
- **Dil:** Python 3.9+

## 📁 Proje Yapısı

```text
postgre-microservices/
├── dependencies/       # Bağımlılık yönetimi ve DB Pool sağlayıcıları
├── exceptions/         # Özel hata sınıfları (Custom Exceptions)
├── repositories/       # Veritabanı sorgularının (CRUD) bulunduğu katman
├── routers/            # API uç noktaları (Endpoints)
├── schemas/            # Pydantic modelleri (Data Validation)
├── services/           # İş mantığının (Business Logic) bulunduğu katman
├── config.py           # Ortam değişkenleri ve yapılandırma
└── main.py             # Uygulama giriş noktası ve Lifespan yönetimi