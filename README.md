# Flight Deal Finder ✈️

A Python-based flight search tool that tracks flight prices and sends notifications when a deal is found. It uses Google Sheets (via Sheety) to manage destinations and Amadeus API for real-time flight data.

## 🚀 Features
- **Dynamic Destination Management**: Uses Google Sheets to store and manage target cities and price thresholds.
- **Automated IATA Lookup**: Automatically finds and fills missing IATA codes for cities in the sheet.
- **Smart Search**: Searches for flights within a 6-month window.
- **Price Alerts**: Sends notifications via SMS or WhatsApp (using Twilio) when a price lower than the threshold is found.

## 🛠️ Setup Instructions

### 1. Requirements
- Python 3.x
- Sheety API Account
- Amadeus API Account
- Twilio Account (for notifications)

### 2. Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flight-deals.git
   cd flight-deals
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Environment Variables
Create a `.env` file in the root directory and add your credentials (refer to `.env.example`):
```env
SHEETY_USERNAME="your_username"
SHEETY_PASSWORD="your_password"
SHEETY_PRICES_ENDPOINT="your_sheety_endpoint"

AMADEUS_API_KEY="your_api_key"
AMADEUS_SECRET="your_api_secret"

TWILIO_SID="your_twilio_sid"
TWILIO_AUTH_TOKEN="your_twilio_token"
TWILIO_VIRTUAL_NUMBER="your_twilio_number"
TWILIO_VERIFIED_NUMBER="your_phone_number"
TWILIO_WHATSAPP_NUMBER="your_whatsapp_sandbox_number"

ORIGIN_CITY_IATA="LON"
```

### 4. Google Sheets Setup
Ensure your Google Sheet (managed via Sheety) has the following columns:
- **City**
- **IATA Code** (can be left blank, the script will fill it)
- **Lowest Price**

## 🖥️ Usage
Run the application using:
```bash
python main.py
```

---

### 🇹🇷 Proje Hakkında (Turkish)
Bu proje, uçak bileti fiyatlarını takip eden ve belirlediğiniz fiyatların altına düştüğünde size WhatsApp veya SMS ile bildirim gönderen bir Python uygulamasıdır. Verileri yönetmek için Google Sheets (Sheety), uçuş aramaları için Amadeus API ve bildirimler için Twilio kullanır.

## 📄 License
This project is open-source and available under the MIT License.
