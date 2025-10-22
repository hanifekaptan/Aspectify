# Production (Canlı Ortam) Kurulum Kılavuzu

Bu kılavuz, Aspectify uygulamasının **kalıcı ve stabil bir servis olarak** canlı ortama nasıl dağıtılacağını açıklar.

**Ön Koşul:** Bu kılavuza başlamadan önce, projenin temel kurulum adımlarını bildiğiniz varsayılmaktadır. Gerekirse, lütfen önce **[Ana Kurulum Kılavuzu](../getting-started/installation.md)**'nu inceleyin.

## 1. Production için Yapılandırma

Geliştirme ortamından farklı olarak, production ortamı için `.env` dosyasında bazı değerlerin dikkatli bir şekilde ayarlanması gerekir.

1.  Sunucuda proje kodunun bulunduğu dizine gidin.
2.  `cp .env.example .env` komutu ile `.env` dosyanızı oluşturun.
3.  `.env` dosyasını açın ve **özellikle aşağıdaki değerleri** production için ayarladığınızdan emin olun:

    ```dotenv
    # .env (Production için Kritik Alanlar)

    # UYGULAMA AYARLARI
    # Bu, uygulamanın debug modunu kapatır ve performansı artırır.
    ENVIRONMENT=production

    # GÜVENLİK
    # 'openssl rand -hex 32' gibi bir komutla oluşturulmuş,
    # tahmin edilemez, uzun ve karmaşık bir anahtar girin.
    SECRET_KEY=buraya_çok_güçlü_ve_rastgele_bir_anahtar_girmelisiniz

    # LOGLAMA
    # Production'da gereksiz logları önlemek için INFO veya WARNING kullanın.
    LOG_LEVEL=INFO

    # HARİCİ SERVİS API ANAHTARLARI
    # Tüm API anahtarlarının production için olan anahtarlar olduğundan emin olun.
    GEMINI_API_KEY=[PRODUCTION_GEMINI_API_ANAHTARINIZ]
    ```
**Önemli Not:** Proje şu anda aktif geliştirme aşamasındadır. Docker desteği, veritabanı entegrasyonu ve bir API katmanı henüz mevcut değildir. Bu kılavuz, projenin mevcut komut satırı tabanlı çalışmasını açıklamaktadır.