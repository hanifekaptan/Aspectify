# Loglama Sistemi Yapılandırması ve Yönetimi

## Genel Bakış

-   **Log Dosyası:** Tüm loglar, uygulama ana dizinindeki `logs/app.log` dosyasına yazılır.
-   **Yapılandırma:** Log seviyesi ve diğer ayarlar ortam değişkenleri (`environment variables`) ile kontrol edilir.
-   **Log Döndürme (Rotation):** Log dosyasının aşırı büyümesini engellemek için, dosya boyutu 10MB'a ulaştığında otomatik olarak döndürülür ve en son 5 dosya saklanır.

## Yapılandırma

Log seviyesini kontrol etmek için `.env` dosyasında veya sunucu ortam değişkenlerinde aşağıdaki değişkeni ayarlayın.

```env
# Log seviyesi: DEBUG, INFO, WARNING, ERROR, CRITICAL
# Üretim ortamları için önerilen seviye INFO veya WARNING'dir.
LOG_LEVEL=INFO
```

## Log Formatı

Tüm log girişleri, analizi kolaylaştırmak için standart bir formatta yazılır:

-   **Format:** `Zaman Damgası - Logger Adı - Seviye - Mesaj`
-   **Örnek:** `2024-01-15 10:30:45,123 - app.agents.absa_agent - INFO - ABSA analizi başlatıldı`

## Log Dosyası Yönetimi

### Log Döndürme (Log Rotation)

Loglama sistemi, `RotatingFileHandler` kullanarak log dosyalarını otomatik olarak yönetir.

-   **Maksimum Dosya Boyutu:** `10 MB`
-   **Saklanacak Dosya Sayısı:** `5` (app.log, app.log.1, ..., app.log.4)

Bu ayarlar `app/core/logging_config.py` dosyasında tanımlanmıştır ve değiştirilmesi gerekirse bu dosya güncellenmelidir.

### Log Temizleme

Uygulama, eski log dosyalarını otomatik olarak temizleyen bir mekanizma içermemektedir. Sunucuda disk alanı sorunlarını önlemek için, `logrotate` (Linux) gibi standart sistem araçları veya zamanlanmış görevler (cron jobs) ile `logs/` dizinindeki eski dosyaların periyodik olarak arşivlenmesi veya silinmesi önerilir.

## Güvenlik Notları

-   **Erişim Kontrolü:** `logs/` dizinine ve log dosyalarına erişim, sadece yetkili kullanıcılar ve sistem servisleri ile sınırlandırılmalıdır.
-   **Hassas Bilgi:** Geliştirme standartları gereği loglarda hassas bilgi bulunmamalıdır. Ancak yine de, olası sızıntılara karşı log dosyaları güvenli kabul edilmemelidir.