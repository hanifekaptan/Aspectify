# Sistem Mimarisi

Aspectify, modern Python mimarisi kullanarak geliştirilmiş bir duygu analizi platformudur.

## Genel Mimari

```
┌─────────────────────────────────────────────────────────────┐
│                    Aspectify Platform                       │
├─────────────────────────────────────────────────────────────┤
│  API Layer (FastAPI)                                        │
│  ├── Endpoints & Authentication                             │
│  └── Request/Response Models                                │
├─────────────────────────────────────────────────────────────┤
│  Core Logic & Services Layer                                │
│  ├── Agents (Orchestration & Business Rules)                │
│  ├── Business Services (e.g., AnalysisService)              │
│  └── AI/ML Services (Internal Wrappers)                     │
│      ├── LLM Service (Gemini)                               │
│      └── Transcription Service (Whisper)                    │
├─────────────────────────────────────────────────────────────┤
│  Data Layer                                                 │
│  ├── Database (PostgreSQL, Pinecone)                        │
│  └── File Storage                                           │
└─────────────────────────────────────────────────────────────┘
```

## Modül Yapısı

### 🏗️ Core (Çekirdek)
```
app/core/
├── config.py          # Yapılandırma yönetimi
└── logging_config.py  # Loglama yapılandırması
```

**Sorumluluklar:**
- Uygulama yapılandırması
- Ortam değişkenleri yönetimi
- Loglama sistemi

### 🤖 Agents (Ajanlar)
```
app/agents/
└── absa_agent.py      # Ana ABSA analiz ajanı
```

**Sorumluluklar:**
- İş akışı yönetimi
- Veri işleme koordinasyonu
- Sonuç formatlama

### 🧠 AI Models (AI Modelleri)
```
app/ai_models/
├── llm_models.py           # LLM model yönetimi
└── openai_whisper_models.py # Whisper model yönetimi
```

**Sorumluluklar:**
- AI model bağlantıları
- Model yapılandırması

### 🔧 Logic (Mantık)
```
app/logic/
├── content_type_identifier.py  # İçerik türü belirleme
├── language_detector.py        # Dil tespiti
└── transcriber.py              # Ses transkripsiyonu
```

**Sorumluluklar:**
- İçerik türü analizi
- Dil tespiti
- Ses dosyası işleme

### 🛠️ Tools (Araçlar)
```
app/tools/
└── absa_analyzer.py    # ABSA analiz aracı
```

**Sorumluluklar:**
- Duygu analizi işlemi
- Aspect belirleme
- Sonuç formatlama

### 📋 Schemas (Şemalar)
```
app/schemas/
├── request/
│   └── multi_modal_request.py  # İstek modelleri
└── response/
    ├── absa_response.py        # ABSA yanıt modeli
    ├── aspect_response.py      # Aspect yanıt modeli
    └── llm_response.py         # LLM yanıt modeli
```

**Sorumluluklar:**
- Veri doğrulama
- API sözleşmeleri
- Tip güvenliği

## Veri Akışı

### 1. Giriş İşleme
```
Kullanıcı Girişi → İçerik Türü Belirleme → Dil Tespiti
```

### 2. İçerik Hazırlama
```
Ses Dosyası → Transkripsiyon → Metin
Metin → Doğrudan İşleme
```

### 3. Analiz Süreci
```
Metin → ABSA Aracı → LLM Model → Sonuç
```

### 4. Sonuç Formatlama
```
Ham Sonuç → Pydantic Model → JSON Yanıt
```

## Teknoloji Yığını

### Backend
- **Python 3.10**: Ana programlama dili
- **FastAPI**: Web framework
- **Pydantic**: Veri doğrulama

### AI/ML
- **Google Gemini**: LLM modeli
- **OpenAI Whisper**: Ses transkripsiyonu
- **LangChain**: AI framework

### Altyapı
- **Docker**: Konteynerleştirme
- **MkDocs**: Dokümantasyon
- **GitHub Pages**: Dokümantasyon hosting

## Gelecek Planları

### Kısa Vadeli
- [ ] API endpointleri ve doğrulama
- [ ] Uygulama akışından bağımsız dil belirleme
- [ ] Önbellekleme adımı
- [ ] Analiz öncesi metin ön işleme
- [ ] Web arayüzü
- [ ] Yapısal ve vektör veri tabanı ayarları
- [ ] Logging ayarları

### Uzun Vadeli
- [ ] Gelişmiş prompt yapısını ile görev sınırlandırma
- [ ] İleri seviye analizleme
- [ ] Görsel analiz
- [ ] Backend ekleme
