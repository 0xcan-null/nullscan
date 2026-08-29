# nullscan
# ⚡ NullScan - Multi-Threaded CLI Port Scanner

`NullScan`, hedef IP veya domain üzerindeki açık portları tespit etmek ve temel servis analizini yapmak için Python ile geliştirilmiş hızlı ve hafif bir port tarayıcıdır.

---

## 🚀 Özellikler
- 🧵 **Multi-Threading:** Eşzamanlı ve yüksek hızlı port taraması.
- 🎯 **Servis Tanıma:** Yaygın portlar (SSH, HTTP, FTP vb.) için otomatik servis eşleştirmesi.
- 📡 **Banner Grabbing:** Açık portlardan servis yanıtlarını yakalama.
- 🎨 **Terminal UI:** Temiz ve renkli terminal arayüzü.

---

## 🛠️ Kurulum & Kullanım

bash
# Repoyu klonlayın
git clone https://github.com/0xcan-null/nullscan.git

# Proje dizinine gidin
cd nullscan

# Temel tarama (1-1024 arası portlar)
python3 nullscan.py -t scanme.nmap.org

# Özel port aralığı ve thread sayısı ile tarama
python3 nullscan.py -t 127.0.0.1 -p 1-5000 -w 150
