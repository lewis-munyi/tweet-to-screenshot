import os
from dotenv import load_dotenv

load_dotenv()

# Load Twitter API credentials
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_key = os.getenv("ACCESS_KEY")
access_secret = os.getenv("ACCESS_SECRET")

# Add/Remove usernames of people who's tweets we want to gather.
profiles = [
    "lewismunyi",
    "BarackObama",
    "KanyeWest",
    "MKBHD",
    "jimmyfallon",
    "TheEllenShow",
    "rihanna"
]