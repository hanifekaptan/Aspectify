# Aspectify

[![İngilizce](https://img.shields.io/badge/Language-English-red)](./README.md)
[![Proje Durumu](https://img.shields.io/badge/status-geliştiriliyor-orange)](https://github.com/hanifekaptan/Aspectify)
[![Python Versiyonu](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Lisans](https://img.shields.io/badge/license-Apache-green.svg)](LICENSE)

Aspectify, metin ve ses gibi çok modlu içerikler için tasarlanmış, gelişmiş bir **Yönelim Tabanlı Duygu Analizi (ABSA)** platformudur. Google Gemini ve OpenAI Whisper gibi modern yapay zeka modellerinin gücünü kullanarak, bir metnin sadece genel olarak pozitif mi negatif mi olduğunu değil, aynı zamanda metin içindeki belirli "yönelimlerin" (aspect) duygu eğilimlerini de ortaya çıkarır.

Bu proje, modern yapay zeka mühendisliği prensiplerini ve temiz mimari yaklaşımlarını keşfetmek amacıyla kişisel bir geliştirme projesi olarak hayata geçirilmiştir.

---

## ✨ Temel Özellikler

-   **🎯 Yönelim Tabanlı Analiz:** "Bu telefonun kamerası harika ama bataryası kötü" cümlesinde "kamera" için pozitif, "batarya" için negatif duygu tespiti yapar.
-   **🎤 Çok Modlu Giriş:** Hem metin hem de ses dosyası analizi destekler.
-   **🤖 Modern AI Entegrasyonu:** Gücünü Google Gemini ve OpenAI Whisper gibi en yeni yapay zeka modellerinden alır.
-   **🧩 Modüler ve Temiz Mimari:** "Temiz Kod" ve "İlgilerin Ayrılığı" prensiplerine dayanan, bakımı kolay ve genişletilebilir bir kod tabanına sahiptir.
-   **📊 Detaylı Çıktılar:** Genel polarite, güven skorları, yönelim listesi ve ilgili alıntılar içeren zengin sonuçlar sunar.

## 🚀 Projenin Mevcut Durumu

⚠️ **Bu proje aktif geliştirme aşamasındadır.** Çekirdek analiz mantığı ve modüler yapı oluşturulmuştur. REST API, Docker desteği ve veritabanı entegrasyonu gibi özellikler yol haritasında yer almaktadır.

## ⚙️ Nasıl Çalışır?

Aspectify, istekleri akıllıca işlemek için modüler ve ajan tabanlı bir mimari kullanır. Akış, farklı içerik türlerini yönetecek şekilde düzenlenmiştir.

**`Kullanıcı Girdisi (Metin/Ses) -> [1. Mantık Katmanı] -> [2. Ajan] -> [3. AI Araçları] -> [4. Birleştirilmiş Yanıt]`**

1.  **Mantık Katmanı (`/logic`):** İlk temas noktasıdır. İçerik türünü (metin/ses) belirler ve dili tespit eder. Girdi bir ses dosyası ise, metne dönüştürmek için **Transkripsiyon Aracı**'nı kullanır.
2.  **Orkestrasyon Ajanı (`/agents`):** Sistemin "beynidir". Hazırlanan metni alır ve hangi araçları kullanacağına karar verir. Analiz aracını çağırmaktan ve nihai çıktının doğru şekilde yapılandırılmasından sorumludur.
3.  **AI Araçları (`/tools`):** Temel görevleri yerine getiren özel işçilerdir. Ana araç, verilen metin üzerinde detaylı yönelim tabanlı analiz yapmak için Gemini modelini kullanan **ABSA Analiz Aracı**'dır.
4.  **Yapılandırılmış Yanıt (`/schemas`):** Ajan, AI araçlarından gelen ham çıktıyı alır ve kullanıcıya döndürmeden önce Pydantic modellerini kullanarak temiz, öngörülebilir bir JSON nesnesine formatlar.

## 🛠️ Teknoloji Yığını

| Kategori            | Çekirdek Teknolojiler            | Planlananlar            |
| ------------------- | -------------------------------- | ----------------------- |
| **Backend**         | Python 3.10+                     | FastAPI                 |
| **Yapay Zeka / ML** | Google Gemini, OpenAI Whisper    | LangChain               |
| **Veri Doğrulama**  | Pydantic                         | -                       |
| **Altyapı**         | -                                | Docker, SQLite      |
| **Veritabanı**      | -                                | Pinecone (Vektör DB)    |

## 📂 Proje Yapısı

Proje, ilgileri ayırarak gezinmeyi ve genişletmeyi kolaylaştıran temiz bir mimariyi takip eder.

```
Aspectify/
├── app/
│   ├── agents/         # İş akışını yönetir (sistemin "beyni")
│   ├── ai_models/      # AI modelleri ile alt seviye entegrasyonlar
│   ├── core/           # Yapılandırma, loglama ve temel ayarlar
│   ├── logic/          # İş mantığı (transkripsiyon, dil tespiti)
│   ├── schemas/        # İstek/yanıt doğrulaması için Pydantic modelleri
│   └── tools/          # Ajanın kullanabileceği özel araçlar (örn: ABSA analiz aracı)
├── test_data/          # Test için örnek veriler
├── tests/              # Test paketi (geliştirme aşamasında)
├── docs/               # Detaylı proje dokümantasyonu
├── main.py             # Uygulamayı çalıştırmak için ana giriş noktası
├── requirements.txt
├── .env.example        # Ortam değişkenleri şablonu
└── README_TR.md
```

## 🚀 Hızlı Başlangıç

Projeyi yerel makinenizde çalıştırmak için bu adımları izleyin.

1.  **Depoyu klonlayın:**
    ```bash
    git clone https://github.com/hanifekaptan/Aspectify.git
    cd Aspectify
    ```
2.  **Sanal ortam oluşturun ve etkinleştirin:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Windows'ta `.venv\Scripts\activate` kullanın
    ```
3.  **Gerekli kütüphaneleri yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **API anahtarlarınızı yapılandırın:**
    `.env.example` dosyasını `.env` olarak kopyalayın ve kendi API anahtarlarınızı girin.
    ```bash
    cp .env.example .env
    ```

Detaylı kurulum ve kullanım talimatları için lütfen tam dokümantasyona başvurun.

## 📖 Detaylı Dokümantasyon

Projenin mimarisi, geliştirme standartları ve gelecek planları hakkındaki tüm detaylar, kapsamlı dokümantasyonumuzda mevcuttur.

➡️ **[Proje Dokümantasyonunu Oku](./docs/README.md)**

## 🤝 Katkıda Bulunma

Bu kişisel bir geliştirme projesi olsa da, fikir ve önerilere her zaman açığım. Katkıda bulunmak isterseniz, lütfen **[Geliştirme Kılavuzu](./docs/development/README.md)**'nu inceleyin.

## 📄 Lisans

Bu proje, MIT Lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız.