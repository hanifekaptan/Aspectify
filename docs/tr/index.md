# Aspectify

**Aspect-Based Sentiment Analysis (ABSA) Uygulaması**

Aspectify, Google'ın Gemini AI modellerini kullanarak metin ve ses içeriği üzerinde yönelim (aspect) tabanlı duygu analizi gerçekleştiren bir uygulamadır. Aynı metin içindeki farklı aspect'ler için duygu analizi yaparak kullanıcı görüşleri hakkında detaylı içgörüler sağlar.

## Özellikler

- 🎯 **Aspect Tabanlı Analiz**: Metin içindeki aspect'leri tespit ederek her bir aspect için duygu analizi yapar.
- 🎤 **Ses Desteği**: Ses dosyalarını deşifre ederek analiz sürecine dahil eder.
- 🌍 **Çok Dilli Destek**: İçerik dili dinamik olarak belirler ve birden fazla dili destekler.
- 🤖 **AI Destekli**: Duygu analizi için Google Gemini modellerini kullanır.
- 📊 **Detaylı Sonuçlar**: Polarite, güven skorları, aspect'ler ve referans gibi detaylı çıktı sağlar
- 📝 **Loglama**: Hata ayıklama ve izleme için uygulama loglaması yapar

## Hızlı Başlangıç

```python
from app.agents.absa_agent import run_absa

text = "Kamera harika ama batarya ömrü kötü."

result = await run_absa(text)
print(f"Genel duygu: {result.polarity}")
print(f"Güven: {result.score}")
for aspect in result.aspects:
    print(f"{aspect.aspect}: {aspect.sentiment} ({aspect.score})")
```

## Mimari

Aspectify modüler bir mimariyi takip eder:
- **agents**: Analiz iş akışları sağlanır ve ajan yapısı yönetilir.
- **ai_models**: Google Gemini ve OpenAI Whisper modelleri entegrasyonları tanımlanır.
- **tools**: Özelleşmiş analiz araçları ve yardımcı programlar sağlanır.
- **logic**: İçerik işleme için temel iş mantığı geliştirilir.
- **schemas**: Veri modelleri tanımlanır.
- **core**: Yapılandırma ve loglama altyapısı oluşturulur.

## Başlangıç

1. [Kurulum](getting-started/installation.md) - Geliştirme ortamını kurun
2. [Yapılandırma](getting-started/configuration.md) - Ayarları yapılandırın
3. [Hızlı Başlangıç](getting-started/quick-start.md) - İlk analizinizi çalıştırın

## Dokümantasyon

1. **Mimari (Architecture):** Bu bölüm, sistemin tasarım temellerini ve genel yapısını ele alır. Sistemin ana bileşenlerini ve bu modüllerin birbiriyle olan etkileşimlerini detaylandırır. Projede kullanılan programlama dilleri, framework'ler ve veritabanlarını içeren teknoloji yığını hakkında bilgi verir. Ayrıca, ana klasör yapısını ve her bir modülün üstlendiği sorumlulukları açıklayarak, bir API isteğinin sistem içindeki yaşam döngüsünü ve nasıl işlendiğini ortaya koyar.

2. **Geliştirme Kılavuzu (Development):** Proje koduna katkıda bulunmayı amaçlayan bu kılavuz, geliştirme sürecinin tamamını kapsar. Bir geliştiricinin kendi bilgisayarında çalışabilmesi için yerel ortamın nasıl kurulacağını adım adım anlatır. Proje genelinde kod tutarlılığını sağlamak amacıyla takip edilmesi gereken kodlama standartlarını ve linter kurallarını tanımlar. Son olarak, yazılan kodun kalitesini ve doğruluğunu sağlamak için testlerin nasıl hazırlanacağını ve çalıştırılacağını gösterir.

3. **Dağıtım Kılavuzu (Deployment):** Bu kılavuz, uygulamanın son kullanıcıya hizmet vereceği canlı bir üretim ortamına kurulması sürecine odaklanmaktadır. Uygulamanın sorunsuz çalışması için gereken sunucu, veritabanı ve diğer altyapı servislerinin gereksinimlerini belirtir. Üretim ortamına özel yapılandırma adımlarını ve ortam değişkenlerinin (environment variables) nasıl ayarlanacağını tarif eder. Ayrıca, sistemin çalışma sırasında ürettiği olayların ve olası hataların takibi için loglama mekanizmasının nasıl yapılandırıldığını açıklar.

4. **API Referansı (API Reference):** Uygulamanın dış dünya ile nasıl iletişim kurduğunu tanımlayan bu teknik referans, API'nin kullanımını detaylandırır. GET /agents ve POST /tasks gibi mevcut tüm API uç noktalarını (endpoints) ve bu uç noktaların işlevlerini içerir. API ile veri alışverişinde kullanılan istek (request) ve yanıt (response) gövdelerinin yapısını tanımlayan veri modellerini (schemas) sunar. (Not: Bu bölüm hazırlık aşamasındadır.)

## Örnek Çıktı

```json
{
  "id": "uuid-burada",
  "polarity": "neutral",
  "score": 0.5,
  "aspects": [
    {
      "aspect": "kamera",
      "sentiment": "positive",
      "score": 0.95,
      "quote": "kamera harika"
    },
    {
      "aspect": "batarya",
      "sentiment": "negative", 
      "score": 0.98,
      "quote": "batarya ömrü kötü"
    }
  ],
  "message": "ABSA başarıyla tamamlandı.",
  "text": "Kamera harika ama batarya ömrü kötü."
}
```

## Destek

Sorular, sorunlar veya katkılar için lütfen [GitHub deposunu](https://github.com/hanifekaptan/Aspectify) ziyaret edin. [Linkedin](https://medium.com/@hanifekaptan) veya [E-mail](hanifekaptan.dev@gmail.com) üzerinden doğrudan iletişime geçebilirsiniz.
