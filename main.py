import time
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# Load environment variables
load_dotenv()

# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Set your origin airport
ORIGIN_CITY_IATA = os.environ.get("ORIGIN_CITY_IATA", "LON")

# ==================== Update the Airport Codes in Google Sheet ====================

# Check IATA code for each row
for row in sheet_data:
    if row["iataCode"] == "":
        # Find missing IATA codes via Amadeus API
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # Small delay to avoid API rate limits
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

# Push updated codes back to Google Sheet
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ==================== Search for Flights and Send Notifications ====================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination}")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    
    # Send alert if price is lower than threshold
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        
        # Send notification via WhatsApp
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )