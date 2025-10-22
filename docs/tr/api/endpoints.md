# API Uç Noktaları (Endpoints)

Bu belge, Aspectify API'sinin sunacağı planlanan RESTful uç noktalarını tanımlar.

**⚠️ Mevcut Durum:** Bu API henüz geliştirme aşamasındadır ve bu uç noktalar aktif değildir. Bu doküman, projenin API vizyonunu ve gelecekteki arayüzünü tanımlamak için bir yol haritası niteliğindedir.

---

## Planlanan Uç Noktalar

### Analiz Başlatma

-   **Endpoint:** `POST /analyze`
-   **Açıklama:** Yeni bir metin veya ses analizi görevi başlatır. Bu, sistemin ana işlevsel uç noktasıdır.
-   **Request Body:** `MultiModalRequest` şemasına uygun bir JSON nesnesi bekler.
-   **Başarılı Yanıt (200 OK):** `ABSAResponse` şemasına uygun bir JSON nesnesi döndürür.

**Örnek İstek (`curl`):**```bash
curl -X POST "http://localhost:8000/analyze" \
-H "Content-Type: application/json" \
-d '{
  "content": "Servis çok hızlıydı ama yemekler soğuktu.",
  "content_type": "text"
}'
```

---

### Görev Durumunu Sorgulama (Gelecek için)

-   **Endpoint:** `GET /tasks/{task_id}`
-   **Açıklama:** Özellikle büyük ses dosyaları gibi uzun sürebilecek asenkron analiz görevlerinin durumunu sorgulamak için planlanmıştır.
-   **Request Body:** Yok.
-   **Başarılı Yanıt (200 OK):** Görevin durumunu ('PENDING', 'SUCCESS', 'FAILED') ve başarılıysa analiz sonucunu içeren bir JSON nesnesi döndürür.