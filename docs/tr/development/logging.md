# Geliştirici için Loglama Kılavuzu

## Logger Kullanımı

Uygulamanın ana logger'ı `app.core.logging_config` modülünden import edilebilir. Ancak en iyi pratik, her modülün kendi logger'ını oluşturmasıdır.

```python
import logging

# Modüle özel bir logger oluşturun
logger = logging.getLogger(__name__)

# Logger'ı kullanın
logger.info("Bu modül başlatıldı.")
```

## Log Seviyeleri ve Kullanım Alanları

Doğru log seviyesini seçmek, logların anlamlı olmasını sağlar.

| Seviye | Açıklama | Ne Zaman Kullanılmalı? |
| :--- | :--- | :--- |
| `DEBUG` | Geliştirme sırasında hata ayıklamak için gereken ayrıntılı bilgiler. | Bir değişkenin değerini veya bir fonksiyonun akışını takip ederken. |
| `INFO` | Uygulamanın normal akışını gösteren bilgilendirici mesajlar. | Bir işlemin başladığını, bittiğini veya önemli bir kilometre taşına ulaştığını belirtmek için. |
| `WARNING` | Beklenmedik ancak uygulamanın çalışmasını engellemeyen durumlar. | Bir API'den yavaş yanıt alınması, geçici bir bağlantı sorunu gibi potansiyel sorunlar. |
| `ERROR` | Uygulamanın bir işlemi tamamlamasını engelleyen ciddi hatalar. | Veritabanı bağlantı hatası, dosya bulunamaması, geçersiz girdi gibi durumlar. |
| `CRITICAL` | Uygulamanın tamamen çökmesine neden olabilecek çok ciddi hatalar. | Diskte yer kalmaması, belleğin tükenmesi gibi sistemsel krizler. |

## Hata Yönetimi ve Loglama

Hataları loglarken, mümkün olduğunca fazla bağlam sağlamak önemlidir. `try...except` blokları içinde loglama yapmak standart bir pratiktir.

```python
try:
    # Hata potansiyeli olan bir işlem
    result = risky_operation()
    logger.info("Riskli işlem başarıyla tamamlandı.")
except Exception as e:
    # exc_info=True parametresi, hatanın stack trace'ini loga ekler.
    # Bu, hata ayıklama için hayati öneme sahiptir.
    logger.error(f"Beklenmeyen bir hata oluştu: {e}", exc_info=True)
    raise # Hatayı tekrar yükselterek program akışının devam etmesini engelle
```

## Güvenlik: Hassas Bilgileri Loglamaktan Kaçının

**Asla** kullanıcı şifreleri, API anahtarları, token'lar veya kişisel veriler gibi hassas bilgileri loglamayın.

```python
# ❌ YANLIŞ YAKLAŞIM
logger.debug(f"Kullanıcı girişi: {username}, şifre: {password}")

# ✅ DOĞRU YAKLAŞIM
logger.info(f"Kullanıcı girişi denemesi: {username}")
```

Gerekli durumlarda, loglamadan önce veriyi maskeleyen yardımcı fonksiyonlar kullanın.
