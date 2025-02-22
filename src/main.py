#!/usr/bin/python3
"""
Fetches a motivational quote and sends it to a Telex channel.
"""

import requests
import os
import json

# Load configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)

TELEX_WEBHOOK = os.getenv("TELEX_WEBHOOK", config["webhook_url"])
QUOTE_API = "https://api.quotable.io/random"

def fetch_quote():
    """Fetches a motivational quote from the API."""
    try:
        response = requests.get(QUOTE_API, timeout=5)
        response.raise_for_status()
        data = response.json()
        return f"🌟 {data['content']} - {data['author']}"
    except requests.RequestException as e:
        print(f"Error fetching quote: {e}")
        return None

def send_to_telex(quote):
    """Sends the quote to the Telex webhook."""
    if not quote:
        print("No quote available to send.")
        return
    
    payload = {"text": quote}
    try:
        response = requests.post(TELEX_WEBHOOK, json=payload, timeout=5)
        response.raise_for_status()
        print("Quote sent successfully!")
    except requests.RequestException as e:
        print(f"Error sending quote to Telex: {e}")

if __name__ == "__main__":
    quote = fetch_quote()
    send_to_telex(quote)
