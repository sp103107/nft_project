# test_config.py
import os
from dotenv import load_dotenv

load_dotenv()

# Test loading Twitter API key
twitter_key = os.getenv("TWITTER_API_KEY")
print(f"Twitter API Key: {twitter_key}")

# Test loading Reddit client ID
reddit_id = os.getenv("REDDIT_CLIENT_ID")
print(f"Reddit Client ID: {reddit_id}")