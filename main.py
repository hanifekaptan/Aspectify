import asyncio
import json
import os

from app.agents.absa_agent import run_absa
from app.schemas.response.absa_response import ABSAResponse
from app.core.logging_config import logger

async def main():
    logger.info("ABSA uygulaması başlatılıyor...")
    
    test_file_path = "test_data/text/test_texts.jsonl"

    if not os.path.exists(test_file_path):
        logger.error(f"Test dosyası bulunamadı: {test_file_path}")
        print(f"Hata: Test dosyası bulunamadı: {test_file_path}")
        return

    logger.info("Test verileri okunuyor ve duygu analizi yapılıyor...")
    print(f"\n\n{'-'*50}\nTest verileri okunuyor ve duygu analizi yapılıyor...\n{'-'*50}\n")

    results = []
    with open(test_file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= 1:
                break
            data = json.loads(line.strip())
            text = data["text"]
            expected_sentiment = data.get("expected_sentiment", "N/A") # Eğer beklenen duygu yoksa N/A

            print(f"\nAnaliz Edilen Metin: {text}")
            print(f"Beklenen Duygu: {expected_sentiment}")
            
            try:
                logger.info(f"Metin analizi başlatılıyor: {text[:50]}...")
                analysis_result: ABSAResponse = await run_absa(text)
                logger.info(f"Analiz tamamlandı - Polarity: {analysis_result.polarity}, Score: {analysis_result.score}")
                print(f"Ajan Sonucu (Polarite): {analysis_result.polarity}")
                print(f"Ajan Sonucu (Skor): {analysis_result.score}")
                print(f"Ajan Sonucu (Aspektler): {analysis_result.aspects}")
                results.append({
                    "text": text,
                    "expected": expected_sentiment,
                    "actual_polarity": analysis_result.polarity,
                    "actual_score": analysis_result.score
                })
            except Exception as e:
                logger.error(f"Analiz sırasında hata oluştu: {e}")
                print(f"Analiz sırasında hata oluştu: {e}")
                results.append({
                    "text": text,
                    "expected": expected_sentiment,
                    "actual_polarity": "ERROR",
                    "actual_score": 0
                })

            await asyncio.sleep(2) # Kota limitlerini aşmamak için gecikme artırıldı (10 saniye)

    print(f"\n\n{'-'*50}\nAnaliz Özeti\n{'-'*50}\n")
    for res in results:
        print(f"Metin: {res['text']} | Beklenen: {res['expected']} | Gerçek: {res['actual_polarity']} (Skor: {res['actual_score']})")

if __name__ == "__main__":
    asyncio.run(main())

    