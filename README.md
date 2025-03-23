# Ollama_Sound_to_Text

Bu yazdığım Python betiği, mikrofondan gelen sesi metne çevirerek bu metni yerel olarak çalışan bir LLM (Büyük Dil Modeli) olan Ollama’ya gönderir ve cevabını ekrana yazdırır. 

## 📌 Kısaca Ne Yapar?
Bilgisayarındaki mikrofonu dinler.

Konuştuklarını metne çevirir (Google Speech Recognition API’si ile).

Bu metni Ollama isimli yerel yapay zekaya (örneğin Qwen2.5 modeliyle) gönderir.

Modelden gelen cevabı anında terminalde yazdırır ve cevap sürelerini gösterir.


