# Kurulum

Bu rehber, Aspectify geliştirme ortamını kurmanıza yardımcı olacak.

## Ön Gereksinimler

- Python 3.10
- pip (Python paket yükleyicisi)
- Git

## Adım 1: Depoyu Klonlayın

```bash
git clone https://github.com/hanifekaptan/Aspectify.git
cd Aspectify
```

## Adım 2: Sanal Ortam Oluşturun

```bash
python -m venv .venv
```

#### Windows:
```bash
.venv\Scripts\activate
```

#### macOS/Linux:
```bash
source .venv/bin/activate
```

## Adım 3: Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

## Adım 4: Ortam Yapılandırması

Proje kök dizininde `.env` dosyası oluşturun:

```env
GOOGLE_API_KEY=your_google_api_key_here
LOG_LEVEL=INFO
PROJECT_NAME="Aspectify"
PROJECT_VERSION="1.0.0"
```

## Adım 5: Kurulumu Doğrulayın

Test betiğini çalıştırarak her şeyin çalıştığını doğrulayın:

```bash
python main.py
```

Şuna benzer bir çıktı görmelisiniz:

```
--------------------------------------------------
Test verileri okunuyor ve duygu analizi yapılıyor...
--------------------------------------------------

Analiz Edilen Metin: Yeni aldığım telefonun kamerası harika fotoğraflar çekiyor ama bataryası bir günü zor çıkarıyor.
Beklenen Duygu: neutral
Ajan Sonucu (Polarite): neutral
Ajan Sonucu (Skor): 0.5
Ajan Sonucu (Aspektler): [AspectAnalysisResponse(aspect='kamera', sentiment='positive', score=0.98), AspectAnalysisResponse(aspect='batarya', sentiment='negative', score=0.99)]
```

## Sorun Giderme

### Yaygın Sorunlar

1. **ModuleNotFoundError**: Sanal ortamı aktifleştirdiğinizden emin olun
2. **API Key Hatası**: `.env` dosyasında Google API anahtarınızın doğru ayarlandığını kontrol edin

### Google API Anahtarı Alma

1. [Google AI Studio](https://aistudio.google.com/) adresini ziyaret edin
2. Yeni bir proje oluşturun veya mevcut birini seçin
3. API anahtarı oluşturun
4. Anahtarı `.env` dosyanıza kopyalayın

## Sonraki Adımlar

- [Yapılandırma](configuration.md) - Uygulama yapılandırması hakkında bilgi edinin
- [Hızlı Başlangıç](quick-start.md) - İlk analizinizi çalıştırın
