# Yanıt Modelleri

Aspectify API'si, yapılandırılmış ve tip güvenli yanıt modelleri kullanır.

## Genel Bakış

Tüm API yanıtları Pydantic modelleri kullanarak doğrulanır ve serileştirilir. Bu, tip güvenliği, otomatik doğrulama ve API dokümantasyonu sağlar.

## Ana Yanıt Modelleri

### ABSAResponse

Ana duygu analizi yanıt modeli.

```python
class ABSAResponse(BaseModel):
    id: str
    polarity: str
    score: float
    aspects: List[AspectAnalysisResponse]
    message: str
    text: str
```

#### Alanlar

| Alan | Tip | Açıklama |
|------|-----|----------|
| `id` | `str` | Benzersiz analiz ID'si (UUID) |
| `polarity` | `str` | Genel duygu (positive/negative/neutral) |
| `score` | `float` | Güven skoru (0.0-1.0) |
| `aspects` | `List[AspectAnalysisResponse]` | Aspect analizleri listesi |
| `message` | `str` | İşlem durumu mesajı |
| `text` | `str` | Analiz edilen metin |

#### Örnek

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
    }
  ],
  "message": "ABSA completed successfully.",
  "text": "Bu telefonun kamerası harika."
}
```

### AspectAnalysisResponse

Aspect analizi yanıt modeli.

```python
class AspectAnalysisResponse(BaseModel):
    aspect: str
    sentiment: str
    score: float
    quote: str
```

#### Alanlar

| Alan | Tip | Açıklama |
|------|-----|----------|
| `aspect` | `str` | Aspect adı (örn: "kamera", "batarya") |
| `sentiment` | `str` | Aspect duygusu (positive/negative/neutral) |
| `score` | `float` | Güven skoru (0.0-1.0) |
| `quote` | `str` | Metinden ilgili alıntı |

#### Örnek

```json
{
  "aspect": "kamera",
  "sentiment": "positive",
  "score": 0.95,
  "quote": "kamera harika fotoğraflar çekiyor"
}
```

### LLMResponse

LLM model yanıt modeli.

```python
class LLMResponse(BaseModel):
    polarity: str
    score: float
    aspects: List[AspectAnalysisResponse]
```

#### Alanlar

| Alan | Tip | Açıklama |
|------|-----|----------|
| `polarity` | `str` | Genel duygu (positive/negative/neutral) |
| `score` | `float` | Güven skoru (0.0-1.0) |
| `aspects` | `List[AspectAnalysisResponse]` | Aspekt analizleri listesi |

#### Örnek

```json
{
  "polarity": "positive",
  "score": 0.8,
  "aspects": [
    {
      "aspect": "kalite",
      "sentiment": "positive",
      "score": 0.9,
      "quote": "kalite çok iyi"
    }
  ]
}
```

## İstek Modelleri

### MultiModalRequest

Çoklu modal istek modeli.

```python
class MultiModalRequest(BaseModel):
    data: str
    language: Optional[str] = None
```

#### Alanlar

| Alan | Tip | Açıklama |
|------|-----|----------|
| `data` | `str` | Analiz edilecek metin veya dosya yolu |
| `language` | `Optional[str]` | İsteğe bağlı dil kodu |

#### Örnek

```json
{
  "data": "Bu ürün gerçekten harika!",
  "language": "tr"
}
```

## Veri Türleri

### Duygu Türleri

```python
from typing import Literal

PolarityType = Literal["positive", "negative", "neutral"]
SentimentType = Literal["positive", "negative", "neutral"]
```

**Değerler:**
- `positive`: Pozitif duygu
- `negative`: Negatif duygu
- `neutral`: Nötr duygu

### İçerik Türleri

```python
from typing import Literal

ContentType = Literal["text", "audio_path"]
```

**Değerler:**
- `text`: Düz metin
- `audio_path`: Ses dosyası yolu

## Doğrulama Kuralları

### ABSAResponse Doğrulama

```python
class ABSAResponse(BaseModel):
    id: str = Field(..., description="Benzersiz analiz ID'si")
    polarity: str = Field(..., regex="^(positive|negative|neutral)$")
    score: float = Field(..., ge=0.0, le=1.0, description="Güven skoru")
    aspects: List[AspectAnalysisResponse] = Field(..., min_items=0)
    message: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)
```

### AspectAnalysisResponse Doğrulama

```python
class AspectAnalysisResponse(BaseModel):
    aspect: str = Field(..., min_length=1, description="Aspekt adı")
    sentiment: str = Field(..., regex="^(positive|negative|neutral)$")
    score: float = Field(..., ge=0.0, le=1.0, description="Güven skoru")
    quote: str = Field(..., min_length=1, description="Metinden alıntı")
```

## Serileştirme

### JSON Serileştirme

```python
# Model'i JSON'a çevir
response = ABSAResponse(...)
json_data = response.model_dump()

# JSON'dan model oluştur
json_str = '{"id": "123", "polarity": "positive", ...}'
response = ABSAResponse.model_validate_json(json_str)
```

### Dict Serileştirme

```python
# Model'i dict'e çevir
response = ABSAResponse(...)
dict_data = response.model_dump()

# Dict'den model oluştur
dict_data = {"id": "123", "polarity": "positive", ...}
response = ABSAResponse.model_validate(dict_data)
```
