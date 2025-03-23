# Ollama_Sound_to_Text

Bu yazdığım Python betiği, mikrofondan gelen sesi metne çevirerek bu metni yerel olarak çalışan bir LLM (Büyük Dil Modeli) olan Ollama’ya gönderir ve cevabını ekrana yazdırır. 

## 📌 Kısaca Ne Yapar?
Bilgisayarındaki mikrofonu dinler.

Konuştuklarını metne çevirir (Google Speech Recognition API’si ile).

Bu metni Ollama isimli yerel yapay zekaya (örneğin Qwen2.5 modeliyle) gönderir.

Modelden gelen cevabı anında terminalde yazdırır ve cevap sürelerini gösterir.

## ⚙️ Çalıştırmak İçin Gerekenler
✅ GEREKLİ KURULUMLAR
Python 3.8+ yüklü olmalı.

Terminal veya Komut İstemcisi (CMD, PowerShell ya da bash) kullanıyor olmalısın.

📦 GEREKLİ KÜTÜPHANELERİ KUR
```
python
pip install speechrecognition requests pyaudio
```
🔴 Not: pyaudio bazı sistemlerde kurulum hatası verebilir. Eğer hata alırsan, şu komutu dene:

Windows:

bash
Kopyala
Düzenle
pip install pipwin
pipwin install pyaudio
macOS:

bash
Kopyala
Düzenle
brew install portaudio
pip install pyaudio
🧠 OLLAMA MODELİNİ YÜKLE
https://ollama.com adresinden Ollama'yı indir ve kur.

Terminalde aşağıdaki komutla bir model indir:

bash
Kopyala
Düzenle
ollama pull qwen2.5:1.5b
veya

bash
Kopyala
Düzenle
ollama pull mistral
Model yüklendikten sonra, script içerisindeki "model": "qwen2.5:1.5b" kısmını değiştirmene gerek yok (ama istersen mistral, llama3, gemma vb. modellerle değiştirebilirsin).

▶️ ÇALIŞTIRMA
Betik dosyasını örneğin voice_assistant.py olarak kaydet.

Terminalde bulunduğun klasöre git:

bash
Kopyala
Düzenle
cd /dosya/yolu/voice_assistant_klasoru
Çalıştır:

bash
Kopyala
Düzenle
python voice_assistant.py
🗣️ NASIL KULLANILIR?
Terminalde "Konuşabilirsiniz..." mesajı geldiğinde mikrofonunu kullanarak konuş.

Sistem bunu metne çevirip Ollama'ya gönderir.

Ollama'dan gelen cevabı ve yanıt süresini terminalde görürsün.

💡 Örnek Kullanım Senaryosu
"Bugün İstanbul’da hava nasıl?" dersen, sistem bunu Ollama’ya iletir ve modelin verdiği bilgiyi döndürür.

Türkçe konuşabilir ve Türkçe yanıt alırsın (model Türkçeyi destekliyorsa).

⚠️ Dikkat Etmen Gerekenler
Modelin çalışıyor olması gerekir. Ollama port 11434’te hizmet veriyor olmalı.

İnternet bağlantısı sadece Google Speech API için gereklidir. Ollama offline çalışır.

Google API günlük limitlerine takılırsan, farklı Speech-to-Text sistemleri (örneğin Whisper) ile değiştirebilirsin.


