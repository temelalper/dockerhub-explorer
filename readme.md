# 🐳 DockerHub Explorer

Bu proje, DockerHub API'sini kullanarak image araması yapmanızı ve beğendiklerinizi favorilerinize eklemenizi sağlayan modern bir web uygulamasıdır.

## 🛠️ Mimari ve Teknolojiler

Bu proje **REST API** mimarisi kullanılarak geliştirilmiştir.

* **Backend:** Python, Flask (API Endpoints)
* **Veritabanı:** SQLite & SQLAlchemy ORM
* **Frontend:** Vue.js 3 (CDN), Bootstrap 5
* **Bağlantı:** Python `requests` kütüphanesi ile DockerHub entegrasyonu.

## 🚀 Kurulum ve Çalıştırma

Projeyi bilgisayarınızda ayağa kaldırmak için aşağıdaki adımları izleyin.

### 1. Gereksinimler
* Python 3.x yüklü olmalıdır.

### 2. Kurulum
Terminali açın ve proje klasörüne gidip gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt