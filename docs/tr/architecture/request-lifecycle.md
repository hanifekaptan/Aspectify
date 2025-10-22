# İstek Yaşam Döngüsü ve Veri Akışı

Bu belge, bir kullanıcının Aspectify API'sine bir istek gönderdiği andan, işlenmiş yanıtı aldığı ana kadar geçen süreci ve verinin sistem içindeki yolculuğunu açıklar.

## Yüksek Seviye Akış

Sistemdeki veri akışı, mantıksal katmanlar arasında gerçekleşir:

1.  **API Katmanı**: Kullanıcıdan gelen istek alınır, kimlik doğrulaması yapılır ve Pydantic modelleri ile doğrulanır.
2.  **Çekirdek Mantık & Servisler Katmanı**: Doğrulanan veri, işlenmek üzere Ajanlara (Agents) ve servislere yönlendirilir. Analiz ve diğer tüm işlemler bu katmanda gerçekleşir.
3.  **Veri Katmanı**: İşlem sırasında gerekli olan verilere erişilir.
4.  **API Katmanı**: İşlem sonucu elde edilen veri, Pydantic modelleri kullanılarak formatlanır ve standart bir JSON yanıtı olarak kullanıcıya döndürülür.

## Detaylı İşlem Adımları

Çekirdek Mantık katmanındaki analiz süreci beş ana adımdan oluşur:

### 1. Giriş İşleme (Input Processing)

Sisteme gelen her istek ilk olarak içeriğin türünü (`metin`, `ses dosyası` vb.) belirleyen bir adımdan geçer. Ardından, içeriğin dili tespit edilerek sonraki adımlara hazırlık yapılır.

```
Kullanıcı Girişi → İçerik Türü Belirleme → Dil Tespiti
```

### 2. İçerik Hazırlama (Content Preparation)

Eğer gelen içerik bir ses dosyası ise, `Whisper` modeli kullanılarak metne dönüştürülür (transkripsiyon). Gelen içerik zaten metin formatındaysa, bu adım atlanarak dil tespiti adımına geçilir.

```
Ses Dosyası → Transkripsiyon → Metin → Dil Tespiti
```
```
Metin → Dil Tespiti
```

### 3. Dil Tespiti (Language Detection)

İşlenmek üzere hazırlanan metin, Aspect-Based Sentiment Analysis (ABSA) aracına gönderilirmeden önce dilin içeriği tespit edilir. Tespit edilen dile göre uygun dilde cevap döndürülür.


### 4. Analiz Süreci (Analysis Process)

Hazırlanan metin ve edinilen dil bilgisi, Aspect-Based Sentiment Analysis (ABSA) aracına gönderilir. Bu araç, analiz işlemini gerçekleştirmek için `Gemini` LLM modelini kullanarak metindeki duygu ve aspect'leri çıkarır ve ham bir sonuç üretir.

```
Metin → ABSA Aracı → LLM Model → Sonuç
```

### 5. Sonuç Formatlama (Result Formatting)

Analiz sürecinden elde edilen ham sonuç, önceden tanımlanmış Pydantic şemaları (`schemas`) kullanılarak yapılandırılmış ve tutarlı bir formata dönüştürülür. Son olarak, bu yapı API aracılığıyla standart bir JSON yanıtı olarak kullanıcıya sunulur.

```
Ham Sonuç → Pydantic Model → JSON Yanıt
```