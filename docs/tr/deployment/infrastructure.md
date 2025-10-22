# Çalışma Ortamı Gereksinimleri

Bu belge, Aspectify platformunu mevcut haliyle çalıştırmak için gereken ortamı ve projenin gelecekteki hedefleri için planlanan altyapıyı tanımlar.

## Mevcut Durum: Temel Gereksinimler

Projenin şu anki versiyonunu çalıştırmak için aşağıdaki yazılımların sisteminizde kurulu olması yeterlidir:

-   **Python:** `3.10`
-   **pip:** Python paketlerini yüklemek için (`requirements.txt` dosyasını kullanır).
-   **Git:** Proje kodunu indirmek için.

### Harici Bağımlılıklar

Uygulamanın çekirdek analiz mantığı, aşağıdaki harici servislere erişim için geçerli API anahtarlarına ihtiyaç duyar. Bu anahtarların `.env` dosyasında yapılandırılması zorunludur:

-   **Google Gemini API Anahtarı**
-   **OpenAI Whisper API Anahtarı**

## Gelecek Planları: Planlanan Altyapı

Projenin yol haritası, onu daha ölçeklenebilir ve sağlam bir servis haline getirmek için aşağıdaki teknolojileri içermektedir. Bu bileşenler eklendikçe bu doküman güncellenecektir.

-   **Konteynerleştirme (Docker):** Uygulamanın ve bağımlılıklarının her ortamda tutarlı bir şekilde çalışmasını sağlamak için Docker ve Docker Compose entegrasyonu planlanmaktadır.
-   **Veri Katmanı (Database):** Analiz sonuçlarını kalıcı olarak saklamak ve daha karmaşık sorgular yapabilmek için PostgreSQL (yapısal veri) ve Pinecone (vektör veri) veritabanları eklenecektir.
-   **API Katmanı (FastAPI):** Uygulamanın harici servisler tarafından kolayca kullanılabilmesi için bir REST API arayüzü FastAPI kullanılarak geliştirilecektir.