# Yapılandırma

Aspectify, `app.core.config` modülü aracılığıyla merkezi bir yapılandırma sistemi kullanır.

## Yapılandırma Dosyası

Ana yapılandırma `app/core/config.py` dosyasında tanımlanır:

```python
from dotenv import load_dotenv
load_dotenv()

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    PROJECT_NAME: str = "Aspectify"
    PROJECT_VERSION: str = "1.0.0"
    LOG_LEVEL: str = "INFO"
    GOOGLE_API_KEY: SecretStr | None = None
    GEMINI_2_5_PRO_MODEL: str = "gemini-2.5-pro"
```

## Ortam Değişkenleri

Kurulum (installation) dosyasındaki talimatları takip ederek `.env` dosyası oluşturun.

## Yapılandırma Seçenekleri

### Log Seviyeleri

Mevcut log seviyeleri:

<!-- - `DEBUG`: Hata ayıklama için ayrıntılı bilgi -->
- `INFO`: Program yürütmesi hakkında genel bilgi
<!-- - `WARNING`: Beklenmeyen bir şey oldu
- `ERROR`: Ciddi bir sorun oluştu
- `CRITICAL`: Çok ciddi bir hata oluştu -->

### AI Modelleri

Şu anda desteklenen Gemini modelleri:

- `gemini-2.5-pro`: Gemini latest model

## Yapılandırmayı Kullanma

Kodunuzda yapılandırma ayarlarına erişin:

```python
from app.core.config import settings

print(f"Proje: {settings.PROJECT_NAME}")
print(f"Sürüm: {settings.PROJECT_VERSION}")
print(f"Log Seviyesi: {settings.LOG_LEVEL}")

if settings.GOOGLE_API_KEY:
    api_key = settings.GOOGLE_API_KEY.get_secret_value()
```

## Doğrulama

Yapılandırma sistemi doğrulama için Pydantic kullanır:

- Tür kontrolünü sağlayarak dğru veri türlerini sağlar.
- Varsayılan değerler ile makul değerlerini atar.

## Sorun Giderme

### Yapılandırma Yüklenmiyor

1. `.env` dosyasının proje kök dizininde olduğunu kontrol edin
2. Dosya izinlerini doğrulayın
3. `.env` dosyasında sözdizimi hatası olmadığından emin olun

### API Anahtarı Sorunları

1. Anahtarın doğru kopyalandığını doğrulayın (ekstra boşluk yok)
2. Anahtarın uygun izinlere sahip olduğunu kontrol edin
3. Anahtarın süresi dolmamış olduğundan emin olun

### Model Yapılandırması

1. Model adının doğru olduğunu doğrulayın
2. Modelin bölgenizde mevcut olduğunu kontrol edin
3. API anahtarının modele erişimi olduğundan emin olun
