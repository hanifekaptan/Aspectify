# Hızlı Başlangıç

Bu rehber, Aspectify ile ilk duygu analizinizi yapmanıza yardımcı olacak.

## Temel Kullanım

### 1. Metin Analizi

En basit kullanım şekli:

```python
import asyncio
from app.agents.absa_agent import run_absa

async def main():
    text = "Bu telefonun kamerası harika ama bataryası çok kötü."
    result = await run_absa(text)
    
    print(f"Genel Duygu: {result.polarity}")
    print(f"Güven Skoru: {result.score}")
    print("Yönelimler (aspects):")
    for aspect in result.aspects:
        print(f"  - {aspect.aspect}: {aspect.sentiment} ({aspect.score})")

asyncio.run(main())
```

### 2. Ses Dosyası Analizi

Ses dosyalarını da analiz edebilirsiniz:

```python
import asyncio
from app.agents.absa_agent import run_absa

async def main():
    audio_path = "path/to/your/audio.wav"
    result = await run_absa(audio_path)
    
    print(f"Transkripsiyon: {result.text}")
    print(f"Genel Duygu: {result.polarity}")
    print(f"Güven Skoru: {result.score}")

asyncio.run(main())
```

## Desteklenen Formatlar

### Metin Girişi
- Doğrudan metin string'i
- Herhangi bir dilde metin

### Ses Dosyaları
- `.wav` - WAV formatı
- `.mp3` - MP3 formatı
- `.m4a` - M4A formatı
- `.flac` - FLAC formatı

## Örnek Çıktı

```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
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
      "quote": "bataryası çok kötü"
    }
  ],
  "message": "ABSA completed successfully.",
  "text": "Bu telefonun kamerası harika ama bataryası çok kötü."
}
```

## Duygu Türleri

### Polarity (Genel Duygu)
- `positive`: Pozitif duygu
- `negative`: Negatif duygu
- `neutral`: Nötr duygu

### Sentiment (Yönelim (aspect) Duygusu)
- `positive`: Pozitif
- `negative`: Negatif
- `neutral`: Nötr

## Güven Skorları

Skorlar 0.0 ile 1.0 arasında değişir:

- **0.0 - 0.3**: Düşük güven
- **0.3 - 0.7**: Orta güven
- **0.7 - 1.0**: Yüksek güven

## Hızlı Test

Test verilerinizi kullanarak hızlı bir test yapın:

```bash
python main.py
```

Bu komut `test_data/text/test_texts.jsonl` dosyasındaki örnek metinleri analiz eder.

## Gelişmiş Kullanım

### Özel Dil Belirtme

Dil tespiti, uygulamaya entegre edilmiş ilgili modüller tarafından otomatik olarak tespit edilmesine karşın, aşağıdaki kullanım ile istenilen dil girişi sağlanabilir.

```python
from app.tools.absa_analyzer import absa_analyzer_tool

result = absa_analyzer_tool.invoke({
    "text": "Bu ürün gerçekten harika!",
    "language": "tr"
})

result = absa_analyzer_tool.invoke({
    "text": "This product is amazing!",
    "language": "en"
})
```

### Toplu Analiz

```python
import asyncio
from app.agents.absa_agent import run_absa

async def analyze_multiple_texts(texts):
    results = []
    for text in texts:
        result = await run_absa(text)
        results.append(result)
    return results

texts = [
    "Bu telefon harika!",
    "Kamera kalitesi kötü.",
    "Fiyat uygun ama performans yetersiz."
]

results = asyncio.run(analyze_multiple_texts(texts))
```

## Sorun Giderme

### Yaygın Hatalar

1. **API Key Hatası**: `.env` dosyasında Google API anahtarınızı kontrol edin
2. **Boş Metin**: Analiz edilecek metin boş olamaz
3. **Desteklenmeyen Format**: Ses dosyası formatını kontrol edin

### Performans İpuçları

1. **Toplu İşlem**: Birden fazla metni aynı anda işleyin
2. **Önbellekleme**: Sonuçları önbelleğe alın
3. **Asenkron Kullanım**: `async/await` kullanın

## Sonraki Adımlar

- [Mimari](../architecture/overview.md) - Sistem mimarisi hakkında genel bilgi
- [Geliştirme](../development/local-setup.md) - Geliştirme kılavuzu hakkında bilgi
- [Dağıtım](../deployment/infrastructure.md) - Dağıtım için altyapı gereksinimleri hakkında bilgi
- [API Referansı](../api/endpoints.md) - API endpointleri hakkında bilgi