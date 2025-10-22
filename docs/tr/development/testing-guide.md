# Test Kılavuzu

## Test Felsefesi ve Gelecek Vizyonu

-   **Birim Testleri (Unit Tests):** Her bir fonksiyonun veya sınıfın, diğer bileşenlerden izole bir şekilde doğru çalıştığını doğrulayan testlerdir. Kodun temel yapı taşlarının sağlamlığını garanti ederler.
-   **Entegrasyon Testleri (Integration Tests):** Birden fazla modülün (örneğin bir API endpoint'inin bir servisi çağırması) birlikte uyum içinde çalıştığını kontrol eden testlerdir. Sistemin bütünsel sağlığı hakkında bilgi verirler.

**Mevcut Durum:** Projenin bu aşamasında test altyapısı planlanmış olup, test kapsamı aktif olarak geliştirilme sürecindedir. Gelecekte eklenecek tüm yeni özelliklerin ve yapılacak hata düzeltmelerinin ilgili testlerle birlikte sunulması hedeflenmektedir.

## Kullanılacak Araçlar

Projemizdeki testleri yazmak ve çalıştırmak için Python ekosisteminin standart aracı olan **Pytest**'i kullanacağız.

-   **Kurulum:** Pytest, `requirements.txt` (veya `requirements-dev.txt`) dosyasına eklenerek projenin geliştirme bağımlılıkları arasında yer alacaktır.

## Testleri Çalıştırma

Test paketi oluşturulduğunda, projenin ana dizinindeyken tüm testleri çalıştırmak için aşağıdaki komut kullanılacaktır:

```bash
pytest
```

## Yeni Testler Nasıl Yazılmalı?

Gelecekte yazılacak testler için aşağıdaki yapı ve standartlar takip edilecektir.

### 1. Dosya Yapısı ve İsimlendirme

-   Tüm test dosyaları, projenin ana dizinindeki `tests/` klasöründe yer alacaktır.
-   `tests/` klasörünün iç yapısı, kaynak kodun bulunduğu `app/` klasörünün yapısını yansıtacaktır.
-   Test dosyalarının ve fonksiyonlarının isimleri `test_` öneki ile başlamalıdır.

**Örnek Yapı:**

```
├── app/
│   └── logic/
│       └── language_detector.py
└── tests/
    └── logic/
        └── test_language_detector.py
```

### 2. Örnek Bir Test Yazımı

Aşağıda, basit bir yardımcı fonksiyon için nasıl bir test yazılabileceğine dair bir örnek bulunmaktadır.

**Test Edilecek Fonksiyon (`app/utils/formatters.py`):**

```python
def normalize_text(text: str) -> str:
    """Metni küçük harfe çevirir ve başındaki/sonundaki boşlukları temizler."""
    if not isinstance(text, str):
        return ""
    return text.strip().lower()
```

**Test Kodu (`tests/utils/test_formatters.py`):**

```python
from app.utils.formatters import normalize_text

def test_normalize_text_with_mixed_case_and_whitespace():
    """Karışık harf ve boşluk içeren metni doğru normalleştirmeli."""
    assert normalize_text("  Hello World  ") == "hello world"

def test_normalize_text_with_empty_string():
    """Boş metin verildiğinde boş metin döndürmeli."""
    assert normalize_text("") == ""

def test_normalize_text_with_already_normalized_string():
    """Zaten normalleştirilmiş metni değiştirmemeli."""
    assert normalize_text("zaten normal") == "zaten normal"
```

Bu kılavuz, Aspectify projesinde tutarlı ve etkili bir test kültürü oluşturmak için bir başlangıç noktasıdır.