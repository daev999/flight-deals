# ✈️ Flight Deals

A Python application that searches for the cheapest flights using the SerpAPI Google Flights API and automatically updates a Google Sheet whenever a lower fare is found.

This project was built as part of **Day 39 of the 100 Days of Code: Python Bootcamp by Dr. Angela Yu**.

---

## 📌 Features

- Search for flights from London (LHR) to multiple destinations.
- Retrieve flight data using the SerpAPI Google Flights API.
- Find the cheapest available flight.
- Compare the flight price with the stored lowest price in Google Sheets.
- Automatically update the spreadsheet when a cheaper flight is found.
- Handle missing flight prices gracefully.
- Cache API requests to reduce unnecessary API calls.

---

## 🛠 Technologies Used

- Python 3
- Requests
- Requests Cache
- Sheety API
- SerpAPI (Google Flights)
- python-dotenv

---

## 📂 Project Structure

```text
flight-deals/
│
├── main.py                 # Coordinates the entire application
├── flight_search.py        # Handles communication with the SerpAPI
├── flight_data.py          # Finds and structures the cheapest flight
├── data_manager.py         # Reads and updates the Google Sheet
├── .env                    # Stores API keys and credentials
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. Retrieve destination data from Google Sheets.
2. Loop through every destination.
3. Search for available flights.
4. Find the cheapest flight.
5. Compare it with the stored lowest price.
6. Update the spreadsheet if a lower price is found.

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
SERP_API_KEY=your_serpapi_key
SERP_API_ENDPOINT=your_serpapi_endpoint

SHEETY_ENDPOINT=your_sheety_endpoint
SHEETY_USERNAME=your_sheety_username
SHEETY_PASSWORD=your_sheety_password
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/flight-deals.git
```

Move into the project folder:

```bash
cd flight-deals
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create your `.env` file with your API credentials.

Run the project:

```bash
python main.py
```

---

## 📖 What I Learned

This project helped me practise:

- Working with REST APIs
- Environment variables and protecting secrets
- Object-Oriented Programming (OOP)
- Working across multiple Python modules
- Structuring larger Python applications
- Parsing nested JSON data
- Error handling with `try` / `except`
- Updating data using the Sheety API
- Request caching to minimise API usage

---

## 🚀 Future Improvements

- Send email notifications when cheaper flights are found.
- Add SMS or WhatsApp notifications.
- Allow users to subscribe to flight alerts.
- Support multiple departure airports.
- Schedule automatic daily flight searches.

---

## 🙏 Acknowledgements

This project was completed as part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

It has been adapted and extended as part of my own Python learning journey.

---

## 📄 License

This project is licensed under the MIT License.