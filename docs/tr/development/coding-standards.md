# Kodlama Standartları ve Git İş Akışı

Bu belge, Aspectify projesindeki kod kalitesini, okunabilirliğini ve uzun vadeli sürdürülebilirliğini sağlamak için bir rehberdir. Temel felsefemiz, "Temiz Kod" (Clean Code) prensiplerine dayanır; yani kodun sadece çalışması değil, aynı zamanda başka bir geliştirici (buna gelecekteki kendimiz de dahil) tarafından kolayca anlaşılabilmesi hedeflenmektedir.

Bu hedefe ulaşmak için Python'un resmi stil rehberi olan **[PEP 8](https://peps.python.org/pep-0008/)**'i temel alıyoruz.

## Kodlama Standartları

Kodun kalitesini ve tutarlılığını sağlamak için aşağıdaki kurallara ve en iyi pratiklere uyulması beklenmektedir.

### 1. İsimlendirme (Naming Conventions)

Proje genelinde tutarlılığı sağlamak için aşağıdaki isimlendirme kuralları benimsenmiştir:

-   **Değişkenler, Fonksiyonlar ve Modüller:** Küçük harflerle ve kelimeler arasında alt çizgi kullanılarak isimlendirilir (`snake_case`).
    -   *Örnek:* `process_data`, `user_name`
-   **Sınıflar (Classes):** Her kelimenin ilk harfi büyük olacak şekilde isimlendirilir (`PascalCase`).
    -   *Örnek:* `AnalysisService`, `MultiModalRequest`
-   **Sabitler (Constants):** Tamamı büyük harflerle ve kelimeler arasında alt çizgi kullanılarak isimlendirilir (`SCREAMING_SNAKE_CASE`).
    -   *Örnek:* `MAX_RETRIES`, `DEFAULT_TIMEOUT`

### 2. Yorumlar ve Docstring'ler

Anlaşılır kod, kendi kendini belgeleyen koddur. Ancak gerekli durumlarda, kodun "neden" bu şekilde yazıldığını açıklamak kritik öneme sahiptir.

-   Anlaşılması zor veya karmaşık mantık içeren kod bloklarını açıklamak için `#` ile başlayan yorum satırları kullanın.
-   Tüm public modüller, sınıflar ve fonksiyonlar, ne işe yaradıklarını, aldıkları parametreleri ve döndürdükleri değeri açıklayan bir docstring (`"""Docstring burada."""`) içermelidir. Bu, hem kodun anlaşılmasına yardımcı olur hem de gelecekte otomatik dokümantasyon oluşturmayı kolaylaştırır.

### 3. Okunabilirlik ve Basitlik

-   **Tek Sorumluluk Prensibi:** Bir fonksiyonun çok fazla iş yapmasından kaçının. Mümkünse, her fonksiyon iyi tanımlanmış tek bir sorumluluğu yerine getirmelidir.
-   **Tekrardan Kaçınma (DRY - Don't Repeat Yourself):** Tekrar eden mantığı yardımcı fonksiyonlara veya sınıflara taşıyarak kod tekrarını önleyin.
-   **Satır Uzunluğu:** Kodun farklı ekranlarda daha kolay okunmasını sağlamak için satır uzunluğunu ideal olarak 80-100 karakter civarında tutmak, genel kabul görmüş bir pratiktir.

## Git İş Akışı

Temiz bir Git geçmişi, projenin gelişimini anlamak ve olası hataları takip etmek için en değerli araçlarımızdan biridir.

### 1. Branch (Dal) Yönetimi

Her yeni görev için `main` branch'inden yeni bir dal oluşturun. Bu, ana dalı her zaman stabil tutmamızı sağlar. Dal isimleri, yapılan işi özetleyen şu önekleri kullanmalıdır:

-   **`feature/`**: Yeni bir özellik eklerken (örn. `feature/add-caching`)
-   **`fix/`**: Bir hatayı düzeltirken (örn. `fix/login-bug`)
-   **`docs/`**: Dokümantasyonla ilgili değişiklikler yaparken (örn. `docs/update-readme`)

### 2. Commit Mesajları

Anlaşılır bir proje geçmişi, en az kodun kendisi kadar değerlidir. Bu nedenle, "Conventional Commits" standardını takip ediyoruz.

-   **Format:** `<tip>: <kısa açıklama>`
-   **Örnek Tipler:**
    -   **`feat`**: Yeni bir özellik eklendiğinde.
    -   **`fix`**: Bir hata düzeltildiğinde.
    -   **`docs`**: Sadece dokümantasyonda değişiklik yapıldığında.
    -   **`style`**: Kodun anlamını etkilemeyen formatlama değişiklikleri.
    -   **`refactor`**: Bir hatayı düzeltmeyen veya bir özellik eklemeyen kod yeniden düzenlemesi.
    -   **`test`**: Eksik testlerin eklenmesi veya mevcut testlerin düzeltilmesi.
    -   **`chore`**: Build süreci veya yardımcı araçlarla ilgili değişiklikler.

-   **İyi Commit Mesajı Örnekleri:**
    ```
    feat: Add multi-modal request support for audio files
    fix: Correctly handle Unicode characters in text analysis
    docs: Update local setup guide with Docker instructions
    ```