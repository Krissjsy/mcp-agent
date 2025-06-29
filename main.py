import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key securely
API_KEY = os.getenv("OPENAI_API_KEY")

# Use it
print("Loaded API key:", API_KEY)
