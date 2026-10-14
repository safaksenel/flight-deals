# ✈️ Flight Deal Finder & Automated Twilio WhatsApp/SMS Bot
### *Akıllı Uçak Bileti Fiyat Takip ve Anlık WhatsApp/SMS Bildirim Motoru*

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Twilio](https://img.shields.io/badge/Twilio-WhatsApp%20%2F%20SMS-F22F46?logo=twilio&logoColor=white)](https://www.twilio.com/)
[![Amadeus API](https://img.shields.io/badge/Amadeus-Flight%20Search%20API-1A3B8B?logo=amadeus&logoColor=white)](https://developers.amadeus.com/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

---

## 🇺🇸 [English] Project Overview

A Python-based automated flight search and deal intelligence tool that tracks airfare prices and instantly delivers mobile alerts via WhatsApp/SMS when an exceptional discount is detected. Integrates Google Sheets (via Sheety) for dynamic destination monitoring and Amadeus Flight Search API for real-time global airline routing.

### 🚀 Key Features
- **Dynamic Destination Management**: Uses Google Sheets to store and manage target destinations and maximum price thresholds (`Flight Deals.xlsx` template included).
- **Automated IATA Lookup**: Automatically queries Amadeus API to resolve and populate missing 3-letter IATA city codes.
- **Flexible Horizon Search**: Continuously scans multi-city round trips across a rolling 6-month window.
- **Instant Mobile Alerts**: Dispatches automated Twilio WhatsApp / SMS alerts directly to your phone when prices dip below threshold.

<p align="center">
  <img src="Twilio-MESSAGE.jpeg" alt="WhatsApp Notification" width="400"/>
</p>

### 🛠️ Setup Instructions
1. **Prerequisites**: Python 3.9+, Amadeus API keys, Twilio credentials, Sheety account.
2. **Installation**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Environment Configuration**: Create `.env` based on `.env.example`:
   ```ini
   AMADEUS_API_KEY=your_key
   AMADEUS_API_SECRET=your_secret
   SHEETY_ENDPOINT=your_endpoint
   TWILIO_SID=your_sid
   TWILIO_AUTH_TOKEN=your_token
   ```
4. **Run**:
   ```bash
   python main.py
   ```

---

## 🇹🇷 [Turkish] Proje Özeti

Uçak bileti fiyatlarını gerçek zamanlı takip eden, belirlediğiniz bütçe eşiğinin altına indiğinde WhatsApp / SMS üzerinden anlık alarm gönderen otonom Python aracıdır. Rota ve bütçe yönetimini Google Sheets (Sheety), uçuş aramalarını Amadeus Global API ve anlık bildirimleri Twilio üzerinden yürütür.

### 🚀 Öne Çıkan Özellikler
- **Dinamik Hedef Yönetimi**: Google Sheets üzerinden hedef şehirleri ve fiyat limitlerini yönetme (`Flight Deals.xlsx` şablonu dahildir).
- **Otomatik IATA Kodu Tamamlama**: Eksik şehir kodlarını Amadeus API kullanarak otomatik tamamlama.
- **6 Aylık Tarama Penceresi**: Gelecek 6 ay boyunca en uygun fiyatlı gidiş-dönüş seferlerini analiz etme.
- **Anlık WhatsApp / SMS Uyarıları**: Fırsat bilet yakalandığında cep telefonunuza saniyeler içinde zengin bildirim iletme.

<p align="center">
  <img src="Twilio-MESSAGE.jpeg" alt="WhatsApp Bildirimi" width="400"/>
</p>

### 🛠️ Kurulum Talimatları
```bash
pip install -r requirements.txt
cp .env.example .env
python main.py
```

---

## 👨‍💻 Geliştirici / Author

**Ahmet Şafak Şenel**  
- **GitHub:** [@safaksenel](https://github.com/safaksenel)  
- **LinkedIn:** [Ahmet Şafak Şenel](https://www.linkedin.com/in/%C5%9Fafak-%C5%9Fenel-70a633319/)  
- **Portfolio:** [safaksenel.dev](https://github.com/safaksenel/portfolio)  
