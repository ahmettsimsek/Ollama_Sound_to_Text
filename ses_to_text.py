# -*- coding: utf-8 -*-
import subprocess
import speech_recognition as sr
import requests
import time
import json

# Mikrofon ve tanıma ayarları
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Ollama'yı başlatma fonksiyonu
def start_ollama():
    ollama_command = ['ollama', 'serve', '--port', '11434']
    ollama_process = subprocess.Popen(
        ollama_command, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        text=True, 
        encoding='utf-8'
    )
    return ollama_process

# Ollama'ya mesaj gönderme fonksiyonu
def send_to_ollama(message):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "qwen2.5:1.5b",
        "prompt": message,
    }
    try:
        # Başlangıç zamanını al
        start_time = time.time()
        
        # Ollama'ya istek gönder
        response = requests.post(url, json=data, stream=True)
        
        # İlk yanıt satırının gelme zamanını hesapla
        first_line_time = None
        
        if response.status_code == 200:
            print("Ollama'dan gelen yanıt:")
            
            for line in response.iter_lines():
                if line and first_line_time is None:
                    # İlk satır geldiğinde zamanı kaydet
                    first_line_time = time.time()
                    initial_response_time = first_line_time - start_time
                    print(f"\nGirişte cevap verme süresi: {initial_response_time:.2f} saniye")
                
                if line:
                    response_data = json.loads(line.decode('utf-8'))
                    if "response" in response_data:
                        print(response_data["response"].encode('utf-8').decode('utf-8'), end="", flush=True)
                    elif "error" in response_data:
                        print("Hata:", response_data["error"], flush=True)
            print()
        else:
            print("Hata:", response.status_code, response.text)
        
        # Bitiş zamanını al
        end_time = time.time()
        
        # Toplam yanıt süresini hesapla
        total_response_time = end_time - start_time
        print(f"\nToplamda cevap verme süresi: {total_response_time:.2f} saniye")
        
    except Exception as e:
        print("Ollama'ya istek gönderme hatası:", e)

# Mikrofondan ses alıp metne çevirme fonksiyonu
def listen_and_convert():
    print("\nDinliyorum...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        recognizer.pause_threshold = 2.0
        recognizer.dynamic_energy_threshold = False
        recognizer.energy_threshold = 300
        print("Konuşabilirsiniz...")

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("Mikrofon zaman aşımına uğradı, tekrar deneyin.")
            return None

    try:
        print("Metne çeviriyorum...")
        text = recognizer.recognize_google(audio, language="tr-TR", show_all=True)
        if isinstance(text, dict) and 'alternative' in text:
            best_result = max(text['alternative'], key=lambda x: x.get('confidence', 0))
            final_text = best_result.get('transcript', '')
            print(f"Duyduğum: {final_text}")
            return final_text
        else:
            print("Sesi anlayamadım.")
            return None
    except sr.UnknownValueError:
        print("Sesi anlayamadım.")
        return None
    except sr.RequestError as e:
        print(f"Google Speech Recognition servisiyle bağlantı hatası: {e}")
        return None

# Ana program
if __name__ == "__main__":
    ollama_process = start_ollama()
    try:
        while True:
            print("Mikrofondan ses alındı, metne çevriliyor...")
            text = listen_and_convert()
            if text:
                print("Ollama'ya gönderilen metin:", text)
                send_to_ollama(text)
    except KeyboardInterrupt:
        print("\nProgram sonlandırıldı.")
        ollama_process.terminate()
